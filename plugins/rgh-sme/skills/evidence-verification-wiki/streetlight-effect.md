---
type: concept
title: Streetlight Effect
description: Searching for evidence only where existing tools or familiarity make looking convenient, rather than where the answer is actually likely to be found.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 2"
---
# Streetlight Effect

Named for the joke about a drunk man searching for lost keys under a streetlight — not because he lost them there, but because that's where the light is — the **streetlight effect** (or streetlight anti-methodology) is the tendency to investigate a problem exclusively using the tools, data sources, or areas one is already familiar and comfortable with, regardless of whether that's where the evidence relevant to the actual question is likely to be. It produces investigations that look thorough (real tools were used, real data was gathered) while systematically missing whatever the familiar tools can't see.

## Why It's a Distinct Failure Mode
This differs from ordinary [confirmation bias in verification](confirmation-bias-in-verification.md), which is about scrutinizing agreeable claims less than disagreeable ones. The streetlight effect operates even absent any prior belief about the answer — it's a bias in *where a reviewer looks*, driven by convenience and familiarity rather than by what the claim actually requires checking. It also compounds the [claim verification triage](claim-verification-triage.md) problem: a reviewer who defaults to the easiest-to-check evidence first, without separately asking whether that evidence can actually resolve the question, may exhaust their effort budget on a well-lit but irrelevant area while the claim's real substance goes unchecked.

## Recognizing It
- Verification effort concentrates on the specific data source, log, or document the reviewer already knows how to query, while alternative sources that would require learning a new tool or contacting an unfamiliar party go untried.
- A conclusion is reached that happens to be exactly what the readily available evidence could show, without the reviewer separately asking whether that evidence was actually capable of ruling out the alternative explanations.
- An investigation is described as thorough because of the *volume* of familiar-tool output examined, rather than because the right sources for the specific question were consulted.

## Verification Action
- Before starting to check a claim, ask where the evidence that could actually confirm or refute it would exist — independent of which sources are easiest for the reviewer to access — and treat a mismatch between "where I can look" and "where the answer would be" as a reason to seek out the harder source, not a reason to substitute the convenient one.
- When reviewing someone else's investigation or verification write-up, check whether the sources consulted were capable in principle of answering the specific question, not merely whether sources were consulted at all.
- Be specifically suspicious of a "the data doesn't show a problem" conclusion drawn only from the tools/sources routinely already in use — absence of evidence in a convenient source is not evidence of absence unless that source could actually have shown it.

## See Also
- [Confirmation Bias in Verification](confirmation-bias-in-verification.md)
- [Claim Verification Triage](claim-verification-triage.md)
- [Knowledge Bias in Verification](knowledge-bias-in-verification.md)
