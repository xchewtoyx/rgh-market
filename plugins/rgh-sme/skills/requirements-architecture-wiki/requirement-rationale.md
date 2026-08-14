---
type: concept
title: Requirement Rationale
description: >
  Recording why a requirement exists — not just what it says — lets
  developers make sound trade-offs later and forces stakeholders to
  justify a requirement's business value before it is accepted.
sources:
  - title: Mastering the Requirements Process
    resource: "Mastering the Requirements Process: Getting Requirements Right (Suzanne Robertson, James Robertson), ch. 12"
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 7"
---

Rationale is a statement of *why* a requirement is necessary for the
business, distinct from the requirement's description of what is needed
and its [fit criterion](fit-criterion.md) for how it's verified. Two
things make rationale worth capturing as a mandatory field rather than
optional color: it gives developers the context to make good trade-offs
when implementation constraints force a choice the original requirement
didn't anticipate, and it forces whoever is asking for a requirement to
articulate its business value — which is often enough on its own to
surface "gold plating," a requirement that exists because someone wanted
it, not because the business needs it.

Rationale capture matters even more, not less, once a system is changing:
documenting the "how" and "why" of a change — the requirements driving it,
lessons learned from any proof of concept, and the reasoning behind
specific decisions — is what lets that reasoning be reevaluated later if
plans need to change, rather than being lost the moment the person who
made the call moves to something else. For long-running, multi-year change
efforts specifically, this rationale needs to be kept current as a single
source of truth, not scattered across meeting notes, since the people
who made the original decisions are the ones most likely to have left by
the time it matters again.

See [architectural decision capture](architectural-decision-capture.md)
for the equivalent practice applied to a *design* decision rather than a
requirement — the two are distinct per [requirement vs. design
decision](requirement-vs-design-decision.md), but both exist to answer the
same underlying question later: why is this here?
