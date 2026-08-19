---
name: investigate-failure
description: Read-only investigation of a failure — CI break, regression, incident. Returns structured findings and recommended fix path without editing code unless scope expands.
---

Supervisor skill for failure investigation.

1. Read `${CLAUDE_PLUGIN_ROOT}/workflows/research.md` and `${CLAUDE_PLUGIN_ROOT}/roles/researcher.md`.
2. Resolve the target bundle config for `ci.local_command` and conventions:
   `scripts/bundle_registry.py resolve --bundle <bundle> --root
   <target-repo-root>` (`${CLAUDE_PLUGIN_ROOT}/scripts/bundle_registry.py`
   in a plugin-only session) — see `repos/README.md` "Resolution order".
   No legacy `.agentic/harness.yaml` / `repos/<bundle>.yaml` fallback
   (issue #327).
3. Dispatch `researcher` with failure context (logs, failing test, issue).
4. Output: root-cause hypothesis, evidence, suggested subtasks for implementor.

Do not edit product files unless the user explicitly expands scope.
