---
type: concept
title: Utility Tree
description: >
  A utility tree decomposes overall system "goodness" into quality
  attributes, then system-specific refinements, then concrete scenarios
  scored by business value and technical risk — a way to construct
  candidate architecturally significant requirements when no stakeholder
  workshop is available.
sources:
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 19"
  - title: How to Measure Anything
    resource: "How to Measure Anything: Finding the Value of Intangibles in Business (Douglas W. Hubbard), ch. 6"
---

A utility tree is a top-down structure an architect can build alone when
stakeholder workshops or a usable requirements document aren't available:
the root is "Utility" (the system's overall goodness), branching into the
major quality attributes the system must exhibit, each quality attribute
branching into system-specific **refinements** (for performance, that
might be "data latency" and "transaction throughput," or "user wait time"
and "page-refresh time" — chosen for relevance to this system, not copied
from a generic list), and each refinement's leaves being concrete
[quality attribute scenarios](quality-attribute-scenario.md) — the actual
candidate [architecturally significant
requirements](architecturally-significant-requirement.md).

Each leaf scenario is scored on two independent axes, each high/medium/low:
**business value** (high = the project fails without it, low = nice to
have) and **technical risk** (high = a real source of concern about
achievability, low = confident it's achievable). The two scores are
deliberately kept separate rather than combined into one priority number,
because they answer different questions: value says whether it matters,
risk says whether it's hard.

The tree earns its keep through two checks that fall out of it almost for
free. First, a refinement with no recorded scenario is not automatically a
gap — it's a prompt to go check whether a real, unrecorded scenario is
hiding there. Second, scenarios scoring high on both axes are "the most
significant of the significant requirements" and deserve the most
architectural attention; if a large number of scenarios land in that
high/high cell, that itself is a warning sign worth raising about whether
the system as scoped is achievable at all, independent of any individual
scenario's content.

A utility tree is a stand-in for direct stakeholder input, not a
replacement for it — it produces a candidate ASR set for validation, the
same way any other elicitation source does, and should still be checked
against the people who actually hold the business value and risk
judgments wherever that's possible.

The H/M/L scoring is a deliberately lightweight triage device, not a rigorous
risk analysis: ordinal labels like "high" and "medium" are ambiguous
(does "high" mean 5% chance of a $5M loss, or 50% chance of a $500K
loss?) and cannot be compared arithmetically or fed into a real
cost/benefit calculation. That trade-off is appropriate for triaging which
architecturally significant requirements deserve deeper attention, but if
a specific (H,H) scenario turns out to justify a large investment decision
on its own, that decision deserves an actual quantified estimate — ranges
and probabilities, not another coat of "high" — before money is committed
on the strength of it.
