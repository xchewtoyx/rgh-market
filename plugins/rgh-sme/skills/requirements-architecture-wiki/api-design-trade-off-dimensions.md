---
type: concept
title: API Design Trade-Off Dimensions
description: >
  Recurring API design dimensions — endpoint generality, granularity,
  chattiness, data currency, and contract stability — each force explicit
  trade-off documentation before an architectural decision is committed.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann, Stocker, Lübke, Zdun, Pautasso), ch. 1"
---

API designs differ along a small set of recurring dimensions. Each is a
[documenting trade-offs](documenting-trade-offs.md) opportunity: name the
options, the forces on each side, and which was chosen in the
[architectural decision record](architectural-decision-capture.md).

- **Endpoint generality** — one general endpoint versus many specialized
  ones (reusability across clients versus fit for specific use cases).
- **Operation granularity** — fine-grained versus coarse-grained scope
  (matching, aggregating, or splitting underlying system functionality in
  one call).
- **Chattiness** — few rich operations versus many small ones (affects
  understandability, performance, scalability, bandwidth, and
  evolvability).
- **Data currency versus correctness** — stale-but-available data versus
  strict consistency; polling versus event-driven or streaming updates;
  often related to command/query separation in the contract design.
- **Contract stability versus change rate** — backward-compatible
  extension strategies versus breaking changes; how compatibility is
  introduced and verified over time (see [interface
  evolution](interface-evolution.md)).

Non-technical forces also belong in the same trade-off write-up: client
diversity (unified good-enough API versus diverging per-client variants),
market dynamics (standardized interfaces for provider independence versus
proprietary lock-in), distribution fallacies (unreliable networks make QoS
guarantees hard), and the **illusion of control** — once data and behavior
are exposed, clients will use them in unexpected ways and control is hard
to regain.

[API architecturally significant
requirements](api-architecturally-significant-requirements.md) supply the
quality goals each dimension must satisfy; [pattern-language documentation
format](pattern-language-documentation-format.md) supplies named options
when a published pattern matches the force being resolved.
