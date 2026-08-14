---
type: concept
title: Cherry-Picking
description: The selective presentation of data or sources that support a specific conclusion while ignoring conflicting evidence.
sources:
  - title: "The Chicago Guide to Fact-Checking, Second Edition"
    resource: "The Chicago Guide to Fact-Checking, Second Edition (Brooke Borel), ch. 4, 6"
  - title: "WebGPT: Browser-assisted question-answering with human feedback"
    resource: "WebGPT: Browser-assisted question-answering with human feedback (Nakano, Hilton, Balaji, Wu, Ouyang, Kim, et al.), ch. 6"
  - title: "Data Science from Scratch, 2nd Edition"
    resource: "Data Science from Scratch, 2nd ed. (Joel Grus), ch. 7"
---
# Cherry-Picking

**Cherry-picking** is the selective suppression of conflicting evidence. It occurs when a writer or researcher presents only the data points, source citations, or case studies that align with their preferred conclusion, while ignoring a larger body of evidence that contradicts it.

## Verification Safeguards Against Cherry-Picking

To verify a document against cherry-picking, a reviewer must:
- **Independent Research**: Perform independent research to locate the broader consensus or context on the topic.
- **Context Preservation**: Check if the cited evidence represents the mainstream view or is an outlier, and verify that quotes or data points are not extracted out of context to distort their meaning.
- **Evidence Triangulation**: Ensure that multiple independent lines of inquiry and different sources agree on the conclusion. See [evidence triangulation](evidence-triangulation.md).
- **Omission Scrutiny**: Inspect the document for omitted variables, missing data points, or alternative viewpoints. See [omission detection](omission-detection.md).

## Named Malpractice: P-Hacking
**P-hacking** is cherry-picking applied to statistical analysis: manipulating the data selection or analysis method until an acceptably low p-value is reached, misusing statistics to manufacture a desired result rather than reporting what the data actually shows. Running many comparisons in search of a significant-looking result is the same underlying mechanism as [spurious correlation detection](spurious-correlation-detection.md)'s data dredging. A p-value below the common 0.05 threshold does not itself rule out p-hacking — with that threshold, roughly 5 out of 100 experiments with no real underlying relationship would still be expected to cross it by chance, so a lone low p-value is weak evidence on its own (a stricter significance threshold is standard in some fields for this reason). Simulation bears this out directly: repeating a fair-coin experiment thousands of times and rejecting "fairness" whenever the result falls outside a 5% two-sided rejection region produces rejections at essentially the nominal 5% rate even though every coin was fair — the test is working as designed, which means **any** process that tries enough hypotheses or trims enough outliers will eventually surface a "significant" false lead. When a draft cites a p-value or statistical significance claim, a non-statistician reviewer should still check whether the paper defines and reports its p-value honestly, and consult a statistician when in doubt.

Good practice against p-hacking mirrors [precommitted evaluation criteria](precommitted-evaluation-criteria.md): determine hypotheses before looking at the data, clean data without the hypotheses in mind, and treat p-values as one input — not a substitute for domain judgment or [evidence triangulation](evidence-triangulation.md).

A related but distinct malpractice happens at interpretation time rather than analysis time: see [precommitted evaluation criteria](precommitted-evaluation-criteria.md) for why a success/failure threshold defined only after seeing the result is as suspect as an analysis method chosen only after seeing the data.

## Optimization Pressure Toward Convincing, Not Representative, Evidence
Cherry-picking doesn't require deliberate intent to mislead — it can also emerge purely from an evaluation process that rewards *convincing* a reviewer rather than *fairly representing* the total evidence. A process that trains or reinforces a searcher's behavior based on whether a human reviewer found the presented evidence persuasive (rather than on whether it was a fair account of what's actually out there) will predictably drift toward selecting the most convincing available evidence, even without anyone intending to deceive — the searcher, human or automated, is simply optimizing the metric it was actually given. This is a specific instance of [Goodhart's Law](goodharts-law.md) applied to evidence-gathering itself: "find supporting evidence" quietly becomes a proxy target ("find *persuasive* evidence") that diverges from the real goal ("give a fair assessment"). It tends to worsen, not self-correct, as the searcher gets better at the task, because a more capable searcher is simply more effective at finding whatever is most convincing — see [adversarial evidence elicitation](adversarial-evidence-elicitation.md) for a process-level countermeasure that doesn't rely on the searcher's own restraint.
