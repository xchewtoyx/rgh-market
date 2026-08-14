---
type: concept
title: Hawthorne Effect Check
description: Checking whether a measured improvement following an intervention could be an artifact of participants knowing they were being observed or studied, rather than the intervention itself.
sources:
  - title: "The Checklist Manifesto: How to Get Things Right"
    resource: "The Checklist Manifesto (Atul Gawande), ch. 7"
  - title: "How to Measure Anything: Finding the Value of Intangibles in Business"
    resource: "How to Measure Anything, 3rd ed. (Douglas W. Hubbard), ch. 8"
---
# Hawthorne Effect Check

The **Hawthorne effect** is the tendency for people to change their behavior, often for the better, simply because they know they're being watched or studied — independent of whatever intervention is actually being evaluated. A before-after (pre/post) study of a real-world intervention is specifically vulnerable to this: without a randomized control group that experiences the same observation but not the intervention, an improvement measured after rollout could be produced by the extra scrutiny of the study itself rather than by the intervention.

## Why Pre/Post Designs Are Exposed to This
A before-after comparison (measuring an outcome before an intervention, then again after) lacks the counterfactual a randomized controlled trial provides — there's no group that was observed just as closely but didn't receive the intervention, so an observation-driven improvement and an intervention-driven improvement are hard to distinguish from the raw before/after numbers alone. The same design is also vulnerable to other confounds that have nothing to do with the intervention: a secular trend already underway before the intervention, or regression to the mean if the "before" period happened to catch an unusually bad stretch.

## How Studies Rule It Out
Full randomization isn't always practical or ethical for real-world interventions (e.g., a hospital safety protocol change). A substitute technique is to check whether the measured effect holds consistently across conditions where the degree of scrutiny or observation plausibly differed:
- **Subgroup consistency**: does the effect hold across sites, teams, or time periods that received different amounts of direct observation or attention during the study, not just in the specific location most closely monitored?
- **Explicit observer-presence analysis**: a study reporting an outcome improvement should specifically check and report whether the effect size differs between more closely observed and less closely observed conditions — a real worked case tested and reported that a measured improvement held independent of observer presence specifically, which is the direct test for this confound rather than an incidental one.

## Verification Action
When a draft cites a before-after study as evidence an intervention caused an improvement, check whether the study addresses the Hawthorne effect directly (an explicit observer-presence check) or only indirectly (consistency across diverse subgroups/sites). A pre/post study that doesn't address this at all should be treated as weaker evidence than one that does, even if both report the same headline effect size.

## The Cheapest Fix Is Concealment
Where randomization or a control group isn't practical, the most direct mitigation is to keep the fact of observation concealed from subjects wherever feasible — the effect only requires that subjects *know* they're being watched, so a measurement design that observes without the subject's awareness (analogous to how [blinding](blinding-to-prevent-bias.md) removes an evaluator's or subject's knowledge of which condition is in effect) sidesteps the confound rather than requiring a statistical correction for it after the fact.

## See Also
- [Confounding Variables](confounding-variables.md)
- [Experimental vs. Observational Causal Evidence](experimental-vs-observational-causal-evidence.md)
- [Blinding to Prevent Bias](blinding-to-prevent-bias.md)
