---
type: concept
title: Omission Detection
description: The practice of identifying missing evidence, data points, or perspectives that make an otherwise factually accurate document misleading.
sources:
  - title: "The Chicago Guide to Fact-Checking, Second Edition"
    resource: "The Chicago Guide to Fact-Checking, Second Edition (Brooke Borel), ch. 2"
---
# Omission Detection

**Omission detection** is the practice of scanning a document for what is *missing* rather than what is present. A document can be entirely composed of verified, true statements, yet remain profoundly incorrect or biased because it omits critical context, counter-arguments, or conflicting data points.

## The Risk of Omission
Omission is a primary mechanism of [cherry-picking](cherry-picking.md) and false narratives. By presenting only the data that supports a desired outcome and omitting the rest, an author can lead readers to an incorrect conclusion without stating a single falsehood. In technical contexts, omitting known edge cases, system limitations, or failing test results can lead to unsafe designs. The same risk applies at the scale of a single citation: a summary or paraphrase of a source that accurately restates its finding while quietly dropping the source's own stated qualifications, caveats, or scope limits misrepresents that source, even though every sentence in the summary can be individually verified as accurate — see [claim scope calibration](claim-scope-calibration.md).

## Techniques for Detecting Omissions
Because missing information is by definition not on the page, detecting it requires active research and domain expertise:
- **Pre-Reading Context**: Before performing a line-by-line check of the document, the reviewer should read external, independent sources on the same topic to understand the broader context and see if the current draft stakes out an unusually narrow or biased framing.
- **Skeptical Reading**: The reviewer must look for logical leaps or gaps between assertions. If a conclusion is drawn without presenting the necessary intermediate evidence, this is a flag for potential omission.
- **Stakeholder and Expert Consultation**: Querying independent experts or stakeholders who represent alternative perspectives to identify details the author may have ignored.
- **Cross-Checking against System Limits**: In technical reviews, verify if the document addresses known failure modes, constraints, and standard operating boundaries.

## See Also
- [Defining Checkable Claims](defining-checkable-claims.md)
- [Argument-Level Verification](argument-level-verification.md)
- [Cherry-Picking](cherry-picking.md)
