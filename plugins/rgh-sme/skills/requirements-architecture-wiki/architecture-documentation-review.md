---
type: concept
title: Architecture Documentation Review
description: >
  Reviewing architecture documentation checks whether it is correct,
  complete enough, consistent, understandable, and fit for the
  stakeholders' actual tasks — before those gaps become design or
  integration failures.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan), ch. 11"
  - title: The DevOps Handbook
    resource: "The DevOps Handbook, 2nd Edition (Kim, Humble, Debois, Willis, Forsgren), ch. 8, ch. 18"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (ed. Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 7"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 12"
---

Reviewing architecture documentation is a distinct activity from
evaluating whether the design it describes is actually fit for purpose —
see the [Architecture Tradeoff Analysis
Method](architecture-tradeoff-analysis-method.md) for that. It is also a
distinct activity from writing it: the review asks whether the
documentation is correct, complete enough
for its purpose, internally consistent, understandable, and fit for the
tasks its stakeholders actually need to perform — catching ambiguity and
omissions while they're still cheap to fix, before they surface as design,
implementation, or integration failures.

The procedure: establish the review's purpose, scope, and participants;
distribute preparation material in advance; build a question set from
stakeholder concerns and quality goals rather than reviewing generically;
inspect individually first, then collectively; record issues with owners
and dispositions; follow up until closed. Question sets should cover
context and boundary, elements and relations, interfaces, notation,
consistency across views, [requirements
traceability](requirements-traceability.md), quality-attribute reasoning,
[rationale and decisions](architectural-decision-capture.md), and the
maintainability of the documentation itself. A review is not a passive
presentation — reviewers need a concrete problem to work and evidence in
the documentation to work it against, not just a walkthrough to nod along
to.

Three review lenses apply to any substantial document, each targeting a
different failure mode (often folded into code review for reference docs,
but worth separating explicitly for [design documents](design-document.md)
and external-facing material):

- **Technical review** (accuracy) — a subject-matter expert checks facts
  and technical claims; often the same person who would review the code.
- **Audience review** (clarity) — someone unfamiliar with the domain
  (a new teammate or an API customer) checks whether the document works
  without unstated assumptions.
- **Writing review** (consistency) — a technical writer or volunteer
  checks style, structure, and adherence to [documentation type by
  purpose](documentation-type-by-purpose.md).

High-profile or externally published documents should get more of these
types; even one ad hoc reviewer beats none. When documentation is tied
into the engineering workflow, it improves over time — implicit audience
review happens when readers file bugs against docs they actually use.

Concrete tactics that make "inspect individually first, then collectively"
actually happen rather than staying an aspiration: have each participant
submit their top concerns in writing, as complete sentences, before the
session — consolidated by the facilitator into the review's question set
— so the group discussion starts from independently-formed views instead
of the first person to speak anchoring everyone else. During the session
itself, work top-down through the documentation's own structure (for an
architecture package, that means confirming the most foundational
commitments — scope, boundary, the central structural decision — before
descending into subordinate details), since disagreement about a
foundational commitment makes review of everything built on top of it
premature.

Two lighter-weight variants of this same idea recur outside formal review
meetings. First, an informal design checklist applied whenever new
functionality is proposed, that explicitly requires stating **any
departure from prior established architectural patterns and the
justification for that departure** — this catches undocumented
architectural drift at the point it's introduced rather than at a later
formal review, and is a direct, ongoing check on
[conceptual integrity](conceptual-integrity.md). Second, review quality in an individual change (e.g. a pull
request) tracks less with reviewer thoroughness than with whether the
change itself documents its own rationale: what problem it solves, what
risks were identified, and what countermeasures were taken — a review
comment thread that later has an incident postmortem linked back into it
is doing double duty as both change rationale and an evolving record.
