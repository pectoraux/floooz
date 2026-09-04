#!/usr/bin/env python3
"""Validate the repository bootstrap/governance contracts used by fresh agents."""

from __future__ import annotations

import json
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


def fail(message: str) -> None:
    raise SystemExit(f"repository validation failed: {message}")


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
    expected_ids = [f"FZ-{number:03d}" for number in range(1, 51)]
    if ids != expected_ids:
        fail("program state work items must be ordered exactly FZ-001 through FZ-050")

    ready = [item for item in items if item.get("status") == "READY"]
    if [item.get("id") for item in ready] != ["FZ-001"]:
        fail("bootstrap state must have only FZ-001 READY")

    blocked = {item.get("id") for item in items if item.get("status") == "BLOCKED"}
    expected_blocked = set(expected_ids[1:])
    if blocked != expected_blocked:
        fail("all work items after FZ-001 must remain BLOCKED until dependencies are satisfied")

    print("repository validation passed")
    print(f"required governance files: {len(REQUIRED_FILES)}")
    print(f"work items: {len(items)}")
    print("eligible work item: FZ-001")


if __name__ == "__main__":
    main()
