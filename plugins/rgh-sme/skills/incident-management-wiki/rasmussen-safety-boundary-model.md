---
type: concept
title: Rasmussen's Safety Boundary Model
description: Jens Rasmussen's model of a system operating within three invisible boundaries — acceptable performance, economic failure, and unacceptable workload — that organizational pressure constantly pushes it toward.
sources:
  - title: "Observability Engineering"
    resource: "Observability Engineering, 2nd Edition (Charity Majors, Liz Fong-Jones, George Miranda), ch. 22"
---

Jens Rasmussen modeled every sociotechnical system as operating within three invisible boundaries:

- **The boundary of acceptable performance**: cross it and customers (or users) start to suffer.
- **The boundary of economic failure**: cross it and the business's profitability breaks.
- **The boundary of unacceptable workload**: cross it and the team responsible burns out or can no longer keep up.

Constant organizational, financial, and efficiency pressure pushes the system's actual operating point toward these boundaries over time — nobody deliberately decides to become unsafe or unprofitable, but everyday local optimizations (shipping capability faster, cutting cost, tolerating higher on-call load) each nudge the operating point a little closer to one boundary or another. This is the same underlying dynamic as [practical drift](practical-drift.md): drift is not a series of bad decisions but the accumulation of many individually reasonable ones, in the absence of a countervailing pressure pulling back toward the center.

The model's operational claim is that these boundaries are usually invisible until they're crossed — a team can be drifting toward burnout or toward a latent reliability failure for a long time with no single metric flagging it, because no individual local decision looks unsafe in isolation. Making the boundaries visible in real time (a customer-experience signal, a cost-per-unit-of-work signal, a team-load signal, tracked continuously rather than inferred after the fact) is what lets an organization correct course before crossing one, rather than discovering the boundary only in the incident that resulted from crossing it. This generalizes [chronic unease](chronic-unease.md) from an individual disposition into an organizational design requirement: something has to keep the distance-to-boundary visible, or drift proceeds unchecked.
