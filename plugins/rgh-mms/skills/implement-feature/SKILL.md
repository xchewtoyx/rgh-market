---
name: implement-feature
description: End-to-end feature implementation for a pinned product repo — plan, implement, review, approve, PR, then land per delivery.integration_mode (human per-issue or milestone-aggregate). Use for issues and milestones.
---

Supervisor skill for feature delivery.

1. Read `workflows/milestone-delivery.md` (canonical).
2. Load product `.agentic/harness.yaml` and `AGENTS.md`.
3. Dispatch roles from `roles/` via client harness in `harnesses/`.
4. Follow `policy/change-safety.md` round caps, escalation, and
   default-branch merge gate.
5. Honor `delivery.integration_mode`: `per-issue` waits for human merge to
   default; `milestone-aggregate` merges approved issue PRs into the milestone
   tracking branch and reserves the human gate for the bulk aggregation PR.

Alias: same loop as `milestone-delivery` skill with product-contract resolution.
