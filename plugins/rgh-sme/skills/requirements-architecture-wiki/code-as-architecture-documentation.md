---
type: concept
title: Code as Architecture Documentation
description: >
  Infrastructure and application code, version history, and commit
  messages can serve as an always-current record of a system — but only
  for what has been explicitly expressed somewhere; automation cannot
  infer design meaning that was never stated.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 4"
  - title: "Infrastructure as Code, Patterns and Practices"
    resource: "Infrastructure as Code, Patterns and Practices (Rosemary Wang), ch. 1, ch. 2"
  - title: Living Documentation
    resource: "Living Documentation: Continuous Knowledge Sharing by Design (Cyrille Martraire), ch. 6, ch. 7"
---

For many purposes, code is a more useful record of a system than
separately written documentation, precisely because it cannot drift out of
date the way prose can — it is what actually runs. New team members can
browse it, reviewers can read commits, auditors can review the code plus
its version history. Version control specifically adds traceability: a
history of changes, who made them, and — if commit messages are written
well — context about why, including incident references and ticket links.
That last part is not automatic; it depends entirely on people writing
useful commit messages, which is why some teams make "commit messages must
capture why a change occurred" an explicit practice rather than an
assumed norm.

This is not a substitute for the rest of an [architectural decision
record](architectural-decision-capture.md): code communicates architecture
without relying on a stale wiki page, but many stakeholders who need
high-level context don't know the technology stack well enough to read it
out of the code directly. The common pattern is keeping ADRs written in a
lightweight markup format in source control, alongside the code they
govern, so both evolve together — and, where practical, generating
architecture diagrams and parameter references automatically from code,
wired into the delivery pipeline so the diagrams update whenever the code
does. A **living services diagram** is one instance of this: a
[context diagram](context-diagram.md) discovered from which services are
actually running and their declared metadata, rather than hand-maintained.

The hard limit on all of this automation: it can only surface design
meaning that has been expressed *somewhere* in the system — as a type, an
annotation, a schema, a naming convention. Automation cannot infer intent
that was never encoded anywhere, which is exactly why deliberate
[rationale capture](requirement-rationale.md) for the decisions that
matter most still can't be fully replaced by generating documentation from
code alone.
