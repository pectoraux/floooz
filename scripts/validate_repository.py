#!/usr/bin/env python3
"""Validate the repository bootstrap/governance contracts used by fresh agents.

Enforces the durable invariants documented in:
- AGENTS.md (roadmap authority / synchronized state)
- spec/implementation-roadmap.md (update protocol, work-item status ledger)
- spec/development-state/program-state.json (machine-readable progress authority)

The validator is state-independent: it accepts any synchronized, dependency-
consistent program state, not just the bootstrap state.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "AGENTS.md",
    "GEMINI.md",
    "ZAI.md",
    "README.md",
    "spec/architecture-lock.md",
    "spec/architecture.md",
    "spec/requirements.md",
    "spec/work-items.md",
    "spec/work-orders.md",
    "spec/dependency-graph.md",
    "spec/implementation-roadmap.md",
    "spec/implementation-map.md",
    "spec/development-state/program-state.json",
    "docs/implementation/IMPLEMENTATION-GUIDE.md",
    "docs/implementation/FRESH-AGENT-CONTEXT.md",
    "docs/android/ANDROID-IMPLEMENTATION.md",
    "docs/android/FZ-ANDROID-WORKSTREAM.md",
    "docs/integrations/WORKFLOWOS.md",
)

STATUS_READY = "READY"
STATUS_BLOCKED = "BLOCKED"
STATUS_FINAL = "FINAL"
VALID_STATUSES = (STATUS_READY, STATUS_BLOCKED, STATUS_FINAL)

# Roadmap ledger rendering of each machine status (see spec/implementation-roadmap.md).
LEDGER_GLYPH = {
    STATUS_READY: "🟦 READY",
    STATUS_BLOCKED: "⬜ BLOCKED",
    STATUS_FINAL: "✅ FINAL",
}

LEDGER_ROW = re.compile(
    r"^\|\s*(FZ-\d{3})\s*\|\s*(🟦 READY|⬜ BLOCKED|✅ FINAL)\s*\|"
)

EXPECTED_IDS = tuple(f"FZ-{number:03d}" for number in range(1, 51))


def fail(message: str) -> None:
    raise SystemExit(f"repository validation failed: {message}")


def require_evidence(item: dict, item_id: str) -> dict:
    """FINAL requires objective PR/CI acceptance evidence (roadmap update protocol)."""
    evidence = item.get("acceptedVia")
    if not isinstance(evidence, dict):
        fail(f"{item_id} is FINAL without an 'acceptedVia' evidence record")
    pr = evidence.get("pr")
    if not isinstance(pr, int) or pr < 1:
        fail(f"{item_id} acceptedVia.pr must be a positive integer pull request number")
    ci_run = evidence.get("ciRun")
    if not isinstance(ci_run, str) or not ci_run.startswith("https://"):
        fail(f"{item_id} acceptedVia.ciRun must be a URL to the objective CI evidence")
    branch = evidence.get("branch")
    if not isinstance(branch, str) or not branch:
        fail(f"{item_id} acceptedVia.branch must be the acceptance branch name")
    return evidence


def main() -> None:
    for relative in REQUIRED_FILES:
        path = ROOT / relative
        if not path.is_file():
            fail(f"required source-of-truth file is missing: {relative}")

    state_path = ROOT / "spec/development-state/program-state.json"
    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"program-state.json is not valid JSON: {exc}")

    if state.get("sourceOfTruth") != "repository":
        fail("program state must declare the repository as source of truth")

    roadmap = state.get("roadmap")
    if not isinstance(roadmap, dict):
        fail("program state must contain roadmap metadata")

    if roadmap.get("path") != "spec/implementation-roadmap.md":
        fail("program state roadmap path must be spec/implementation-roadmap.md")
    if roadmap.get("status") != "FROZEN":
        fail("implementation roadmap must be FROZEN")
    if roadmap.get("machineCounterpart") != "spec/development-state/program-state.json":
        fail("roadmap machine counterpart must point back to program-state.json")
    if roadmap.get("synchronizationRequired") is not True:
        fail("roadmap/program-state synchronization must be required")

    roadmap_text = (ROOT / "spec/implementation-roadmap.md").read_text(encoding="utf-8")
    if "**Status:** FROZEN" not in roadmap_text:
        fail("human-readable implementation roadmap must declare FROZEN status")
    if "spec/development-state/program-state.json" not in roadmap_text:
        fail("roadmap must identify the machine progress authority")

    items = state.get("items")
    if not isinstance(items, list) or len(items) != 50:
        fail("program state must define exactly 50 FZ work items")

    ids = [item.get("id") for item in items if isinstance(item, dict)]
    if ids != list(EXPECTED_IDS):
        fail("program state work items must be ordered exactly FZ-001 through FZ-050")

    status_by_id: dict[str, str] = {}
    for item in items:
        item_id = item.get("id")
        status = item.get("status")
        if status not in VALID_STATUSES:
            fail(f"{item_id} has invalid status {status!r}; expected one of {VALID_STATUSES}")

        depends_on = item.get("dependsOn")
        if not isinstance(depends_on, list):
            fail(f"{item_id} must declare a dependsOn list")
        for dep in depends_on:
            if dep not in EXPECTED_IDS:
                fail(f"{item_id} depends on unknown work item {dep!r}")
            if dep not in ids:
                fail(f"{item_id} dependency {dep!r} is not present in the item list")
            if EXPECTED_IDS.index(dep) >= EXPECTED_IDS.index(item_id):
                fail(f"{item_id} dependency {dep!r} must precede it (dependency graph must stay acyclic)")

        if status == STATUS_FINAL:
            require_evidence(item, item_id)

        status_by_id[item_id] = status

    # Dependency-eligibility invariant: an item is READY only when every hard
    # dependency is FINAL, must be BLOCKED while any dependency is incomplete,
    # and a FINAL item's dependencies must remain FINAL.
    ready: list[str] = []
    for item in items:
        item_id = item["id"]
        status = item["status"]
        deps_final = all(status_by_id[dep] == STATUS_FINAL for dep in item["dependsOn"])

        if status == STATUS_READY:
            if not deps_final:
                unmet = [dep for dep in item["dependsOn"] if status_by_id[dep] != STATUS_FINAL]
                fail(f"{item_id} is READY but dependencies are not FINAL: {', '.join(unmet)}")
            ready.append(item_id)
        elif status == STATUS_BLOCKED:
            if deps_final and item["dependsOn"]:
                fail(f"{item_id} is BLOCKED although every dependency is FINAL; it must be READY")
        elif status == STATUS_FINAL:
            if not deps_final:
                unmet = [dep for dep in item["dependsOn"] if status_by_id[dep] != STATUS_FINAL]
                fail(f"{item_id} is FINAL but dependencies regressed: {', '.join(unmet)}")

    # Roadmap ledger synchronization: the human-readable ledger must render the
    # exact machine status for all 50 work items.
    ledger_rows: dict[str, str] = {}
    for line in roadmap_text.splitlines():
        match = LEDGER_ROW.match(line)
        if match:
            ledger_rows[match.group(1)] = match.group(2)
    if len(ledger_rows) != 50:
        missing = [fid for fid in EXPECTED_IDS if fid not in ledger_rows]
        if missing:
            fail(f"roadmap ledger is missing rows for: {', '.join(missing)}")
        fail("roadmap ledger must contain exactly 50 work-item rows")
    for item_id, status in status_by_id.items():
        expected_glyph = LEDGER_GLYPH[status]
        if ledger_rows[item_id] != expected_glyph:
            fail(
                f"roadmap ledger/{item_id} shows {ledger_rows[item_id]!r} but program state says "
                f"{status!r} ({expected_glyph!r}); synchronize the roadmap and machine state"
            )

    final_items = [fid for fid in EXPECTED_IDS if status_by_id[fid] == STATUS_FINAL]
    blocked_count = sum(1 for fid in EXPECTED_IDS if status_by_id[fid] == STATUS_BLOCKED)

    print("repository validation passed")
    print(f"required governance files: {len(REQUIRED_FILES)}")
    print(f"work items: {len(items)}")
    print(f"final: {len(final_items)} ({', '.join(final_items) if final_items else 'none'})")
    print(f"ready: {len(ready)} ({', '.join(ready) if ready else 'none'})")
    print(f"blocked: {blocked_count}")
    print("roadmap ledger synchronized with program state")


if __name__ == "__main__":
    main()
