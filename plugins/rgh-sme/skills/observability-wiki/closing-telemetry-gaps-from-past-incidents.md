---
type: concept
title: Closing Telemetry Gaps from Past Incidents
description: After every incident, ask what indicator — however weak — would have predicted it earlier, and add that as new instrumentation; repeating this on ever-weaker leading signals catches problems earlier in their lifecycle over time.
sources:
  - title: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations"
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 14, 15"
  - title: "The Site Reliability Workbook"
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 4, 10"
---

A practical exercise: review recent (e.g. 30-day) severe incidents and, for each, ask what telemetry — even a weak, indirect signal — would have given advance warning. For a worked example (a web server that stopped responding), leading indicators existed across every layer: application (page load times creeping up), OS (free memory or disk space trending down), database (transaction times rising), network (functioning servers behind a load balancer silently dropping out). Add whichever of these weren't already instrumented.

The ideal end state, per Tom Limoncelli, is to delete all current alerts, then after each user-visible outage ask what indicator would have predicted it and add only that — repeating until the alert set consists entirely of things that prevent outages, rather than things that fire after one has already happened.

This is the same underlying discipline as identifying missing telemetry after an incident, or during peer review before a change ships, rather than waiting for the next occurrence of the same failure mode to expose the same gap — see [telemetry definition and scope](telemetry-definition-and-scope.md) for the five layers to check when doing this review, and [runbooks: value and limits](runbooks-value-and-limits.md) for a related caution about over-investing in codifying *responses* versus improving the underlying *signal*. [Chaos engineering](chaos-engineering-as-observability-stress-test.md) is the proactive, real-fault counterpart to this reactive review, and a [telemetry premortem](telemetry-premortem.md) is a cheaper, purely-imagined version of the same proactive check — both find the gap before a real incident does.

## Postmortem Culture and Telemetry Feedback Loops

A mature [postmortem culture](actionable-paging-hygiene.md) treats every operational incident as a feedback loop for telemetry systems. The Site Reliability Workbook prescribes a formal postmortem process designed to catch these gaps:

1. **The Diagnostic Question**: For every incident, the postmortem authors must ask: *“What metric, log, trace, or dashboard would have made our diagnosis faster?”*
2. **Actionable Tracking**: Every identified telemetry gap must be captured as a concrete, tracked bug or ticket with a single accountable owner, a priority rating, and a *verifiable end state* (e.g., “instrument query-execution latency on client X,” rather than a vague “improve database metrics”).
3. **Closing the Loop**: As Google SRE lead Ben Treynor Sloss notes, *“a postmortem without subsequent action is indistinguishable from no postmortem.”* Unresolved telemetry-gap tickets must be closed out with the same urgency as the code fixes for the incident itself, preventing recurrence of the same blind spot.
