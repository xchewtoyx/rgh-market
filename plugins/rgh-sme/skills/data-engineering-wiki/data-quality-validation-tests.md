---
type: concept
title: Data Quality Validation Tests (Binary vs. Statistical)
description: >
  The two styles of validation gate a pipeline can run — simple binary rule
  checks and distributional/statistical checks — and why the second is
  needed to catch subtler regressions the first can't see.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 7"
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 15"
---

Most traditional data tests are binary logic: is a non-nullable field
unexpectedly null? Did a new, unrecognized categorical value show up? These
checks are cheap to write and catch a real class of problems, but they're
blind to a more dangerous class: quiet, gradual, or partial distortions that
never violate a simple rule. A shift in search-term statistics, for example,
could be genuine customer behavior, an undetected bot-traffic spike, or an
unrelated experiment someone else deployed — a binary null-check sees none
of these, because every value involved is individually well-formed.

**Statistical data testing** — checking whether a dataset's distribution,
volume, or other aggregate properties have shifted outside an expected
range, not just whether individual fields are populated and typed correctly
— is what catches this second class. It's the pipeline analogue of noticing
that something is *off* in aggregate even though no single row is
obviously broken.

The two styles are complementary, not substitutes: binary checks are cheap
validation gates worth running on every load, while statistical checks catch
the [data quality](data-quality-dimensions.md) failures — usually accuracy or
completeness failures that don't manifest as a missing or malformed field —
that binary checks structurally cannot see. A concrete example: a boolean
label field that's [defaulted to a plausible value pending later
confirmation](default-value-masks-missing-data.md) stays well-formed even
when the confirming feed stops working entirely, so the only thing that
actually catches the resulting outage is a statistical check on the label's
positive rate — e.g., alerting when a held-out sample's ratio of positive
labels falls well outside its normal historical range. A pipeline that only implements
binary checks has validation gates in name but is still exposed to the
"silent killer" failure mode where bad data drives decisions for months
before anyone notices.

**Validation also needs to run end-to-end, not only per stage.** A
multi-stage pipeline where every individual stage passes its own local
checks can still produce wrong final output, because a per-stage check only
verifies that stage's own contract — it has no way to see that a downstream
stage silently dropped a field an upstream stage added, or that the
composition of several individually-correct transformations produces an
incorrect result together. Measuring and validating the pipeline's actual
end-to-end output against the original source — not just confirming each
stage individually reports success — is what catches this class of
cross-stage bug that per-stage validation structurally cannot see, for
exactly the same reason binary checks can't see distributional drift: each
local view is technically correct and still misses the failure.
