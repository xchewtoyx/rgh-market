---
type: concept
title: Operation Responsibility Patterns
description: >
  Four recurring read/write profiles for endpoint operations — computation,
  retrieval, state creation, and state transition — that classify how work
  touches provider state.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 5"
---

Every endpoint operation fits one of four **operation responsibility**
patterns (Figure 5.19):

| Pattern | Read state | Write state |
| --- | --- | --- |
| [Computation function](computation-function.md) | No | No |
| [Retrieval operation](retrieval-operation.md) | Yes | No |
| [State creation operation](state-creation-operation.md) | No* | Yes |
| [State transition operation](state-transition-operation.md) | Yes | Yes |

\*State creation may read minimally (duplicate-key checks) but its purpose is
append/write.

State-preserving responsibilities behave like **functions** (self-contained
work for the client). State-changing responsibilities are **operations**
(client hands data in; provider stores or transforms it for later retrieval).

Classify each operation in the API description with its read/write profile —
undocumented mixed stateful/stateless behavior harms cohesion and complicates
load balancing. Most creation, retrieval, and computation calls can be
[idempotent](request-deduplication-and-idempotency-keys.md); some transitions
(start activity) inherently are not.

See sibling notes for each pattern's variants (event notification, bulk
report, status check, business activity processor, validation service, long-
running computation).
