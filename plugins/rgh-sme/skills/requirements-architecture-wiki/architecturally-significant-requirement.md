---
type: concept
title: Architecturally Significant Requirement
description: >
  A requirement is architecturally significant when it would produce a
  meaningfully different design if changed and it carries enough business
  value to be worth trading other requirements off against.
sources:
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 19"
---

An architecturally significant requirement (ASR) is a requirement that
satisfies two conditions at once: it has a profound effect on the
architecture — the design would plausibly look meaningfully different
without it — and it carries high enough business or mission value that it
is worth potentially trading other requirements off against. ASRs are
often, but not always, [quality attribute
scenarios](quality-attribute-scenario.md): every [tactic or
pattern](architectural-tactic.md) choice is a response to some quality
attribute requirement, and the harder or more important that requirement,
the more likely it qualifies as an ASR.

ASRs rarely arrive pre-labeled. Most requirements documents shape
architecture the least where they're most complete (functional behavior)
and shape it the most where they're weakest or silent (quality attributes,
business goals, developmental constraints) — a requirements document
written for an acquirer's interests, or one still incomplete when
architecture work has to start, is a source to mine, not a source to wait
for. An architect gathers ASRs from at least four kinds of source, and
credible practice draws on more than one:

- **Requirements documents**, mined by category (usage, timing, external
  elements, networking, orchestration, security, data, resources, project
  management, hardware, flexibility, named technologies) even when nothing
  is explicitly labeled an ASR — and specifically asking, for each
  category, what's likely to change over the system's life, since
  anticipated evolution is itself architecturally significant whether or
  not it appears as a stated requirement.
- **Stakeholder interviews and workshops** — see [Quality Attribute
  Workshop](quality-attribute-workshop.md). Stakeholders frequently don't
  know their own quality-attribute requirements in advance; the architect
  is expected to help set them collaboratively, not just transcribe them,
  bringing comparative judgment about what similar systems have achieved
  and what a given target actually costs.
- **Business goal analysis** — see [business-goal-driven
  requirements](business-goal-driven-requirements.md). Some
  architecturally consequential decisions trace to a business goal with no
  quality-attribute requirement in between at all (a manager insisting on
  a piece of architecture for organizational reasons no specification
  would ever capture) — omitting it is just as much a failure as missing a
  stated requirement.
- **An architect-authored [utility tree](utility-tree.md)**, when none of
  the above sources are available and the architect has to construct
  candidate ASRs unilaterally as a starting point for validation.

Requirements keep changing after they're gathered — "walking on water and
developing software from a specification are both easy if both are
frozen" — so ASR-gathering is a channel to keep open with stakeholders
throughout the project, not a one-time inception activity. Getting ahead
of a rumored ASR change with cheap exploratory design, and reporting back
early if it turns out prohibitively expensive (ideally with a nearly-as-
good, cheaper alternative already in hand), is itself high-value work.
