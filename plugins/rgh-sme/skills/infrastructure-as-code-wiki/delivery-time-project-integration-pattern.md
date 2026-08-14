---
type: concept
title: "Pattern: Delivery-Time Project Integration"
description: Building and testing each dependent infrastructure project separately first, then combining tested versions of them at a dedicated integration stage in the pipeline, after which they progress together.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 19"
---

Delivery-time project integration builds and tests each project on its own first, and only combines specific versions of dependent projects at a dedicated *fan-in* (or project integration) stage partway through the [delivery pipeline](infrastructure-delivery-pipeline.md); once combined, those versions progress through the rest of delivery together. For example, a [stack](infrastructure-stack.md) that uses a [server image](server-image-as-code.md) is tested alone first, then integrated with the latest server image version that has already passed its own tests.

Testing each project separately before integration enforces real boundaries between them: if the stack's code accidentally reaches directly into a file that belongs to the image project, the isolated test stage fails immediately, exposing the coupling before it reaches integration — a useful forcing function that build-time integration's tighter coupling doesn't provide as cleanly.

Combined versions need to travel together through the rest of delivery, typically implemented either by bundling everything into a single artifact at the integration stage, or by producing a small descriptor file recording the specific version of each constituent project, which later stages read to know exactly which artifacts to pull. This pattern sits between [build-time](build-time-project-integration-pattern.md) (integrate first) and [apply-time project integration](apply-time-project-integration-pattern.md) (integrate every time, at the point of use) on the spectrum of when dependent projects get combined.
