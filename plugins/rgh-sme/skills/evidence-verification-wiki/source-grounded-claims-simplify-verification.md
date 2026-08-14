---
type: concept
title: Source-Grounded Evaluation Simplifies Verification
description: Checking whether a claim is supported by a specific cited source is a more accurate and more consistent task than judging the claim's truth directly, but only if the cited source was chosen fairly rather than persuasively.
sources:
  - title: "WebGPT: Browser-assisted question-answering with human feedback"
    resource: "WebGPT: Browser-assisted question-answering with human feedback (Nakano, Hilton, Balaji, Wu, Ouyang, Kim, et al.), ch. 6"
---
# Source-Grounded Evaluation Simplifies Verification

Asking a reviewer "does this cited source actually support this claim?" is a fundamentally easier and more reliable task than asking "is this claim true?" — especially for technical, subjective, or vague claims where truth itself is hard to adjudicate directly from general knowledge. Grounding a claim in a specific citation converts an open-ended judgment call into a narrower correspondence check: does the source say what is claimed, and does it say it with the stated force.

## Why Source-Grounding Improves Both Accuracy and Agreement
Two distinct benefits follow from requiring cited support rather than a bare assertion:
- **More accurate verification**: a reviewer checking correspondence between a claim and its cited source has a concrete target to compare against, rather than having to independently establish the underlying fact from scratch or from background knowledge alone.
- **Less noisy verification**: comparing a claim to a citation is a much more specifiable, procedure-like check than judging truth directly, which produces higher agreement between independent reviewers checking the same claim — and higher inter-reviewer agreement is itself a precondition for collecting consistent verification judgments at scale rather than idiosyncratic ones.

This is the same mechanism that makes [defining checkable claims](defining-checkable-claims.md) valuable in the first place — a claim tied to a locatable source is precisely what makes "a specific, reproducible path to verify it" possible — and it is why [citation completeness](citation-completeness-check.md) matters beyond attribution ethics: a citation that actually lets a reader trace and check the claim is what makes the accuracy-and-agreement benefit real rather than aspirational.

## The Transparency Byproduct
A verification process built around inspectable sources has a second advantage beyond the reviewer's own accuracy: it is auditable by someone other than the reviewer. If the evidence trail supporting a claim is a set of named, followable sources rather than an opaque judgment, any later reader can retrace the same path and reach an independent opinion, instead of having to trust the evaluator's unexplained conclusion. This is the same property [progressive reasoning disclosure](progressive-reasoning-disclosure.md) asks for in the reasoning that connects evidence to conclusion, applied specifically to the sourcing step: showing which source backs which claim, not just stating that verification "was done."

## The Caveat: This Benefit Assumes Fair Source Selection
The gain from source-grounding depends entirely on the cited source being a fair representation of the total evidence, not merely a convenient or persuasive one. If whoever is gathering references is rewarded for finding sources that *convince* a reviewer rather than for finding sources that are *representative*, the ease of checking "does this source say X" stops being a genuine accuracy improvement — the reviewer ends up accurately confirming a cherry-picked pairing, not accurately confirming the underlying claim. See [cherry-picking](cherry-picking.md) for this failure mode and the optimization pressure that produces it, and [adversarial evidence elicitation](adversarial-evidence-elicitation.md) for a process-level countermeasure.

## Verification Action
- When a claim is supported by a citation, explicitly check the narrower question — "does this source say this, with this force" — rather than re-litigating the claim's truth from first principles; this is both faster and more reliable than independent adjudication.
- Do not treat "the claim has a citation" as sufficient on its own — separately confirm the citation was not selected because it was persuasive rather than representative (see [cherry-picking](cherry-picking.md), [evidence triangulation](evidence-triangulation.md)).
- When designing a review or labeling process, prefer structuring the task as source-correspondence checking over open-ended truth judgment wherever a genuine source exists to check against — the task redesign itself is a verification-quality improvement, not just a convenience.

## See Also
- [Defining Checkable Claims](defining-checkable-claims.md)
- [Citation Completeness Check](citation-completeness-check.md)
- [Cherry-Picking](cherry-picking.md)
- [Adversarial Evidence Elicitation](adversarial-evidence-elicitation.md)
- [Progressive Reasoning Disclosure](progressive-reasoning-disclosure.md)
