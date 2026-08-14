---
type: concept
title: Measurement Inversion for Reliability Investment
description: >
  The reliability signals worth building are usually not the ones already
  heavily instrumented, because a variable's economic value of measurement
  runs inversely to how much measurement attention it already receives.
sources:
  - title: "How to Measure Anything: Finding the Value of Intangibles in Business"
    resource: "How to Measure Anything, 3rd Edition (Hubbard), ch. 7"
---

Instrumentation effort tends to concentrate on whatever is already easy to
measure — the metrics a team already knows how to collect, or that a
previous team happened to wire up — rather than on whatever would actually
change a decision. This produces a predictable pattern across many
organizations' reliability programs, generalized as the **Measurement
Inversion**: a variable's economic value of measurement is usually
*inversely* proportional to how much measurement attention it typically
receives. The highest-value gaps are routinely things nobody has ever
instrumented at all (e.g. how often a specific failure mode actually
degrades a critical user journey, or how a soft dependency's slow-but-not-
failing responses erode a downstream SLO); the metrics a team has dashboarded
for years usually carry low or near-zero further value, because their
uncertainty was already mostly resolved by the act of measuring them
repeatedly.

**Practical filter for reliability work**: before adding a new SLI, alert, or
monitoring dimension, ask what decision it would actually change — whether
to invest in hardening a dependency, which [critical user
journey](critical-user-journey.md) needs a new SLO, whether a service is
[hard or soft](hard-vs-soft-dependency.md). A signal that can't move a
decision either way has close to zero value no matter how cheap it is to
collect, and effort spent refining an already-well-understood metric is
usually better redirected toward a genuinely unmeasured risk. This is the
same filter that should drive [SLO-driven risk
prioritization](slo-driven-risk-prioritization.md) and [error-budget-driven
prioritization](error-budget-driven-prioritization.md): rank candidate
measurement or mitigation work by how much it would change what the team
does next, not by how familiar or easy the metric is to build.

**Why the inversion happens**: teams measure what their existing tooling
already makes easy (survey a user, mine existing logs) regardless of whether
that's where the real uncertainty lives; and a metric that's already been
tracked for years has, by virtue of that history, had much of its
uncertainty already resolved — so further investment in it has diminishing
returns compared to a genuinely unknown risk. A large one-time monitoring
buildout is not automatically higher-value than a small, targeted one; size
of effort and value of the resulting decision are not the same axis.
