---
type: concept
title: Goal, Process, and Action Rules
description: >
  Organisational rules operate at three distinct specification levels — goal,
  process, and action — and a gap at the goal level forces frontline
  operators to improvise the strategic judgement no one above them supplied.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 12"
---

Rules coordinate a high-risk operation across three specification levels
(Hale & Swuste, 1998), each answering a different question:

1. **Goal rules** — strategic directives that establish overall priorities
   and the principle for resolving trade-offs (e.g. "safety takes priority
   over schedule when the two conflict, and here is what that means
   concretely in this operation").
2. **Process rules** — tactical guidance specifying workflow structure and
   decision pathways: which options exist, in what order, under which
   conditions.
3. **Action rules** — the detailed operational procedures governing specific
   tasks, the level most written procedures actually operate at.

The three levels are meant to nest: action rules should be a concrete
instantiation of process rules, which should in turn instantiate a clear
goal rule. When an organisation fails to formulate clear, authoritative goal
rules — leaving priorities implicit or contradictory — the failure does not
stay contained at the top. Frontline operators still have to act, so they
improvise ad hoc action rules without the strategic backing a goal rule
would have given them. This simultaneously weakens [downward
resilience](upward-and-downward-resilience.md) (there is no clear intent
being communicated down) and over-burdens upward resilience (the sharp end
is now solving a strategic problem with only local, tactical information).

This is a sharper diagnosis of a familiar symptom: what shows up as
[procedural drift](procedural-drift.md) or excessive [safety
clutter](safety-clutter.md) at the action-rule level often has its actual
cause one or two levels up, in a goal rule that was never made explicit. The
fix implied by this model is not to write a better action-level procedure —
[the fallacy of the quick fix](fallacy-of-the-quick-fix.md) again — but to
supply the missing goal rule the action rules were quietly compensating for.

**A four-year empirical study of Norwegian civil aviation shows a missing
goal rule at the very top of a regulatory hierarchy**, not just inside one
operational unit. The Ministry of Transport mandated the national aviation
authority to ensure aviation is simultaneously "safe" and
"community-serving" — the latter meaning sustaining Norway's network of 46
regional short-runway airports for regional employment and access — without
ever specifying which goal wins when the two conflict, or how much. Because
short political coalition cycles (roughly four years) drove frequent policy
reversals on regional-airport retention, and the underlying aviation act
functioned only as a delegation act with no explicit trade-off rule,
individual regulators were left negotiating the safety/accessibility
trade-off ad hoc, case by case, every time a rule-exemption request came up
— a goal-rule vacuum reproduced at every point in the hierarchy below it,
exactly as this model predicts, all the way down to the [ad-hoc action
rules operators improvised at the sharp
end](upward-and-downward-resilience.md) to compensate for it.

The same three levels also describe how a single response should shift
*during* an unfolding event: see [matching response abstraction to
uncertainty](matching-response-abstraction-to-uncertainty.md).
