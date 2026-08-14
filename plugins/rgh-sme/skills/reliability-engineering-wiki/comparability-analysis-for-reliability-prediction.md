---
type: concept
title: Comparability Analysis for Reliability Prediction
description: >
  Predicting a new system's reliability by finding the closest existing
  analogous system, adjusting its real reliability data for known
  differences, and making that adjustment rationale explicit and revisable.
sources:
  - title: "Sources of Power: How People Make Decisions"
    resource: "Sources of Power: How People Make Decisions (Gary Klein), ch. 12"
---

When a new service or component has no operational history of its own,
[choosing SLO targets from historical data](choosing-slo-targets-from-historical-data.md)
has nothing to read from and
[calibrated estimation](calibrated-estimation-for-slo-targets.md) may still
feel unmoored without a concrete data anchor. **Comparability analysis** is
a middle path: find the closest existing system with real operational
reliability data, and explicitly adjust that data for the known differences
between it and the new system, rather than estimating from scratch or
guessing blind.

The method (developed for predicting aircraft-part failure rates before the
aircraft existed, but general): (1) state the specific reliability question
precisely; (2) identify the closest comparable existing system with actual
operational data; (3) write down *why* that system was chosen as the
analogue; (4) gather its real reliability data; (5) adjust the data for
known differences between the two systems; (6) write down the rationale for
each adjustment; (7) present the resulting prediction alongside its
rationale so others can inspect and contest it.

**Two kinds of difference require two different kinds of adjustment.** A
difference that is a matter of degree on a single known variable — a
higher-pressure hydraulic system, a larger physical scale — can usually be
handled with a proportional numeric adjustment (e.g., "runs at 33% higher
pressure, so cut reliability by a third"), and reasonable people can dispute
the exact factor while still agreeing on the method. A difference in
*usage pattern* or operating conditions — the same hardware used in a
cold-start-under-fire regime versus a steady smooth one — often cannot be
captured as a clean scaling factor at all, and the honest response is to
**reject the analogue entirely** even when the underlying hardware is
identical, rather than force an unjustifiable adjustment number onto it.
Comparability analysis's real discipline is recognizing which kind of
difference you're facing, not just producing a number either way.

**This is not free of judgment, and it degrades when the underlying data is
weak.** In a real accuracy check against aircraft reliability outcomes,
comparability-analysis predictions correlated strongly with actual results
when engineers had solid underlying data to adjust from, but accuracy
dropped sharply for a dimension where engineers lacked real data and had to
fabricate their own baseline — the technique amplifies good underlying data
but cannot manufacture data that isn't there. Comparability analysis also
depends on picking the analogue for genuinely *causal* similarity — the
same operating stresses, the same failure mechanisms — not superficial
resemblance; a mismatched analogue (identical hardware used in a
categorically different way, or a coincidentally similar-looking but
causally unrelated system) will confidently produce a wrong number. This is
the same failure mode
[dependency reliability composition](dependency-reliability-composition.md)
warns about with the shared-fate/independence assumption: the technique
only works when the analogue's causal structure genuinely transfers, and
writing the rationale down explicitly (step 3 and step 6 above) is what
lets someone else catch it when it doesn't.
