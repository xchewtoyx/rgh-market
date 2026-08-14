---
type: concept
title: Micro-Survey Factors Diverge from Macro Resilience Cornerstones
description: >
  A self-report survey administered to one operational function measures
  that function's individual operational capabilities, not the system-level
  anticipation/monitoring/response/learning cornerstones — because those
  cornerstones depend on cross-functional feedback loops no single survey
  population can see or report on.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 11"
---

A large empirical attempt to measure organisational resilience directly —
a 22-item survey administered to ~100 UK rail infrastructure planners,
factor-analysed and then named by a Delphi panel of domain experts —
produced five components (adaptability/flexibility, control,
awareness/preparedness, trade-offs, time management) that **did not map
onto [the four abilities of resilient performance](four-abilities-of-resilient-performance.md)**
(anticipation, monitoring, response, learning) the survey was designed
around. This divergence is not a methodological failure to fix with a
better instrument — it reveals something structural about what a survey
confined to one function can and cannot measure.

**Why the mismatch is structural, not a measurement bug:**

- **Cross-system boundary dependencies.** The macro cornerstones most
  dependent on information from *outside* the surveyed population — [Wald's
  bomber-paradox](walds-bomber-paradox.md)-adjacent "knowing what has
  happened" (learning) and "knowing what to expect" (anticipating) — rely on
  organisational feedback loops that span multiple departments. A survey
  confined to planners cannot see, let alone report on, mechanisms that live
  in the handoffs between planning and the departments planning depends on.
- **Operational vs systemic framing.** For a survey instrument to have
  face validity and produce a reliable response, its items have to be
  grounded in the respondent's own concrete daily tasks — "do I have enough
  time to plan thoroughly," not "is the organisation resilient." That
  grounding requirement itself forces the resulting factor structure toward
  micro-level operational capability, regardless of what macro property the
  designers intended to capture.

**The reframe: what a survey like this actually measures is the
micro-foundations of the macro cornerstones, not the cornerstones
themselves.** Individual planners' flexibility, sense of control, and
trade-off skill are the operational substrate the system-level abilities
are built out of — without adequate time management and managerial
feedback, no individual planner can exercise the trade-off judgement or
adapt to the unexpected event the macro cornerstones name at a higher level
of abstraction. This is the same [level-relativity leading and lagging
indicators](leading-vs-lagging-indicators-are-level-relative.md) already
show for individual metrics, generalised to entire measurement instruments:
a well-designed instrument correctly measures *something real*, but which
level of the system it is actually measuring is a separate question from
which level its designers were aiming at, and answering that question
requires knowing the instrument's population and its methodological
grounding, not just reading its item content.

**The practical implication for choosing a resilience-measurement
instrument**: a survey confined to one function is not a flawed proxy for
system-level resilience that a bigger sample would fix — it is a correct,
useful instrument for a *different*, narrower question (the operational
health of that function specifically), and treating its output as a
system-level resilience score will misread what it actually says. Used
honestly, periodic administration of such a survey is still a genuinely
useful quantitative index for monitoring regional or functional variance
over time — just not a stand-alone measure of total system resilience,
which requires deliberately integrating it with historical performance data
and instruments aimed at the cross-functional cornerstones a single-
function survey cannot reach.
