---
type: concept
title: Survivorship Bias
description: Drawing conclusions only from the cases that survived some selection process to become observable, while the systematically missing, unobserved cases carry the more important information.
sources:
  - title: "The Field Guide to Understanding 'Human Error'"
    resource: "The Field Guide to Understanding 'Human Error' (Sidney Dekker), ch. 7"
  - title: "How to Take Smart Notes: One Simple Technique to Boost Writing, Learning and Thinking"
    resource: "How to Take Smart Notes (Sönke Ahrens), ch. 12"
---
# Survivorship Bias

**Survivorship bias** occurs when a conclusion is drawn from a set of cases that survived some selection process to become observable, without accounting for the cases that didn't survive and so are structurally absent from the visible data — even though those missing cases are often exactly the ones that matter most for the question being asked.

## The Canonical Case: Wald's Bombers
In World War II, statistician Abraham Wald was asked where to add armor to bombers, based on a damage map of bullet holes on planes that returned from missions. The intuitive answer — armor the areas with the most bullet holes — is backwards. A bomber hit in those areas evidently survived the hit and made it home, so those locations mark *survivable* damage. The planes hit in the areas with *no* recorded holes on returning aircraft didn't make it back at all — those are exactly the locations that need armor, and the data set of returning planes can't show them directly, because a plane hit there is missing from the sample entirely, not present with zero damage recorded.

## Why This Is a Distinct Failure Mode
This is related to but distinct from ordinary [selection bias](selection-bias.md): selection bias is about the sampled cases differing systematically from the population with respect to the variable being measured. Survivorship bias is the specific version where the selection mechanism *is the very outcome under study* — only cases that "succeeded" (survived, published, still exist, are still operating) are observable at all, so any pattern found only within the surviving set risks being an artifact of what it takes to survive, not a genuine finding about the broader population including the cases that didn't make it.

## A Second Case: Studying Only Successes
The same mechanism distorts business and management writing: an archive of thousands of consumer products built by studying what's on shelves overwhelmingly captures failures once you account for the base rate (most new products fail), yet companies and case-study writers rarely study their own or competitors' failed products systematically — success biographies and "best practices" writing draw almost entirely on survivors, silently excluding the (often much larger) set of organizations or products that tried similar things and disappeared. A claim like "companies that did X succeeded" is unfalsifiable and largely uninformative without also knowing the outcome rate among comparable companies that did X and failed.

## Recognizing It
A signal that survivorship bias may be operating: a dataset, sample, or evidence base is drawn entirely from things that are still around to be examined (companies still in business, systems still in production, records that weren't destroyed, people who returned from an event) with no accounting for what happened to the ones that aren't. The absence of unsuccessful/destroyed/discontinued cases from the visible evidence is not evidence they didn't matter — it may be exactly why they're invisible.

## Verification Action
- When a claim is based on examining a set of current or surviving examples (successful companies, systems still running, incidents that were reported), ask what selection process determined which cases are observable at all, and whether cases that failed the same process are systematically missing rather than merely rare.
- Ask specifically whether the missing cases would plausibly show the *opposite* pattern from the surviving ones, in which case the visible data is misleading rather than merely incomplete — as in Wald's example, where the most-damaged (missing) planes needed protection at the areas showing the least damage among the ones that survived.
- Where possible, seek out evidence about the missing/excluded cases directly, rather than assuming the visible sample can stand in for the whole population.

## See Also
- [Selection Bias](selection-bias.md)
- [Data Censoring](data-censoring.md)
- [Berkson's Paradox](berksons-paradox.md)
