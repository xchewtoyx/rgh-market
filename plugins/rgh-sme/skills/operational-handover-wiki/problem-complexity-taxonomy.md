---
type: concept
title: Problem Complexity Taxonomy
description: Classifying an operational task as simple, complicated, or complex to decide what kind of documentation and coordination approach it needs.
sources:
  - title: "The Checklist Manifesto: How to Get Things Right"
    resource: "The Checklist Manifesto (Gawande), ch. 3"
---

Not every operational task warrants the same documentation strategy. Before deciding how to document or run a procedure, classify it into one of three categories, because the wrong category leads to either under-documenting a genuinely unpredictable task or over-constraining a task that needs adaptive judgment.

## The Three Classes

- **Simple**: Highly predictable, governed by a standardized recipe. Once the technique is learned, following the same steps reliably reproduces success. A rigid, step-by-step [READ-DO checklist](runbook-checklist-design.md) fits this class well.
- **Complicated**: Composed of many simple sub-tasks, requiring multiple specialists to coordinate. Unanticipated issues at the boundaries between sub-tasks are common, so timing and cross-specialist coordination — not any single specialist's skill — is the main risk. This class needs both a process checklist for the sub-tasks and a [cross-specialist communication schedule](cross-specialist-communication-schedule.md) for the boundaries between them.
- **Complex**: Unique and non-repeatable enough that past experience does not guarantee the next instance goes the same way. Expertise is necessary but not sufficient — real-time adaptive judgment is required, and no fixed procedure can substitute for it. Documentation for this class should favor general guidelines and diagnostic entry points over rigid recipes (see the general-guidelines side of [Playbook Maintenance Tension](playbook-maintenance-tension.md)), and rely on [decentralized authority](decentralized-authority-for-complex-operations.md) for the operator closest to the situation to adapt.

## Applying This During Handover

When taking over a system, classify its recurring operational tasks into these three buckets before deciding how much documentation effort to invest in each. A task misclassified as simple when it's actually complicated will have a checklist that looks complete but omits the coordination points that actually cause failures. A task misclassified as complicated when it's actually complex will produce a checklist that gives operators false confidence that following steps in order is sufficient, when what the situation actually needs is judgment.
