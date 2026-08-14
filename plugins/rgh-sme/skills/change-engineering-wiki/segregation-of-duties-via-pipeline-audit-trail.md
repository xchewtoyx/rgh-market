---
type: concept
title: Segregation of Duties via Pipeline Audit Trail
description: >
  Regulated environments can satisfy segregation-of-duties requirements
  without a change approval board by combining mandatory peer review with
  an automated, immutable deployment pipeline audit trail.
sources:
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 7"
---

# Segregation of Duties via Pipeline Audit Trail

Regulated environments (PCI DSS, SOX, HIPAA, FISMA) require segregation of
duties: the person who makes a change cannot be the sole person who
authorizes it into production. This is commonly implemented as a change
approval board, but DORA research shows that path is achievable, and
performs better, via two automated mechanisms instead:

1. **[Peer review](peer-review-as-change-control.md)** — at least one
   non-author team member reviews and approves the change in version
   control.
2. **Automated deployment pipelines** — production changes are applied
   exclusively via an automated pipeline, which generates an immutable,
   audited trail recording the commit SHA, author, peer-reviewer approval,
   test execution results, and deployment timestamp.

The audit trail substitutes for a CAB's paper record: an auditor can
reconstruct exactly what changed, who wrote it, who approved it, and what
verification it passed, without a human gatekeeper ever having sat in the
deployment path.

This is a specific application of the pipeline's general [traceability](deployment-pipeline-traceability.md)
property — recovering what produced a given running artifact — aimed at a
compliance audience rather than a debugging one.
