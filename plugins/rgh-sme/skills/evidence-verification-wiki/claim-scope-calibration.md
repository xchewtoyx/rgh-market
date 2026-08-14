---
type: concept
title: Claim Scope Calibration
description: Matching the scope and confidence of technical assertions directly to the empirical reach of the underlying methodology.
sources:
  - title: "Writing Science"
    resource: "Writing Science (Joshua Schimel), ch. 18"
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 6"
  - title: "Working Effectively with Legacy Code"
    resource: "Working Effectively with Legacy Code (Michael C. Feathers), ch. 3"
---

# Claim Scope Calibration

**Claim scope calibration** is the discipline of constraining assertions to the precise boundary that underlying evidence and methods can defend. Overreaching claims undermine independent review and technical credibility.

## Methodological Boundaries
Every experimental or analytical method has structural limits:
- **Narrow conclusions over grand claims**: A small, empirically solid conclusion provides far more value than a broad assertion unsupported by data.
- **Methodological alignment**: Assertions must match the specific data a method yields. If a method cannot answer a broad question, the claim must be narrowed to match the defensible data.

## Study Population Generalizability
A finding's scope is also bounded by *who or what it was studied on*. Research drawing on the most convenient, cheapest-to-recruit subject pool available (often a narrow, non-representative population) can produce results that don't generalize to the broader population a claim implies it covers — a phenomenon studied in one narrow population can even vary dramatically in strength across different populations for reasons that aren't yet well understood. A claim's scope should be stated relative to the population actually studied, not the broader population the reader might assume it covers by default.

## Structural Disclosure of Limitations
Making limitations explicit allows reviewers to check assumptions and evaluate risk:
- **Disclose early**: Place methodological and interpretation constraints early in the technical presentation rather than burying them or leaving them unstated.
- **Explain design choices**: When a method introduces known limitations, document why the approach was selected and how design choices or [evidence triangulation](evidence-triangulation.md) mitigate the risk.
- **Constructive framing**: Disclose constraints candidly first, then present the defensible contribution that remains valid despite those boundaries.

## Defending a Narrowly Scoped Test Against "That Isn't Real Verification"
A verification method that deliberately isolates a narrow slice of a system (e.g., testing one component's logic against a stand-in for its collaborators, rather than the full live system) invites the objection that it doesn't prove the whole system works. That objection usually proves too much: no verification method — including exercising the real, fully-integrated system — can rule out every possible real-world combination of inputs and environment either. The correct response is not to abandon the narrow test but to state precisely what claim it *does* support (e.g., "this component behaves correctly given this collaborator interface") and treat that as one piece of a divide-and-conquer verification strategy, each piece narrowing where a future failure could be. A narrow test's value includes locating errors, not just detecting them: once a scoped check passes, a later failure elsewhere can be attributed with confidence to a different area.
