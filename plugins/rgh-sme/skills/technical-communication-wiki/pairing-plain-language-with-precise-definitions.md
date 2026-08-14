---
type: concept
title: Pairing Plain-Language and Precise Definitions
description: >
  State a technical definition twice in the same place — once as a plain
  sentence any stakeholder can parse, once as the exact formula or query
  a specialist can verify — rather than forcing every reader through
  whichever version wasn't written for them.
sources:
  - title: "Implementing Service Level Objectives: A Practical Guide to SLIs, SLOs, and Error Budgets"
    resource: "Implementing Service Level Objectives (Alex Hidalgo), ch. 15"
---

A technical definition often has to serve two readers at once in the same document: someone who needs to act on what it means, and someone who needs to verify exactly what it says. Rather than picking one register and forcing the other reader to translate, state the definition twice, deliberately, side by side: a plain-language sentence ("We will serve 200 responses within 500ms to 99.9% of requests") that any stakeholder — product, support, leadership — can read and immediately understand, and a precise, formal version (the exact query, formula, or specification) that a specialist can check line by line. Neither version replaces the other; the plain sentence would be too imprecise to implement against, and the formal version would be opaque to most of the document's actual readers.

This is a narrow, deliberate exception to the usual rule against restating the same fact twice in one document (see [cutting clutter](cutting-clutter.md)) — it isn't redundancy, because the two versions serve genuinely different reading tasks rather than repeating the same task twice. The test for whether a pairing like this earns its place: does the document have two audiences who need the same fact at two different levels of precision, and would either audience be poorly served by only the other version. Where that's true, writing both is cheaper than writing one and leaving one audience to reverse-engineer the other, or maintaining two separately drifting documents for the two audiences (see [maintaining and deprecating documentation](maintaining-and-deprecating-documentation.md)) — a single source containing both keeps them from silently diverging, since anyone editing the definition sees both forms in one place. Where a precise version already exists elsewhere and is kept current automatically (a live query, a generated value), link to it rather than restating a static copy that can go stale — see [choosing documentation types](choosing-documentation-types.md) on preferring generated reference material over hand-maintained copies wherever a generator can produce it accurately.
