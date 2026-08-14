---
type: concept
title: Default-Negative Values Masking Missing Signal
description: A field initialized to a default value and updated only when a separate confirming feed arrives is indistinguishable from a genuine negative when that feed silently fails, so its completeness must be verified independently of the field's own stored value.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Cathy Chen, Niall Richard Murphy, Kranti Parisa, D. Sculley, Todd Underwood), ch. 15, case study by Daniel Papasian, \"Ad Click Prediction: Databases Versus Reality\""
---
# Default-Negative Values Masking Missing Signal

A recorded "ground truth" field is often not a direct observation of reality but a **proxy populated by an upstream pipeline**: the field starts at a default value and is only overwritten once a separate, asynchronous feed confirms the true value. This structure has a specific, silent failure mode: if the confirming feed stops delivering entirely, the field never gets an error, a null, or any other signal that something is wrong — it simply stays at its default, which is a fully-formed, valid-looking record indistinguishable from a genuine negative.

## Worked Example

A production ad-click prediction system recorded, for every ad shown, a `click` boolean defaulted to `false`. A separate click-logging pipeline verified real clicks (filtering fraud) and updated the bit to `true` when a legitimate click was confirmed. The model trained on this bit as its label. When the click-logging pipeline suffered an outage, every ad shown during the outage window kept its default `click = false` — not because those ads genuinely weren't clicked, but because no confirming signal ever arrived to overwrite the default. The stored data was internally well-formed and passed no validation error; it was simply wrong. The resulting model, trained on data where an entire window of real clicks was invisible, correctly (given what it was shown) learned that click probability was near zero — a large behavioral shift traceable entirely to a data-completeness failure that never announced itself as one.

## Why a Held-Out Check Can Fail to Catch It

A held-out validation set is only independent evidence if it doesn't share the same failure with the thing it's checking. In the case above, the automated pre-deployment validation gate held out a random sample of recent rows and compared new-model loss against old-model loss on them — but that held-out sample was drawn from the very same pipeline, over the very same outage window, so its labels were corrupted identically to the training data. The gate reported the corrupted model as an improvement, because "improvement" was measured entirely in terms of a label that was wrong in the same way on both sides of the comparison. See [evidence triangulation](evidence-triangulation.md): a second check only counts as independent if it doesn't inherit the same upstream dependency as the thing being checked.

## Distinguishing This From Data Censoring

This differs from [data censoring](data-censoring.md), where an observation window closes before an outcome has genuinely occurred yet, and a naive analysis mishandles the still-pending cases. Here the field is not pending or missing in any way visible to a downstream consumer — it holds a specific, valid value that looks exactly like a confirmed observation. Censoring is detectable by asking "which cases are still open?"; this failure mode is not, because nothing distinguishes "confirmed false" from "never confirmed" in the stored representation.

## Verification Action

When a claim rests on a recorded field that is populated asynchronously by an upstream feed (a label, a status flag, a confirmation bit):
- Ask what the field's value looks like when the confirming feed simply never arrives — if it's identical to a legitimate negative, treat the field's completeness as a separate claim requiring its own evidence, not something the field's own value can attest to.
- Check whether the upstream feed's own health or completeness has an explicit availability target and alerting, independent of the field it populates — see [incident postmortem verification](incident-postmortem-verification.md) for structuring the response once such a gap is found.
- Add an aggregate sanity check on the field's overall rate (e.g., "the fraction of positive labels in this window should not be surprisingly low or high compared to history") as a cheap, coarse detector for exactly this failure — see [numeric sanity checking](numeric-sanity-checking.md).
- Before trusting a held-out or validation check as independent confirmation, confirm it does not draw on the same upstream feed as the data it's meant to validate.

## See Also
- [Evidence Triangulation](evidence-triangulation.md)
- [Data Censoring](data-censoring.md)
- [Numeric Sanity Checking](numeric-sanity-checking.md)
- [Training Data Provenance Check](training-data-provenance-check.md)
- [Incident Postmortem Verification](incident-postmortem-verification.md)
