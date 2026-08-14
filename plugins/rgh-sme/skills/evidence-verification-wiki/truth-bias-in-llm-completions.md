---
type: concept
title: Truth Bias in LLM Completions
description: A generative model tends to continue and build on a false or nonsensical premise already present in its input rather than questioning or correcting it, so responsibility for input correctness falls entirely on the human.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 2"
---
# Truth Bias in LLM Completions

A generative language model, prompted with a premise, will typically continue as though that premise is true rather than pausing to question or correct it — even when the premise is false, counterfactual, or nonsensical. This **truth bias** follows from how the model is trained: documents in the training data that open with an incorrect claim and then explicitly self-correct mid-document are rare, so the statistically likely continuation of a document containing a false premise is one that keeps building on it, not one that interrupts to challenge it. See [verifying generative AI outputs](verifying-generative-ai-outputs.md) for the broader mechanism (training-data mimicry with no internal distinction between recalled fact and invention) this is a specific instance of.

## Two-Sided Consequence

Truth bias is neither purely a defect nor purely a hazard — the same mechanism cuts both ways:

- **Exploitable deliberately**: a hypothetical can be written as an already-true premise rather than an explicit "pretend that" framing (e.g., "It's 2031, a full year since the first Neanderthals were resurrected" rather than "Pretend that it's 2030 and Neanderthals have been resurrected"), and truth bias will produce a more fully in-character, committed hypothetical answer than an explicit pretend-frame would. Comparing a model's response to the same scenario posed as a stated premise versus posed as an explicit hypothetical question is a useful way to see the effect directly.
- **A verification hazard, especially in automated pipelines**: any counterfactual, outdated, or simply mistaken element that gets introduced into a prompt — whether by a careless human author or, more insidiously, by a programmatic step upstream in an application (a stale variable, a bad retrieval result, a prior turn's uncorrected error) — will not be second-guessed by the model the way a human reader would raise an eyebrow at it. The model has no mechanism analogous to a reader's background knowledge flagging "that doesn't sound right." Correctness of everything fed to the model is entirely the responsibility of the application or prompt author; the model will not catch it for you.

## Verification Action

- When reviewing AI-assisted output (a document, an answer, a generated report), check the *input* the system was given, not just the output it produced — an unquestioned false premise upstream propagates into a confidently stated downstream claim with no internal signal that anything was ever wrong.
- In a multi-step or programmatic pipeline where one model's output becomes a later step's input, treat every hop as a place a bad premise can enter and then be silently carried forward uncorrected — this compounds the general caution in [automation bias in verification](automation-bias-in-verification.md) against trusting automated output as self-correcting.
- Do not read a model's willingness to answer "in character" with a false or hypothetical premise as any kind of corroboration of that premise — the model continuing a premise is evidence the premise went unquestioned, not evidence the premise is true.
- Do not rely on prompt instructions like "point out anything false in the following" as a substitute for actually checking the input yourself — the same truth bias that makes the model continue a false premise elsewhere in a document can also blunt its willingness to flag one when asked to review it, particularly if the false premise is stated as established fact rather than something visibly in question.

## See Also
- [Verifying Generative AI Outputs](verifying-generative-ai-outputs.md)
- [Automation Bias in Verification](automation-bias-in-verification.md)
- [Confabulation in Testimony](confabulation-in-testimony.md)
- [Defining Checkable Claims](defining-checkable-claims.md)
