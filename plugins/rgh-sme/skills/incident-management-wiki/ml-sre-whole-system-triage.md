---
type: concept
title: ML SRE Whole-System Triage Habit
description: The habit an ML production engineer needs during triage — assuming the fault lies outside the component where it manifests — because ML outages are seldom caused by the system or metric where they show up.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Cathy Chen, Niall Richard Murphy, Kranti Parisa, D. Sculley, Todd Underwood), ch. 11"
---

ML outages are seldom caused by the system or metric where they manifest:
poor revenue can trace back to missing data elsewhere in the pipeline,
serving crashes can trace back to a training-side configuration change or a
synchronization error, and impact can originate from the world itself
changing around the model rather than from any code change at all. This
means the first triage habit for an ML SRE or production engineer has to be
stepping back to look at the whole system rather than debugging forward from
the symptom — a different practice from the component-focused instinct most
production engineers bring from non-ML incidents, but a required one for ML
outages specifically. See [ML incident organizational
breadth](ml-incident-organizational-breadth.md) for why that "whole system"
can extend past engineering entirely.

The concrete diagnostic direction this implies: start troubleshooting from
the model's changed or wrong *output* and work backward toward a cause,
rather than starting by "just looking through the data" for something that
seems off. Given the volume of data involved, browsing for an anomaly
without a symptom to anchor the search is a fruitless search in practice —
letting the observed output discrepancy narrow the search space is what
makes tracing a fault back through several unrelated systems (a schema
change here, a stale checkpoint there) tractable at all.

This role should also expect to deal directly with product leaders and
business decision-makers during an incident, since ML outages rarely stay
within the technical team's boundary and usually touch sales or customer
satisfaction — extensive business-facing experience isn't typical for
production engineers, but the role adapts to it quickly once the incident
requires it. Otherwise, standard [incident command
system](incident-command-system.md) practice applies unchanged; most
production engineers are already competent at that part.

Post-incident, this role tends to accumulate a wide range of follow-up
ideas, from missing monitoring to full rearchitectures. The useful
prioritization move is sorting them along two axes — value and
cost/feasibility of implementation — favoring items that are both valuable
and easy, the same triage a well-formed [action item](action-item-quality.md)
needs to survive. Items that are "likely valuable but extremely difficult"
deserve a separate category, reviewed periodically with senior leads rather
than mixed into regular tactical work, since they will never win
prioritization against smaller items if left in the same queue.
