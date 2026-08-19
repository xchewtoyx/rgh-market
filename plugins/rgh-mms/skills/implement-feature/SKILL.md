---
name: implement-feature
description: End-to-end feature implementation for a pinned product repo — plan, implement, review, approve, PR, then land per delivery.integration_mode (human per-issue or milestone-aggregate). Use for issues and milestones.
---

Supervisor skill for feature delivery.

1. Read `${CLAUDE_PLUGIN_ROOT}/workflows/milestone-delivery.md` (canonical).
2. Resolve the target bundle config: `scripts/bundle_registry.py resolve
   --bundle <bundle> --root <target-repo-root>`
   (`${CLAUDE_PLUGIN_ROOT}/scripts/bundle_registry.py` in a plugin-only
   session) — see `repos/README.md` "Resolution order". No legacy
   `.agentic/harness.yaml` / `repos/<bundle>.yaml` fallback (issue #327).
3. Read product `AGENTS.md`.
4. Dispatch roles from `roles/` via client harness in `harnesses/`.
5. Follow `${CLAUDE_PLUGIN_ROOT}/policy/change-safety.md` round caps, escalation, and
   default-branch merge gate.
6. Honor `delivery.integration_mode`: `per-issue` waits for human merge to
   default; `milestone-aggregate` merges approved issue PRs into the milestone
   tracking branch and reserves the human gate for the bulk aggregation PR.

Alias: same loop as `milestone-delivery` skill, resolved via the same
layered config resolver (step 2 above).
