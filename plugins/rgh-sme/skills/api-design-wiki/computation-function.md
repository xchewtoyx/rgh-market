---
type: concept
title: Computation Function
description: >
  A side-effect-free remote function whose result depends only on request input
  and neither reads nor writes provider application state.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 5"
---

A **computation function** `cf: in -> out` outsources deterministic or
trust-sensitive calculation — validation, format conversion, scoring — when
local execution is costly, slow, or lacks expertise.

Forces: trust and reproducibility across the network; latency and payload size;
provider CPU/RAM vs client capacity.

Neither reads nor changes server-side state. Document preconditions on request
elements and postconditions on responses. No transaction management.

**Variants:**

- **Transformation service** — schema or notation conversion (XML↔JSON) without
  semantic change.
- **Validation service** — checks input correctness before a separate
  computation or [state transition operation](state-transition-operation.md);
  if it consults stored rules, it becomes a
  [retrieval operation](retrieval-operation.md) variant.
- **Long-running computation** — async via messaging, callback, or
  [long-running operation](long-running-operation.md) with progress polling.

Stateless operations scale and relocate easily (serverless-friendly). Caching
helps only when many clients repeat the same input. `heartbeat` health checks
are a minimal validation-style example.

Differs from [retrieval operation](retrieval-operation.md), which consults
provider state read-only.
