---
type: concept
title: Root Cause Fallacy
description: Complex system failures typically arise from multiple factors that are individually necessary and only jointly sufficient, so a single "root cause" is a constructed stopping point for an investigation, not a discovered fact.
sources:
  - title: "The Field Guide to Understanding 'Human Error'"
    resource: "The Field Guide to Understanding 'Human Error' (Sidney Dekker), ch. 3"
  - title: "Drift into Failure: From Hunting Broken Components to Understanding Complex Systems"
    resource: "Drift into Failure (Sidney Dekker), ch. 1-2"
---
# Root Cause Fallacy

In a complex, well-defended system, a failure typically results from a conjunction of multiple contributing factors that are individually necessary but only jointly sufficient to produce the outcome — no single one of them "caused" the failure on its own, since removing any one of them would likely have prevented it. Treating one of these factors as *the* root cause is a choice about where to stop looking, not a factual discovery about which factor was uniquely responsible. Different investigating parties looking at the same failure routinely **construct** different causes depending on their institutional position and what each party is positioned (or motivated) to fix — a regulator's investigation and the affected organization's own investigation can both be evidence-based and still land on different "root causes" for the identical event, because cause-finding involves selecting a stopping point in a branching causal web, not extracting a single fact already present in the evidence.

## Relationship to Other Causal Concepts
This is a system-failure-specific instance of the general pattern in [necessary, sufficient, and probabilistic cause](necessary-sufficient-probabilistic-cause.md): a factor can be a necessary contributor to a specific failure without being sufficient on its own, and a document that names one contributing factor as "the" cause is implicitly (and often silently) claiming sufficiency it hasn't actually established. It also compounds with [hindsight bias in review](hindsight-bias-in-review.md): knowing the outcome makes it tempting to trace a single clean causal thread backward from it, when the actual antecedent conditions were multiple, entangled, and only some of them are being highlighted.

## "Broken Component" Investigations That Never Reach Systemic Causes
A recurring pattern in real investigations: pursuing the causal chain further and further up an organization (from a worn part, to a maintenance program, to a regulator) can still terminate in a list of "broken" components at every level — a badly maintained part, an inadequate procedure, an under-resourced inspection regime — without ever explaining why none of these looked deficient to the people responsible for them *at the time*, before the outcome was known. A thorough investigation that nonetheless stops at naming more and different broken parts, rather than examining the relationships and incentives that made each of those parts' state locally unremarkable, has not actually reached a systemic explanation — it has just extended the same broken-component logic to a wider blast radius. See [normalization of deviance](normalization-of-deviance.md) for the specific mechanism by which a component's state can drift to a hazardous point while every individual step along the way looked locally reasonable.

## Official and Rival Explanations Can Share the Same Flawed Premise
When a high-profile investigation fails to identify a single conclusive cause, the resulting vacuum tends to spawn both an official "best available" verdict and one or more rival theories claiming a different, more definitive cause was missed. A years-long, well-resourced investigation into an aircraft's mid-air breakup never found a single conclusive triggering component and settled on a "most likely" ignition source; the resulting uncertainty fed several competing conspiracy theories insisting a different, more concrete cause existed and had merely been overlooked or covered up. The official investigators and the conspiracy theorists disagreed sharply about *which* single cause was correct, but shared, without examining it, the identical assumption that a single, locatable, "smoking gun" cause must exist somewhere — neither camp seriously entertained that ordinarily-functioning components interacting in an unforeseen way, with no individual failure at all, could be the actual explanation. When evaluating a dispute between an official account and its critics, check whether both sides are actually contesting the same unexamined premise (that a single findable cause exists) rather than genuinely disagreeing about the nature of causation itself.

## Verification Action
- When a document names "the root cause" of an incident or failure, check whether the underlying investigation actually supports single-factor causation, or whether multiple contributing factors were each individually necessary — if so, the document should say so rather than collapsing the finding to one factor.
- Ask who conducted the investigation and what stopping point they had an institutional or professional interest in reaching — a different investigating party looking at the same evidence may reasonably have constructed a different "root cause," and a document should acknowledge if other credible investigations reached different conclusions (see [presenting genuine source disagreement](presenting-genuine-source-disagreement.md)).
- Prefer and look for language that lists contributing factors and their interaction, over language that names a single terminal cause — a real systemic investigation into a well-defended system usually surfaces recommendations spanning multiple organizational levels, not a single fix at a single point.
- Separately evaluate the [epistemic level separation](epistemic-level-separation.md) between what the raw evidence establishes and where the investigation chose to stop attributing cause — the stopping point itself is an interpretive choice, not a data point.

## See Also
- [Necessary, Sufficient, and Probabilistic Cause](necessary-sufficient-probabilistic-cause.md)
- [Hindsight Bias in Review](hindsight-bias-in-review.md)
- [Incident Postmortem Verification](incident-postmortem-verification.md)
- [Epistemic Level Separation](epistemic-level-separation.md)
- [Pseudo-Explanatory Labels](pseudo-explanatory-labels.md)
- [Independent Forensic Investigation as the Basis for Evidence-Based Consensus](independent-forensic-investigation.md)
