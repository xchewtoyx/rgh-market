---
name: research
description: Read-only exploration for a registered bundle. Returns a structured research brief without code changes. Use for spikes, design questions, or planner open_questions.
---

You supervise the research loop.

1. Read `${CLAUDE_PLUGIN_ROOT}/workflows/research.md` in full.
2. Resolve the target bundle config for constraint context via
   `scripts/bundle_registry.py resolve --bundle <bundle> --root
   <target-repo-root>` (`${CLAUDE_PLUGIN_ROOT}/scripts/bundle_registry.py`
   in a plugin-only session) — see `repos/README.md` "Resolution order".
   No legacy `repos/<bundle>.yaml` fallback (issue #327).
3. Dispatch `researcher` per `${CLAUDE_PLUGIN_ROOT}/roles/researcher.md`.

Do not edit files or open PRs unless the user explicitly expands scope.
