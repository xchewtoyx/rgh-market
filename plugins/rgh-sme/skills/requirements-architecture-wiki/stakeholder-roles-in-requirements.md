---
type: concept
title: Stakeholder Roles in Requirements
description: >
  Requirements stakeholders play distinct roles — client, customer,
  hands-on user, subject-matter expert, negative stakeholder — each with
  a different vested interest that shapes what they can reliably tell you.
sources:
  - title: Mastering the Requirements Process
    resource: "Mastering the Requirements Process: Getting Requirements Right (Suzanne Robertson, James Robertson), ch. 3, Appendix B"
---

Requirements stakeholders are not interchangeable, and the role someone
plays determines what kind of information they can reliably give you.
Volere distinguishes: the **client** (pays for the development, cares
about cost and business outcome), the **customer** (buys the product,
which is not always the same person as the client), **hands-on users**
(the direct operators of the finished product, who know the actual
day-to-day work — see [trawling techniques](requirements-elicitation-techniques.md)),
**subject-matter experts** (business experts who can explain the rules and
policy behind the work, as distinct from how it's currently executed —
see [essence of the business work](essence-of-the-business-work.md)), and
**negative stakeholders** (people negatively affected by or opposed to the
project, whose objections are still a legitimate source of requirements
and risk, not noise to be filtered out).

For each stakeholder, record their vested interest (what they gain or
lose from success or failure), their degree of influence over project
decisions, their domain expertise, their availability for elicitation
work, and their stance (champion, neutral, resistant, adversary). This
isn't bureaucratic overhead — a requirement sourced from someone with high
influence and a resistant stance needs different handling in the [quality
gateway](quality-gateway.md) than one sourced from an enthusiastic
hands-on user, and knowing which is which up front avoids later disputes
about whether a requirement was ever actually validated by someone with
standing to validate it.

A complementary, coarser classification sorts stakeholders by their
*distance* from the system rather than by role: **first-degree**
stakeholders directly use the system; **second-degree** stakeholders work
with the output of those first-degree users without touching the system
themselves; **third-degree** stakeholders install, deploy, or support it.
This distance-based view is useful precisely where the role-based Volere
list gets ambiguous — a "hands-on user" and a "negative stakeholder" can
both be first-degree, and knowing that tells you they need to be
reconciled directly rather than one deprioritized on the other's behalf.
