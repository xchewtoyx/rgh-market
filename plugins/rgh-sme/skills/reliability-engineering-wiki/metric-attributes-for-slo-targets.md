---
type: concept
title: Metric Attributes That Constrain SLO Targets
description: >
  A metric's resolution, event quantity, and quality all bound how tight an
  SLO target can realistically be before the measurement itself becomes the
  noise source.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 4"
---

Three attributes of the underlying metric constrain what target is actually
achievable, independent of how reliable the service really is:

- **Resolution** — how frequently the metric is sampled or reported. Coarse
  resolution means a single bad sample can instantly represent a large chunk
  of the error budget; mitigations include requiring consecutive bad samples
  before counting a "bad" event, or loosening the target to match achievable
  resolution.
- **Quantity** — low-event-volume services (e.g. an hourly batch job) see the
  measured percentage swing wildly from a single failure (1 failure/day on
  an hourly job = 95.83% that day). Mitigations: a larger time window, a
  looser target, or confidence-interval-based statistical treatment. See
  [low-traffic SLO alerting](low-traffic-slo-alerting.md) for the alerting-
  side version of this same problem.
- **Quality** — noisy or inaccurate underlying data may need sustained-
  duration thresholds (e.g. "bad" only if in violation for 5+ consecutive
  minutes) or percentage-of-samples-bad thresholds to filter false positives.

These attributes are a standard checkpoint when
[identifying a miscalibrated SLO](identifying-a-miscalibrated-slo.md): if the
target keeps tripping for reasons unrelated to real user pain, one of these
three is often the actual culprit rather than the target itself being wrong.
