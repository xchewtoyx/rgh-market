---
type: concept
title: Paltering and Weasel-Wording Detection
description: Catching statements that are literally true but engineered to create a false impression, or that use vague phrasing specifically to dodge accountability.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 1"
---
# Paltering and Weasel-Wording Detection

A statement can pass a literal fact-check — every word technically true — and still mislead, by exploiting the gap between what a sentence literally says and what a reasonable listener will infer from it (linguistic **implicature**). Checking only literal truth misses this entire failure mode.

## Paltering
**Paltering** is misleading through technically true statements rather than outright lying. Examples of the pattern: a present-tense denial that's true at the moment spoken but implies a broader, false claim ("there is no relationship" said after one recently ended); a mild negative phrasing that implies more than it states ("it wasn't terrible" implies mediocre, not good); a narrow comparison that implies a broader one ("not the most responsible father I've ever known" technically just names one better father, while implying the subject is bad generally). Paltering carries plausible deniability — the speaker can always point to the literal words — and draws less social sanction than an outright lie, which is exactly what makes it attractive to someone trying to mislead without being caught doing so.

## Weasel Wording
**Weasel wording** uses the same literal/implied gap specifically to dodge accountability rather than to imply something false:
- **Asymmetric qualifiers**: "reduces X by up to 50%" is false only if the product ever exceeds 50% — it says nothing about the typical result, while implying one close to the ceiling.
- **Agentless passive voice**: "mistakes were made" removes the actor who made them, avoiding a direct claim about who's responsible.
- **Unsourced hedges**: "people are saying" attributes a claim to an unnamed, unverifiable collective, avoiding both sourcing responsibility and the legal exposure of a direct assertion.
- **Jargon substitution**: replacing a plain, verifiable description of a bad situation with vague institutional language (e.g., "collaborative action with global stakeholders" standing in for a specific harmful practice) obscures what's actually being claimed or admitted.

## Verification Action
When auditing a claim, check not only whether its literal words are true but what a reasonable reader would infer from it — if the inferred meaning is false or unsupported even though the literal statement is true, flag the statement as misleading regardless of its technical accuracy. Be specifically alert to passive voice with no named actor, qualifiers like "up to," and vague institutional jargon substituting for a specific factual claim — each is a common surface signal for paltering or weasel-wording underneath.

## See Also
- [Unfair Comparison Detection](unfair-comparison-detection.md)
- [Hedge Words for Uncertain Claims](hedge-words-for-uncertain-claims.md)
