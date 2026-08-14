---
type: concept
title: Experimental vs. Observational Causal Evidence
description: Why randomized manipulation of a variable provides stronger causal evidence than an observed association, and how converging independent manipulations build further confidence.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 4"
  - title: "The DevOps Handbook, 2nd Edition"
    resource: "The DevOps Handbook, 2nd Edition (Kim, Humble, Debois, Willis, Forsgren), ch. 17"
  - title: "Superforecasting: The Art and Science of Prediction"
    resource: "Superforecasting (Philip E. Tetlock, Dan Gardner), ch. 2"
---
# Experimental vs. Observational Causal Evidence

Randomized, controlled manipulation of a variable is the strongest available evidence for a causal claim, because it breaks the link between the variable being studied and any confounding factor that might otherwise explain an observed association. Observational data alone — where the variable of interest wasn't randomly assigned — is much more vulnerable to hidden confounds and [selection bias](confounding-variables.md).

## Worked Example: Fever-Reducing Drugs
Observational data shows fever-reducing drugs correlated with slower recovery from viral infection. But drug assignment wasn't random in that data — sicker patients were more likely to be given antipyretics in the first place, a selection-bias confound that alone could produce the same correlation with no causal effect of the drug at all. Randomized trials (assigning the drug independent of how sick a patient was) found the drugs genuinely did slow recovery and increase transmission. Separately, animal experiments using *physical cooling* instead of drugs (ruling out any drug-specific side effect unrelated to temperature itself) replicated the same effect — two independent manipulations converging on the same causal conclusion built far more confidence than either alone.

## Worked Example: Opt-In Program Evaluation
Observational comparisons of people who voluntarily opted into a wellness or improvement program against those who didn't consistently found the program associated with better outcomes. A properly randomized version of the same evaluation (randomizing who was even offered the program, then separately tracking who chose to opt in among those offered it) found the program itself had no statistically significant effect on the outcomes originally claimed. A follow-up analysis restricted only to the people who had been offered the program then reproduced the original (spurious) observational pattern: opt-in participants looked better on the outcome even after adjusting for measurable differences — confirming the earlier observational research had been capturing [selection bias](selection-bias.md) (healthier or more motivated people self-select into voluntary programs) rather than a genuine effect of the program itself.

## Worked Example: A/B Testing Confident Predictions
A claim doesn't need to be observational to need verification — a confidently-argued prediction about what change will cause an improvement is itself just an unverified causal hypothesis until tested. In large-scale online controlled experiments (A/B tests) studied by Microsoft's experimentation group, only about one-third of well-designed feature experiments actually produced the predicted improvement in their target metric — the other two-thirds had negligible or negative effect, despite each having seemed like a reasonable, well-argued idea beforehand. The lesson generalizes beyond software features: a stakeholder's or author's confidence that "doing X will cause Y" is not evidence that it will — it is an untested causal hypothesis, and the base rate at which such confident predictions turn out true, even from domain experts, is often much lower than the confidence with which they're asserted.

## Worked Example: Medicine Before and After Randomized Trials
For most of medical history, treatments spread on authority and anecdote rather than randomized assignment — and judged by modern evidence, many were useless or harmful. Even early controlled experiments could fail to change practice if their implications weren't understood: James Lind's 1747 scurvy trial compared six treatments among paired sailors, but scurvy kept killing sailors for generations afterward because the result wasn't integrated into policy. Randomized controlled trials as a rigorous norm took hold much later; Austin Bradford Hill's logic for the "numerical method" was that random assignment balances unknown differences across large enough groups so outcome differences can be attributed to treatment rather than confounds — "it isn't perfect… but it beats wise men stroking their chins."

When cardiac care units were introduced, many physicians argued it was unethical to withhold them in a trial. Archie Cochrane ran a randomized comparison anyway (cardiac unit vs. home bed rest). Mid-trial he told cardiologists results leaned toward the units — then revealed he'd reversed the direction; home care had actually done slightly better, exposing how prior belief had been driving interpretation. National policies rolled out without any trial — such as a "short, sharp, shock" incarceration program for young offenders — leave subsequent crime trends consistent with many contradictory explanations, because no randomized test ever established what the policy itself caused.

## Verification Action
- When a draft's causal claim rests on observational data with no random assignment, flag the possibility of a selection-bias or other confound that could produce the same pattern without the causal mechanism claimed — see [confounding variables](confounding-variables.md) and [selection bias](selection-bias.md).
- Treat a claim as more strongly supported when independent manipulations of the same underlying cause (different methods, different populations, different research groups) converge on the same result — this is a causal-evidence-specific case of general [evidence triangulation](evidence-triangulation.md).

## See Also
- [Correlation vs. Causation](correlation-vs-causation.md)
- [Confounding Variables](confounding-variables.md)
- [Evidence Triangulation](evidence-triangulation.md)
- [Hawthorne Effect Check](hawthorne-effect-check.md)
- [Blinding to Prevent Bias](blinding-to-prevent-bias.md)
