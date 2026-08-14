---
type: concept
title: Endpoint Operation Design Challenges
description: >
  Competing forces — accuracy, autonomy, scale, consistency, idempotence, and
  auditability — that shape endpoint granularity and operation responsibility choices.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 5"
---

Endpoint placement and operation design sit in the Define phase of API work —
alongside message structure (Chapter 4). Poor positioning yields unscalable
providers and mishmash client experiences. Business ideation produces candidate
endpoints; designers balance **granularity** (small specific vs large universal)
against **coupling** (as low as possible, as high as needed). See [API design recurring trade-offs](api-design-recurring-trade-offs.md)
for the full set of recurring contract dimensions.

Two classifying questions drive the pattern map:

- **Endpoint role** — activity-oriented [processing resource](processing-resource.md)
  versus data-oriented [information holder resource](information-holder-resource.md)
  (with operational, master, reference, transfer, and link-lookup specializations).
- **Operation responsibility** — read/write profile via [operation responsibility patterns](operation-responsibility-patterns.md).

## Conflicting qualities

- **Accuracy** — implementation matches contract; preconditions, invariants, and
  postconditions in the [API description](api-description.md) set mutual expectations.
- **Autonomy versus coordination** — fine-grained endpoints rewrite independently
  but multiply integration, consistency, and compliance testing cost.
- **Scale and availability** — [service level agreement as contract](service-level-agreement-as-contract.md)
  targets may be unrealistic as 24/7; weakest link bounds end-to-end reliability;
  compensating operations need clear architecture.
- **Manageability** — runtime FCAPS monitoring validates design assumptions.
- **Consistency and atomicity** — business activities all-or-nothing; failures
  need explicit abort or compensation to valid state.
- **Idempotence** — repeated calls with same input yield same output and state
  effect; supports safe retry ([request deduplication and idempotency keys](request-deduplication-and-idempotency-keys.md),
  [standard method contract](standard-method-contract.md)).
- **Auditability** — tamper-evident logs for regulated processes.

Richer contracts cost learning and test effort; exposing a shared database via
stored procedures couples clients to one failure domain and blocks independent
deployment — valid only with eyes open to scale and responsibility violations.

Operation granularity trade-off: many small [computation functions](computation-function.md)
and retrievals compose flexibly but need orchestration; few large operations are
self-contained but heavy to configure and evolve.
