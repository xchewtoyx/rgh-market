---
type: concept
title: Evidence Triangulation
description: Verifying claims by cross-checking them across multiple independent sources to avoid circular sourcing and aggregation errors.
sources:
  - title: "The Chicago Guide to Fact-Checking, Second Edition"
    resource: "The Chicago Guide to Fact-Checking, Second Edition (Brooke Borel), ch. 4-5"
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 5"
  - title: "The DevOps Handbook, 2nd Edition"
    resource: "The DevOps Handbook, 2nd Edition (Kim, Humble, Debois, Willis, Forsgren), ch. 23"
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th Edition (Len Bass, Paul Clements, Rick Kazman), ch. 23"
---
# Evidence Triangulation

**Evidence triangulation** is the process of cross-checking a claim against multiple independent sources to confirm its validity. This technique is especially critical when primary sources are unavailable or when dealing with highly complex or disputed claims.

## The Rule of Independent Triangulation
To establish a fact using secondary sources, a reviewer should look for a minimum of **three independent sources** that corroborate the claim. 

Crucially, these sources must be *truly independent*. A major failure mode in research is **circular sourcing** (or aggregation propagation), where multiple outlets or documents report the same statistic, but all of them are merely copying from a single, original, unverified (or incorrect) source.

## Triangulation Checklist
To ensure true triangulation:
- **Trace the Pedigree**: For every source, trace its bibliography or citations back to the origin. If Source A, Source B, and Source C all trace back to a single whitepaper from 2018, they represent only *one* source of evidence, not three.
  - **Named failure mode: zombie statistics** — a number repeated so often it becomes detached from any traceable, checkable source, yet keeps circulating because each new citer simply cites the previous one rather than the original data. Tracing a real zombie statistic's genealogy has taken researchers backward through a chain of several successive secondary citations before dead-ending at an editor's vague memory of unrelated course notes — with the eventual original source, once found, turning out to support a substantively different claim than the one now in circulation. Once a zombie statistic is entrenched, even the original data's own creator can struggle to correct the record. Tracing a source's full citation chain to its origin, rather than stopping at the nearest citation, is the only reliable defense.
- **Vary the Source Types**: Triangulate using different kinds of evidence. For example, combine a user interview (qualitative) with system metrics (quantitative) and a third-party audit report (independent document) to build high confidence.
  - Independence has to be genuine, not just nominal: two checks that both draw on the same upstream data feed will fail together if that feed is corrupted, even though they look like two separate sources on paper — see [default-negative values masking missing signal](default-negative-masks-missing-signal.md) for a documented case where a held-out validation set failed to catch a training-data corruption because it drew on the exact same broken pipeline as the training data itself.
  - This applies to verification *methods*, not only sources: a single control catches only the failure modes it was designed to catch. A documented real-world case: a bank's code-review and change-approval process failed to catch a deliberately planted backdoor because the perpetrator had the means, motive, and opportunity to make the malicious change look legitimate on review — the fraud was instead caught by an unrelated, independent method (ongoing operational monitoring noticing an anomalous pattern of activity). No single verification method should be trusted as sufficient on its own for a high-stakes claim; independent methods that fail in different ways are what catch what any one method misses.
  - Another documented case, from software architecture analysis: a static structural-dependency analysis of a codebase showed a sparse dependency matrix, suggesting low coupling and low architecture debt. Overlaying an independently-derived data source — which files were historically committed together in version control — revealed a dense web of coupling invisible to the structural view alone (files with zero structural relationship that nonetheless changed together repeatedly), matching what the project's own developers had already been experiencing as high change cost. Structural analysis and change-history analysis fail to detect different kinds of coupling, so relying on either alone would have produced a confidently wrong conclusion.
- **Identify Discrepancies**: If sources conflict, do not simply take the majority opinion. Investigate *why* they differ (e.g., different measurement methodologies, time-of-day variations, or geographic constraints).

## "Common Knowledge" Is Not Exempt
Writers often wave off a claim as "common knowledge" to avoid sourcing it — this is a trap. The old adage applies: "if your mother says she loves you, get a second source." A claim's apparent obviousness is not evidence it is currently true; even "Washington DC is the US capital" is only true from 1800 onward (Philadelphia held that role until then), so a claim tied to an earlier era still needs the era-appropriate fact checked, not the modern default assumed. For everyday identifier-level facts (names, spellings, dates), two or three high-quality independent sources are generally an acceptable floor even without a primary source; more consequential or disputed claims warrant the full three-independent-source rule above.

Independence can also be faked deliberately rather than merely coincidental — see [coordinated inauthentic amplification](coordinated-inauthentic-amplification.md) for bots and sockpuppets manufacturing the appearance of multiple corroborating sources from a single origin.

## See Also
- [Primary vs. Secondary Sources](primary-vs-secondary-sources.md)
- [Defining Checkable Claims](defining-checkable-claims.md)
- [Coordinated Inauthentic Amplification](coordinated-inauthentic-amplification.md)
