---
name: contract-first-change
description: Drives a load-bearing change through contract scaffold, implement, review, and settle. Use when manifest contracts.enabled is true and the change affects harness or runtime behavior.
---

You supervise the contract-first change loop.

1. Read `${CLAUDE_PLUGIN_ROOT}/workflows/contract-first-change.md` in full.
2. Resolve the target bundle config: `scripts/bundle_registry.py resolve
   --bundle <bundle> --root <target-repo-root>`
   (`${CLAUDE_PLUGIN_ROOT}/scripts/bundle_registry.py` in a plugin-only
   session) — see `repos/README.md` "Resolution order". Require
   `contracts.enabled: true`. No legacy `repos/<bundle>.yaml` fallback
   (issue #327).
3. Dispatch roles per the workflow; defer to `roles/*.md`.

Never skip contract scaffold before load-bearing edits when contracts are enabled.
