---
type: concept
title: Offloading Sensitive Data
description: >
  The best mitigation for sensitive data is not holding it — but
  offloading to a third party spawns a cascade of reliability and security
  tradeoffs that must be walked deliberately.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 4"
---

# Offloading Sensitive Data

Often the best way to mitigate risk around sensitive data (payment
details, PII) is to *never hold it*: arrange for it not to pass through
your systems, or at least never persist it — e.g. integrate a third-party
payment provider. Benefits: a vulnerability in your systems can no longer
compromise data you don't have; compliance obligations (PCI DSS-style)
may simplify; you skip building data-at-rest protection; you inherit the
vendor's fraud countermeasures and expertise.

But the payment example is a masterclass in tradeoff cascades — worth
internalizing as a pattern for any
[security design review](security-design-review.md):

- **New dependency, new failure modes.** The purchase flow now fails when
  the provider is down. Mitigate with a second provider (two APIs, more
  cost, more attack surface) or a local queue buffering transactions
  during provider outages.
- **The mitigation reintroduces the original risk.** A reliable queue
  wants persistent disk — and now sensitive data is stored on your
  systems again (some payment data may never touch disk at all). And
  rarely exercised fallback subsystems harbor hidden bugs.
- **The fallback becomes an attack vector.** Consider an
  [insider](insider-risk.md) deliberately breaking the provider link to
  *activate* local queueing and then harvest the queue. A security risk,
  born from mitigating a reliability risk, born from mitigating a
  security risk.
- **Vendor integration is attack surface.** You're entrusting customer
  data to the vendor (their security stance must match yours, evaluated
  ongoing). A vendor-supplied linked library — or its transitive
  dependencies — can make *your* system vulnerable; mitigate by
  sandboxing, being able to update it fast, or preferring vendors exposing
  open protocols (REST/JSON, gRPC) over proprietary libraries. Client-side
  JavaScript integration runs with full privileges in your web origin —
  sandbox payment functionality in a separate origin/iframe (adding
  cross-origin complexity) or accept redirect-based UX.

The meta-lessons: nonfunctional requirements have far-reaching,
domain-crossing implications; every mitigation deserves its own threat
model; and sometimes the cleanest resolution is a product-level tradeoff
(an ad-funded model that removes payments entirely) rather than a
technical one.
