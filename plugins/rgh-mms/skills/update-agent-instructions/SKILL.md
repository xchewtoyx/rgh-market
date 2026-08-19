---
name: update-agent-instructions
description: Docs-only update to AGENTS.md, local-policy, or harness-generated adapters. Uses documentation workflow with accuracy gates.
---

Supervisor skill for instruction and policy doc updates.

1. Read `${CLAUDE_PLUGIN_ROOT}/workflows/documentation.md`.
2. Resolve the target bundle config: `scripts/bundle_registry.py resolve
   --bundle <bundle> --root <target-repo-root>`
   (`${CLAUDE_PLUGIN_ROOT}/scripts/bundle_registry.py` in a plugin-only
   session) — see `repos/README.md` "Resolution order". No legacy
   `.agentic/harness.yaml` / `repos/<bundle>.yaml` fallback for config
   resolution (issue #327) — a pinned product's own `.agentic/harness.yaml`
   remains the separate, unaffected contract format for adapter generation
   below. If editing generated adapters, run `scripts/generate-adapters.py`
   instead of hand-editing `.agentic/generated/`.
3. Dispatch implementor then reviewer.

Hand-editable: `AGENTS.md` bootstrap, `.agentic/local-policy.md`, `.agentic/harness.yaml`.
Not hand-editable: `.agentic/generated/`, client adapter files with provenance headers.
