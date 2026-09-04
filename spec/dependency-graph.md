# Floooz Dependency Graph

```text
FZ-001 -> FZ-002 -> FZ-003 -> FZ-004 -> FZ-006 -> FZ-007
FZ-001 -> FZ-005
FZ-003 + FZ-006 -> FZ-008
FZ-008 -> FZ-009,FZ-010,FZ-011,FZ-015,FZ-036,FZ-042
FZ-010 + FZ-011 -> FZ-012 -> FZ-013 -> FZ-014
FZ-015 -> FZ-016 -> FZ-017 -> FZ-018 -> FZ-019
FZ-001 -> FZ-020 -> FZ-021
FZ-020 -> FZ-022 -> FZ-023 -> FZ-024
FZ-021 + FZ-024 -> FZ-025 -> FZ-026
FZ-006 + FZ-020 -> FZ-027 -> FZ-028
FZ-028 + FZ-026 -> FZ-029
FZ-029 + FZ-025 -> FZ-030 -> FZ-031 -> FZ-032
FZ-006 -> FZ-033 -> FZ-034
FZ-034 + FZ-025 -> FZ-035
FZ-036 -> FZ-037,FZ-038
FZ-038 -> FZ-039
FZ-006 -> FZ-040
FZ-037 + FZ-040 -> FZ-041
FZ-042 -> FZ-043 -> FZ-044
FZ-020 + FZ-022 -> FZ-045
FZ-045 + FZ-025 -> FZ-046
FZ-008 + FZ-006 -> FZ-047 -> FZ-048
FZ-013 + FZ-014 -> FZ-049 -> FZ-050 (also depends on FZ-040)
```

Only FZ-001 is initially READY. All others are BLOCKED until every dependency is complete. Cross-cutting rule: no production side effect before FZ-025 is complete.