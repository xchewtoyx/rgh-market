---
type: concept
title: Defining Checkable Claims
description: The process of identifying and isolating testable assertions within a document to prepare them for verification.
sources:
  - title: "The Chicago Guide to Fact-Checking, Second Edition"
    resource: "The Chicago Guide to Fact-Checking, Second Edition (Brooke Borel), ch. 2"
  - title: "The Craft of Research, Fifth Edition"
    resource: "The Craft of Research, Fifth Edition (Booth, Colomb, Williams, Bizup, FitzGerald), ch. 6"
---
# Defining Checkable Claims

A **checkable claim** is any assertion for which concrete, independent steps can be identified to confirm its accuracy. Within the practice of technical and factual verification, identifying what requires checking is the first step toward validating a document's integrity.

## Operational Definition
An assertion is checkable if a reviewer can define a specific, reproducible path to verify it against primary data or authoritative sources. If no concrete steps can be formulated to test the assertion, it is either an opinion, a subjective interpretation, or an untestable assumption — or, if the underlying fact is real but simply has no observation channel yet, a case for [sensing as a verification precondition](sensing-as-verification-precondition.md) rather than an unavoidable dead end. The same discipline applies inside a running system, not just a document: see [invariant assertion placement](invariant-assertion-placement.md) for turning an assumed system invariant into an explicit, checkable claim.

A claim tied to a specific, locatable source is the clearest case of a reproducible verification path — see [source-grounded evaluation](source-grounded-claims-simplify-verification.md) for why checking a claim against its citation is both more accurate and more consistent across reviewers than judging the claim's truth unaided.

## Categories of Checkable Claims
To ensure thorough verification, a reviewer should extract and verify assertions across several categories:
- **Identifier Data**: Spelling of names, places, brands, and product titles.
- **Quantitative Assertions**: Numbers, dates, ages, measurements, unit conversions, and prices.
- **Technical Descriptions**: Scientific explanations, architectural specifications, and physical properties.
- **Relational Claims**: Descriptions of geographic locations, organizational hierarchy, and professional affiliations.
- **Representational Media**: Figures, tables, charts, and diagrams, along with their accompanying captions and labels.
- **Attributions**: Direct quotes, paraphrased statements, and historical anecdotes.

## Core Verification Techniques
- **Line-by-Line Claim Marking**: A structured process of going through a draft and physically or digitally highlighting every noun, number, and assertion. Systematically verifying each marked element prevents selective checking. A passage's real "fact surface" is consistently much larger than it first appears once broken down this finely — a single descriptive paragraph can easily contain well over a hundred separately checkable phrase-level assertions (names, sensory descriptions, implied comparisons) when segmented this way, not just its obvious headline numbers.
- **Verification of the Familiar**: Reviewers must check even the facts they are highly confident they already know. [Knowledge bias](knowledge-bias-in-verification.md) often leads reviewers to skip verifying obvious or repetitive assertions, which frequently harbor errors.
- **Triangulating the Claims**: Once claims are marked, they must be checked against primary sources and verified to ensure that they collectively support the document's [argument-level verification](argument-level-verification.md).

## Well-Formed Claims
A claim invites productive verification only if it is:
- **Specific** enough to check, rather than a vague statement of topic ("this system has performance issues" isn't a claim; "p99 latency exceeds 500ms under load X" is) — see the [negation test for vacuous claims](negation-test-for-vacuous-claims.md) for a quick diagnostic when a sentence resists this kind of pinning-down.
- **Significant**: worth verifying at all, as opposed to trivially true or too minor to matter to the document's conclusions.
- **Contestable**: a reasonable, informed reader could actually doubt it before seeing the evidence — a claim so obviously true it needs no support, or so purely subjective that no evidence could settle it, isn't a meaningful target for verification.
- **Proportionate to its evidence**: qualified/hedged where the evidence only partially supports it, not stated with more certainty than the evidence warrants (see [claim scope calibration](claim-scope-calibration.md) and [hedge words for uncertain claims](hedge-words-for-uncertain-claims.md)).

A claim disguised as settled certainty when the evidence only partially supports it is a distinct failure from a claim being outright false — flag both.

## See Also
- [Knowledge Bias in Verification](knowledge-bias-in-verification.md)
- [Argument-Level Verification](argument-level-verification.md)
- [Omission Detection](omission-detection.md)
- [Claim Type Taxonomy](claim-type-taxonomy.md)
