---
name: contract-first-change
description: Drives a load-bearing change through contract scaffold, implement, review, and settle. Use when manifest contracts.enabled is true and the change affects harness or runtime behavior.
---

You supervise the contract-first change loop.

1. Read `workflows/contract-first-change.md` in full.
2. Load `repos/<bundle>.yaml` — require `contracts.enabled: true`.
3. Dispatch roles per the workflow; defer to `roles/*.md`.

Never skip contract scaffold before load-bearing edits when contracts are enabled.
