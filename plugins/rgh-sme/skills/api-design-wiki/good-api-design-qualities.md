---
type: concept
title: Good API Design Qualities
description: >
  Four contract-level goals — operational, expressive, simple, predictable —
  that guide surface design beyond bare functional correctness.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 1"
---

Users want functionality **programmatically**; a GUI would suffice otherwise. A
**good** API balances:

- **Operational** — meets functional requirements and non-functional needs
  (latency, accuracy). Useless if the backend cannot deliver.
- **Expressive** — callers state intent directly. Hiding capability forces
  workarounds (detecting language by calling translate with every target language
  instead of a dedicated detect operation).
- **Simple** — not minimizing RPC count via one mega `ExecuteAction` that moves
  complexity into opaque configuration. Expose the common path directly; make the
  advanced path possible without burdening typical users ("make the common case
  awesome and the advanced case possible").
- **Predictable** — repeated patterns in naming and behavior so clients generalize
  from prior calls ([API wire naming](api-wire-naming.md): if `TranslateText`
  uses field `text`, `DetectLanguage` should too, not `inputText`). Inconsistent
  surfaces from multiple teams stall productivity.

These qualities organize pattern choices across resource modeling, methods, and
evolution — not a checklist separate from design decisions. They complement
[architecturally significant API requirements](architecturally-significant-api-requirements.md)
and [developer experience](developer-experience.md) from the Patterns for API Design
framing.
