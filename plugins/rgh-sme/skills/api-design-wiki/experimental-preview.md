---
type: concept
title: Experimental Preview
description: >
  A best-effort API or version released outside normal governance with no
  stability, functionality, or longevity commitments, to gather early feedback.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 8"
---

An **experimental preview** lets providers ship unstable APIs (or versions) in a
sandbox with expectations clearly set: functionality, stability, and support
are not guaranteed; the preview may vanish without notice or run only briefly.

Forces: early adopter feedback and revenue timing vs client aversion to wasted
investment and provider cost of full rigor on prototypes.

Often paired with [two in production](two-in-production.md) for the eventual
stable line. May omit [SLA](service-level-agreement-as-contract.md) but still
carry a draft [API description](api-description.md). [API keys](api-key-as-message-element.md)
can restrict access to a closed group.

Document stability state in the description (experimental, prerelease,
supported, deprecated, retired). Weakest commitment alongside
[aggressive obsolescence](aggressive-obsolescence.md).

[Operational data holders](operational-data-holder.md) often preview first;
[master data holders](master-data-holder.md) rarely do.
