---
type: concept
title: The Completeness-Accuracy-Clarity Tradeoff
description: >
  Documentation quality has three competing dimensions — completeness,
  accuracy, and clarity — and a good document optimizes whichever
  dimension matches its single purpose rather than maximizing all three.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 12"
---

No document maximizes completeness, accuracy, and clarity at once. More completeness often costs clarity; exhaustive accuracy on edge cases can bury the common path; clarity on a genuinely complex topic may require simplifying away some strict accuracy. A **good document is one doing its intended single job well**, not one scoring highest on every axis simultaneously.

Match the tradeoff to the type. **Reference documentation** should lean toward completeness — callers need exhaustive coverage even if the page is dense — while still using [scan-friendly structure](scan-friendly-function-comments.md) so seekers are not lost in it. **Conceptual documentation** should lean toward clarity, augmenting reference material rather than replacing it; some duplication and even some sacrificed edge-case precision are acceptable when they help a reader build a mental model (see [choosing documentation types](choosing-documentation-types.md)). **Landing pages** should optimize organization and minimal discussion — see [landing pages as traffic cops](landing-pages-as-traffic-cops.md). A common quality failure is importing design decisions or implementation rationale into API reference because the writer finds them interesting; those belong in design documents or implementation comments instead, mirroring the API-versus-implementation split in code.

The practical improvement rule: focus on **audience needs for this document's purpose**, not on everything the writer knows about the system. See [layered editing passes for documentation](layered-editing-passes.md) for a complementary editing order that tackles accuracy, completeness, structure, and clarity in separate passes rather than collapsing the tradeoff into one undifferentiated rewrite.
