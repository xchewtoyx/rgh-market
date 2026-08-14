---
type: concept
title: Scope of Work vs. Scope of Product
description: >
  The scope of the work is the whole business activity under study; the
  scope of the product is the specific portion of it that a new system
  will automate or support — and the boundary between them is a design
  decision made only after the work is understood.
sources:
  - title: Mastering the Requirements Process
    resource: "Mastering the Requirements Process: Getting Requirements Right (Suzanne Robertson, James Robertson), ch. 8"
---

The **scope of the work** is the whole business activity under study,
fixed at [project blastoff](project-blastoff.md) via the [context
diagram](context-diagram.md). The **scope of the product** is the
specific portion of that work a new software product will actually
automate or support — a strictly narrower boundary, drawn only once the
work itself is understood, not assumed up front.

Drawing the product boundary means deciding, for each [business use
case](business-event-and-use-case.md), how much of it becomes a **product
use case (PUC)**: the specific interaction between a human user (or
adjacent system) and the automated product. A single BUC often contains
several PUCs — a "de-ice road segment" business response might include a
PUC for configuring temperature thresholds and a separate PUC for
generating the truck route map, each independently scoped in or out of
the product.

Where to draw this boundary is itself a decision with real trade-offs:
formulating candidate product boundaries means considering multiple
architectures (fully automated vs. human-assisted workstation vs. mobile
interface), the impact on adjacent systems and human workflows the
boundary shift creates, and feasibility against technical, cost, and
schedule constraints. This is where requirements work and [architecture
decision-making](architectural-decision-capture.md) meet: the product
boundary is a requirements-scoping decision, but it has to be evaluated
using the same trade-off reasoning a design decision would get.
