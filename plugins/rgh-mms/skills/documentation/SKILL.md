---
name: documentation
description: Docs-only change loop for a registered bundle — implementor then reviewer, lighter than full milestone delivery. Use for README, AGENTS.md, and guide updates without behavior changes.
---

You supervise the documentation loop.

1. Read `${CLAUDE_PLUGIN_ROOT}/workflows/documentation.md` in full.
2. Resolve the target bundle config: `scripts/bundle_registry.py resolve
   --bundle <bundle> --root <target-repo-root>`
   (`${CLAUDE_PLUGIN_ROOT}/scripts/bundle_registry.py` in a plugin-only
   session) — see `repos/README.md` "Resolution order". No legacy
   `repos/<bundle>.yaml` fallback (issue #327).
3. Dispatch `implementor` then `reviewer` per harness agent specs.

Skip approver unless the work item has explicit acceptance criteria.
