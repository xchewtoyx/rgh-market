---
type: concept
title: API Architecturally Significant Requirements
description: >
  API design is driven by architecturally significant requirements spanning
  developmental, operational, and managerial qualities — from understandability
  and coupling autonomy to security, data parsimony, and evolvability.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann, Stocker, Lübke, Zdun, Pautasso), ch. 1"
---

[Architecturally significant requirements](architecturally-significant-requirement.md)
for APIs fall into three categories that should be elicited and documented
before committing to a contract:

**Developmental qualities** — discoverable, learnable, understandable, and
easily consumable. Request and response structures should generally follow
the domain model without exposing it wholesale: hide as much implementation
detail as possible while still meeting client information needs. Separating
specification from realization takes deliberate effort; exposing whatever
already exists internally leaks detail and constrains future change. See
[developer experience as requirement](developer-experience-as-requirement.md)
for how these qualities surface in onboarding metrics.

**Operational qualities** — dependable runtime behavior: performance
(latency from network and marshalling is a client concern; throughput and
scalability under load are primarily provider concerns), reliability,
security, and privacy (access control, confidentiality, integrity,
auditability of API traffic).

**Managerial qualities** — evolvability and maintainability over the API's
lifetime, ideally both extensible and backward compatible so provider and
client teams can develop and deploy independently. [Interface
evolution](interface-evolution.md) practices resolve the stability-versus-
flexibility tension; market power sometimes lets the provider dictate the
rhythm, sometimes the client community does.

Cross-cutting ASRs that shape almost every API decision:

- **Coupling autonomy** — loose coupling has four dimensions worth
  documenting in [architectural decision
  records](architectural-decision-capture.md): reference autonomy
  (naming/addressing), platform autonomy (hiding technology choices), time
  autonomy (synchronous versus asynchronous interaction), and format
  autonomy (data contract design). Two APIs from the same provider should
  also avoid unnecessary hidden dependencies between them.
- **Data parsimony** — contracts tend to grow because adding fields is
  easier than removing them, and once added, unknown clients may depend on
  any field; managing optional variability explicitly is an ongoing
  documentation and governance obligation, not a one-time design choice.

These requirements conflict by nature — exposing data for client utility
versus hiding detail for provider freedom, rapid short-term integration
versus long-term independent evolution — which is why they belong in
[documenting trade-offs](documenting-trade-offs.md) alongside the chosen
[API visibility](api-visibility-decision.md) and [integration
type](api-integration-type-decision.md) decisions.
