---
type: concept
title: Architecturally Significant API Requirements
description: >
  Quality goals — understandability, hiding, coupling autonomy, modifiability,
  performance, data parsimony, and security — that drive concrete API pattern choices.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 1"
---

**Architecturally significant requirements (ASRs)** for APIs group into
developmental, operational, and managerial qualities. They connect abstract goals to
pattern decisions across the bundle.

## Development qualities

- **Understandability** — request/response structure should follow the domain model
  without exposing it wholesale or copying internal schemas verbatim; hide what clients
  do not need ([information hiding in contracts](local-interface-to-remote-api.md)).
- **Information sharing versus hiding** — separating specification from realization
  takes effort; exposing internal structures leaks implementation and blocks change.
- **Coupling** — loose coupling sits between requirement and design. Four autonomy
  dimensions (Fehling et al.):
  1. **Reference autonomy** — naming and addressing independent of implementation
  2. **Platform autonomy** — technology choices hidden behind the contract
  3. **Time autonomy** — synchronous versus asynchronous interaction
  4. **Format autonomy** — data contract design; rightsizing exposed structures
     Two APIs from the same provider should avoid unnecessary hidden dependencies.

## Operational qualities

- **Performance and scalability** — **latency** (network, marshalling) primarily
  concerns clients; **throughput and scale** (response times under load) primarily
  concerns providers.
- **Data parsimony** ("Datensparsamkeit") — prefer minimal fields; adding is easy,
  removing is hard because unknown clients may depend on unused attributes. Contracts
  tend to grow unless variability is managed ([field masks](field-mask.md), careful
  additive evolution).
- **Security and privacy** — access control, confidentiality, integrity, and
  auditability of API traffic ([request authentication requirements](request-authentication-requirements.md),
  [API key as message element](api-key-as-message-element.md)).

## Managerial qualities

- **Modifiability** — maintainability including [backward compatibility policy](backward-compatibility-policy.md)
  for parallel client/server deployment.
- **Evolvability** — balance agility and stability via versioning and deprecation
  patterns.

Summary framing used in the pattern language: (1) **development** — discoverable,
learnable, consumable ([developer experience](developer-experience.md)); (2)
**operational** — dependable performance, reliability, security, runtime manageability;
(3) **managerial** — evolvable and maintainable, ideally extensible **and**
backward compatible.

[Good API design qualities](good-api-design-qualities.md) (operational, expressive,
simple, predictable) offer a complementary contract-level checklist from another
source text.
