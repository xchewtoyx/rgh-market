---
name: update-agent-instructions
description: Docs-only update to AGENTS.md, local-policy, or harness-generated adapters. Uses documentation workflow with accuracy gates.
---

Supervisor skill for instruction and policy doc updates.

1. Read `workflows/documentation.md`.
2. Load product `.agentic/harness.yaml` — if editing generated adapters, run
   `scripts/generate-adapters.py` instead of hand-editing `.agentic/generated/`.
3. Dispatch implementor then reviewer.

Hand-editable: `AGENTS.md` bootstrap, `.agentic/local-policy.md`, `.agentic/harness.yaml`.
Not hand-editable: `.agentic/generated/`, client adapter files with provenance headers.
