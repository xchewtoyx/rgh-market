---
type: concept
title: Subversive Investments in Slack
description: >
  Sharp-end practitioners quietly withhold resources from management's
  view specifically to preserve reserve capacity for sudden demand surges,
  compensating for margin that top-down efficiency drives keep consuming.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 7"
---

Where management pursues "good leadership" through efficiency drives, those
drives consume exactly the buffers and reserve capacity a resilient
operation depends on — a direct application of [the law of stretched
systems](law-of-stretched-systems.md) at the point where management action
is what does the stretching. Sharp-end practitioners routinely compensate by
hiding resources from management's own visibility: a spare part kept off the
books, staff time not logged as fully committed, informal stock that would
show up as "waste" on an efficiency audit. These are **subversive
investments in slack** — subversive because they only work by staying
invisible to the same efficiency drive that would eliminate them the moment
they were reported, and slack in the ordinary [buffering
capacity](buffering-margin-and-tolerance.md) sense.

This produces a genuine, structural tension in how resilience should be
managed. Individual, local sharp-end adaptation (hoarding a bit of reserve
capacity here) and system-level resilience (the large-scale, distributed
pattern those individual hoards add up to) are not automatically the same
thing and can even work against each other — see [working at
cross-purposes](working-at-cross-purposes.md) — but in this specific case
the local adaptation is quietly *substituting for* organisational margin
management that management's own efficiency drive has undermined.
Eliminating the hiding (through more thorough audits, tighter resource
tracking) without first fixing the efficiency pressure that made hiding
necessary removes the compensation and leaves the underlying margin
shortfall exposed — a live example of [the substitution
myth](dynamic-stability-and-damping.md): the audit's designers assumed it
would only remove waste, not that it would also remove the informal buffer
the system had been quietly running on.
