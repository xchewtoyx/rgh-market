---
type: concept
title: ML SLO Separation of Concerns
description: >
  Defining SLOs for an ML-enhanced system is easier to reason about split
  along three independent axes — which layer, which signal family, and
  whether the target actually reaches business outcome — rather than as one
  undifferentiated set of targets.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 1"
---

Specifying SLOs for an ML system is harder than for a plain request/response
service, because subtle shifts in the input data or the world it describes
can degrade quality without any conventional error appearing. Three
separations of concern make the target-setting problem more tractable:

1. **Which layer** — serving, training, or the application built on top of
   the model, each of which needs its own SLO vocabulary. Serving looks like
   an ordinary service (error rates, latency). Training looks like a
   [pipeline](pipeline-sli-types.md) with its own throughput and completion
   targets (e.g. "95% of training runs finish within N seconds" — a
   [freshness](pipeline-sli-types.md)-style deadline SLO, see
   [catch-up-time deadline alerting](catch-up-time-deadline-alerting.md) for
   how to alert on one without noise). The application layer is closer to a
   product metric than a systems one — e.g. the count of recommendations
   actually shown, or the rate of successful calls to the model server as
   observed by the calling application, which can differ from the model
   server's own reported error rate because the two are measured from
   different vantage points.
2. **Which signal family** — the traditional [golden four
   signals](sli-types-by-service-category.md) (latency, traffic, errors,
   saturation) still apply to the serving layer, but they sit alongside a
   distinct family of ML-operations-internal signals (training throughput,
   completion rate, confidence/quality thresholds — see
   [ML prediction confidence as SLI](ml-prediction-confidence-as-sli.md))
   that are less generic than the golden four but not fully bespoke either.
3. **Whether the target reaches business outcome** — none of the above,
   even taken together, actually measures ML *performance* in the sense that
   matters: for that, an SLO has to tie to the business purpose the model
   serves (e.g. click-through rate on model-generated suggestions, or an
   end-to-end revenue-attributable-to-model figure, possibly sliced by
   geography or customer segment), often necessarily measured over a longer
   window than a serving-layer SLO would use. See
   [ML SLOs scoped to business outcome](ml-slo-scoped-to-business-outcome.md)
   for why this layer is the one that should anchor the others rather than
   standing as just one more item in the set.

Treating these as three separate axes — rather than one flat SLO list —
keeps a serving-layer error-rate miss from being confused with an
application-layer business-outcome miss, which typically need different
people and different fixes.
