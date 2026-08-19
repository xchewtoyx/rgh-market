---
name: investigate-failure
description: Read-only investigation of a failure — CI break, regression, incident. Returns structured findings and recommended fix path without editing code unless scope expands.
---

Supervisor skill for failure investigation.

1. Read `workflows/research.md` and `roles/researcher.md`.
2. Load product `.agentic/harness.yaml` for CI command and local policy.
3. Dispatch `researcher` with failure context (logs, failing test, issue).
4. Output: root-cause hypothesis, evidence, suggested subtasks for implementor.

Do not edit product files unless the user explicitly expands scope.
