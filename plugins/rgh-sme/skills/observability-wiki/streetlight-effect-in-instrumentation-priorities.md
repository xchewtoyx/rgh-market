---
type: concept
title: The Streetlight Effect in Instrumentation Priorities
description: Teams tend to add more telemetry to the paths that are already well-instrumented and easy to measure, while the highest-value gaps are usually in paths nobody has ever instrumented at all — a pattern worth actively checking for rather than assuming existing coverage tracks actual diagnostic value.
sources:
  - title: "How to Measure Anything: Finding the Value of Intangibles in Business"
    resource: "How to Measure Anything (Douglas W. Hubbard), ch. 7"
---

Across many decision-analysis engagements, a consistent pattern emerges: the variables an organization has historically spent the most effort measuring turn out to have the *least* remaining value in resolving real uncertainty, while the highest-value unmeasured variables are ones that were never tracked at all — sometimes not even considered in the original decision framework. Two mechanisms drive this: people gravitate toward measuring what they already know how to measure (the "drunk looking for his lost wallet under the streetlight because the light is better there, not where he actually dropped it"), and anything already measured repeatedly has, almost by definition, already had much of its uncertainty resolved — so there's mechanically less value left to extract from measuring it more.

The same pattern shows up in instrumentation coverage. A service that's easy to instrument (a well-understood HTTP endpoint, a database query) tends to accumulate more and more telemetry over time — additional metrics, finer-grained spans, more log fields — while genuinely novel failure modes usually live in exactly the paths nobody thought to instrument: a rarely-exercised error branch, an upstream dependency's edge case, a background job with no dashboard at all. This is the instrumentation-side analog of [known-unknowns vs. unknown-unknowns](known-unknowns-vs-unknown-unknowns.md): heavily-instrumented paths are, definitionally, the ones already well understood, while the paths that would most help with a genuinely novel incident are the ones that got no instrumentation investment precisely because nobody anticipated needing it.

The practical corrective is the same move [closing telemetry gaps from past incidents](closing-telemetry-gaps-from-past-incidents.md) and a [telemetry premortem](telemetry-premortem.md) already prescribe, but applied as a standing question rather than only after a specific failure: periodically ask which parts of the system have received the least instrumentation attention, not which parts have the most dashboards — and treat "we've never needed to look at this before" as a reason to check it, not a reason to leave it alone.
