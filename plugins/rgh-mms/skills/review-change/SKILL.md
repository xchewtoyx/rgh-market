---
name: review-change
description: Review a branch or PR against harness policy and product conventions. Dispatches reviewer role only — no implementation.
---

Supervisor skill for standalone review.

1. Read `policy/review-policy.md` and `roles/reviewer.md`.
2. Load product `AGENTS.md`, `.agentic/local-policy.md`, and review checklist.
3. Dispatch `reviewer`; return approve or request_changes with batched findings.

Does not verify acceptance criteria — use approver or implement-feature loop for that.
