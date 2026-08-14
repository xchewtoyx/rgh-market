---
type: concept
title: Essence of the Business Work
description: >
  Stripping a stated need down to the core business activity that would
  still exist even with perfect, instantaneous, free technology reveals
  the true requirement underneath a described solution.
sources:
  - title: Mastering the Requirements Process
    resource: "Mastering the Requirements Process: Getting Requirements Right (Suzanne Robertson, James Robertson), ch. 6, ch. 7"
---

Stakeholders usually describe what they need in terms of a familiar
current solution or a specific technology — "print a report at midnight,"
not the underlying reason a report is needed at all. "Thinking above the
line" means deliberately stripping away the implementation mechanisms
(the paper form, the specific database, the particular UI button) to find
the **essence of the work**: the business activity that would still exist
even if technology were perfect, instantaneous, and free.

The core technique for reaching it is repeatedly asking "why do you
perform this step?" (a root-cause technique) until the answer is a
genuine business driver rather than another description of current
mechanics. This also separates two things that get described in the same
breath but are not the same: a **business rule** (a policy set by business
governance or law, e.g. a legal toxicity limit) versus a **technology
constraint** (how the work happens to be done right now, e.g. "reports
print on a particular printer at midnight"). Only the business rule
belongs in a requirement; the technology constraint describes the current
solution, which is exactly what requirements discovery is trying to look
past — see [requirement vs. design decision](requirement-vs-design-decision.md).

Finding the essence also guards against "paving the cow path": automating
an existing bad process exactly as it stands, instead of using the
opportunity to re-frame a constraint as something that could be solved
differently. Every candidate requirement discovered this way should still
be checked against the [project goal](project-blastoff.md) set at the
start of the project, to prevent scope creep from features that don't
actually serve it.

The same technique applies one level down, inside a single interview,
whenever a stakeholder volunteers a feature request instead of a need:
asking "if you had that, what would it do for you?" ladders back from the
requested solution to the underlying need in the same way "why do you
perform this step?" ladders back to the underlying business activity.
Capturing the answer to that question, not the originally requested
feature, is what keeps multiple solution paths open — "I don't want to
type out a long title" still permits voice search, autocomplete, or
something neither party has thought of yet; "add voice search" forecloses
all but one.
