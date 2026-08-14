---
type: concept
title: Documenting Trade-Offs
description: >
  Laying out the benefits, costs, and risks of each option considered —
  before committing to one — is what makes a design decision reviewable
  and its rationale reconstructable later.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 4, ch. 5, ch. 11"
  - title: The DevOps Handbook
    resource: "The DevOps Handbook, 2nd Edition (Kim, Humble, Debois, Willis, Forsgren), ch. 13"
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 23"
---

A trade-off write-up documents the options that were considered for a
design problem side by side, not just the one that was chosen. A useful
structure, illustrated by a worked example of choosing whether to use a
third-party payment processor instead of handling payment data in-house,
lists for each option: the benefits it offers, its direct costs, and the
risks it introduces — including risks a candidate mitigation for one
option would itself introduce (e.g., a local retry queue added to reduce
one dependency risk can reintroduce the sensitive-data-storage problem the
option was chosen to avoid in the first place). The same structure applies
to smaller design choices: comparing four ways to push a config file to a
fleet of servers by API surface, complexity, ability to scale, and ability
to express least privilege makes the reasoning behind picking one of them
inspectable later, instead of just asserted.

Trade-off tables are also useful for comparing architectural archetypes
directly — for example, monolith-v1 vs. monolith-v2 vs. microservices,
compared on scaling, coordination cost, and deployment granularity — as a
template for structuring the options section of a larger [architectural
decision record](architectural-decision-capture.md).

A trade-off is only worth documenting formally when the complexity it
weighs is [essential rather than accidental](essential-vs-accidental-complexity.md)
— i.e., when it traces back to an actual requirement or constraint, not to
an unexamined default. Recording the trade-off is also what lets a
build-vs-buy or make-vs-adopt decision be judged later against the
requirements that drove it — for example, a decision to build rather than
buy documented against specific, named problems with the available
off-the-shelf options — rather than only against whatever criteria seem
obvious in hindsight.

The same discipline works in reverse, to justify *undoing* an existing
design rather than choosing a new one: a refactoring proposal backed by
historical bug-fix and code-churn data attributable to specific
problem areas, projected forward against an estimated remediation
effort, turns "give us three months to refactor with no new features" —
a hard sell on its own — into a quantified return-on-investment case a
manager can actually evaluate. This is the same reasoning as
[change-mechanism investment
justification](change-mechanism-investment-justification.md) run against
historical data instead of a forward-looking estimate, and it's worth
recording the same way: the data source, the projected saving, and the
assumption that makes the projection conservative rather than optimistic.
