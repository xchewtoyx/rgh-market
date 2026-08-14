---
type: concept
title: Fabrication Detection
description: Heuristics for catching invented facts, sources, or quotes, including the risk that a reviewer under-scrutinizes celebrated authors.
sources:
  - title: "The Chicago Guide to Fact-Checking, Second Edition"
    resource: "The Chicago Guide to Fact-Checking, Second Edition (Brooke Borel), ch. 1, 6"
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 1"
---
# Fabrication Detection

**Misinformation** is false information that spreads unwittingly; **disinformation** is false information spread intentionally. The distinction matters for response (a correction suffices for misinformation; a pattern of disinformation calls for more scrutiny of everything else the same source has produced), but both require the same detection discipline below regardless of intent, since intent is rarely knowable at the moment an error is first caught.

A determined fabricator who understands exactly how verification works can be very hard to catch — several journalism scandals involved writers who had *themselves* previously worked in fact-checking and knew how to construct matching fake sources, backup materials, and quotes. This makes fabrication one of the harder failure modes to defend against with process alone, but a few heuristics help.

## The "Too Good to Be True" Heuristic
Ask whether a story or result "sounds too good to be true." Treat an affirmative answer as a specific cue for heightened scrutiny and independent corroboration, rather than accepting a compelling narrative at face value because it is compelling.

## Worked Example: Investigative Fraud Detection
A 1998 medical paper alleging a link between a vaccine and a developmental condition rested on a sample of just 12 patients — too small on its face to support the sweeping conclusion drawn from it (see [claim scope calibration](claim-scope-calibration.md)). Independent investigative journalism subsequently found the underlying case histories didn't match the paper's own descriptions (several patients described as having the condition didn't; several described as previously healthy had pre-existing issues), and uncovered a large undisclosed financial conflict (payment from a lawyer building litigation against the same manufacturers, plus related patent filings) that gave the author a direct financial stake in the paper's conclusion. Most of the paper's own co-authors later retracted their support for its central interpretation, and the journal fully retracted the paper roughly a decade after publication, with the medical regulator finding the author guilty of misconduct. This demonstrates the specific combination that catches fabrication when a paper's stated methods look thin: check the raw case-level data against the paper's own summary of it, and check for undisclosed financial interests in the conclusion — see [evaluating scientific literature](evaluating-scientific-literature.md) for the conflict-of-interest check this illustrates. Despite total discrediting, the claim continued to circulate for decades afterward — a case of [correction effort asymmetry](correction-effort-asymmetry.md).

## Reputation Is Not a Verification Shortcut
Star or celebrated authors can hide behind their own reputations — institutional trust in a well-regarded contributor is exactly the condition fabrication exploits, and it can also mean their work gets routed to less-specialized reviewers or skips standard verification steps under time or social pressure. A reviewer must be willing to diplomatically flag errors even in famous or highly trusted contributors' work; see [knowledge bias in verification](knowledge-bias-in-verification.md) for the related failure of skipping checks on familiar-seeming material.

## Plagiarism Detection
- Watch for language in a draft that feels oddly familiar (possibly recalled from the reviewer's own background reading) or stylistically inconsistent with the rest of the document's voice.
- Automated plagiarism-detection tools are useful as a first pass, but flagged matches must still be verified manually, since false positives occur.
- A citation attached to closely-imitated phrasing does not clear plagiarism on its own — see [citation completeness check](citation-completeness-check.md) for why citing an idea doesn't license copying a source's expression.

## Verification Action
Fabrication is best caught by the same disciplines that catch honest error, applied without exception: trace every claim to an independently checkable source (see [defining checkable claims](defining-checkable-claims.md)), and treat a source's inability or unwillingness to produce underlying material as a red flag rather than an inconvenience to route around.

## See Also
- [Knowledge Bias in Verification](knowledge-bias-in-verification.md)
- [Defining Checkable Claims](defining-checkable-claims.md)
- [Citation Completeness Check](citation-completeness-check.md)
- [Evaluating Scientific Literature](evaluating-scientific-literature.md)
- [Correction Effort Asymmetry](correction-effort-asymmetry.md)
