---
type: concept
title: Alternative Hypothesis Consideration
description: Actively searching for a better or alternative explanation before accepting the first explanation offered for an observed pattern.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 8, 10"
  - title: "The Craft of Research, Fifth Edition"
    resource: "The Craft of Research, Fifth Edition (Booth, Colomb, Williams, Bizup, FitzGerald), ch. 6"
  - title: "Sources of Power: How People Make Decisions"
    resource: "Sources of Power (Gary Klein), ch. 11"
---
# Alternative Hypothesis Consideration

Having *an* explanation for a true phenomenon doesn't make it *the* explanation. A claim can offer a real, non-fabricated pattern and still attach the wrong causal story to it — verification requires actively brainstorming the space of plausible alternative explanations, not just checking whether the one offered is internally plausible.

## Worked Example
A news alert reported a company's stock dropping after a specific announcement, implying the announcement caused the drop. But the timeline showed the price decline had already happened *before* the announcement, driven instead by a broader market-wide move that morning — the timeline itself falsified the implied causal story once checked. A magnitude check reinforced the same conclusion: the announcement concerned a business unit far too small, relative to the company's total revenue, to plausibly move the stock price by the amount claimed.

## Worked Example: Extraordinary Claims Need Ruled-Out Alternatives
A paper found a correlation between facial-contour measurements and sexual orientation and offered it as support for a specific biological theory (prenatal hormone exposure). Even granting the correlation was real, the paper hadn't ruled out other mechanisms consistent with the exact same facial-contour data: genetics, non-hormonal environmental factors, or reverse causation (e.g., diet or exercise habits affecting both facial structure and behavior). An extraordinary or field-upending explanatory claim needs evidence that positively rules out competing explanations for the same pattern, not just evidence that the pattern itself is real — a genuine correlation supports *an* explanation, not automatically the specific one being proposed for it.

## Prefer the Simpler Explanation
When two candidate explanations fit the same evidence equally well, prefer the simpler one. A widely-cited paper claimed ~90% accuracy training a model to distinguish "criminal" from "noncriminal" faces from photos, attributing its discriminating features (inter-eye distance, nose-mouth angle, lip curvature) to facial structure revealing criminality. Those same features are also exactly what changes between a smiling and a neutral/frowning face — and the paper's own training photos showed noncriminal subjects smiling in flattering self-selected photos while criminal subjects showed neutral or scowling expressions in bureaucratic ID photos. The simpler explanation (the model learned to detect smiles, a self-presentation artifact of the mismatched photo sources) fit the same data at least as well as the extraordinary one (facial structure reveals criminality) — and required no exotic evidence to support it, unlike the extraordinary claim.

## The Audience Test
A well-formed claim should be able to survive a reasonable reader asking: *Why should I believe this over another explanation? What exceptions exist? Is there a better account of the same evidence?* If a claim's author hasn't already run this test against their own claim, a reviewer should run it on their behalf before accepting the claim as verified — this is distinct from checking whether the cited facts are individually accurate, since a claim built on accurate facts can still lose to a better-fitting alternative explanation.

## Stress-Test a Theory by Forcing It Into a Concrete Story
A theory that sounds plausible while stated abstractly can collapse once someone actually tries to spell out, step by step, the concrete sequence of events it requires. A conspiracy theory alleging a second shooter (to explain an official account's seemingly implausible single-bullet trajectory) sounds vaguely credible left vague — but a detailed analysis that actually worked out what the conspirators would have had to plan, predict, and fake in real time (a bullet's exact path pre-selected before unpredictable actual gunshots occurred, physical evidence fabricated to match, a genuinely wounded second victim's real wound somehow still needing to be accounted for) found the number of required implausible coincidences and improvised contingencies ballooned once the story was actually built out — progressively destroying its plausibility. The lesson generalizes: an explanation that only survives being stated in vague, high-level terms should be forced into a fully concrete, step-by-step account before being accepted — the exercise of constructing the detailed story is itself a diagnostic test, separate from checking any individual fact within it.

## Verification Action
Before accepting a causal or explanatory claim, generate at least one plausible competing explanation for the same observed pattern and check it against the same evidence (timeline, magnitude, [confounding variables](confounding-variables.md)) before accepting the offered explanation as correct.

## See Also
- [Correlation vs. Causation](correlation-vs-causation.md)
- [Confounding Variables](confounding-variables.md)
- [Null Model Testing](null-model-testing.md)
- [Objection Anticipation in Argument Construction](objection-anticipation-in-argument-construction.md)
