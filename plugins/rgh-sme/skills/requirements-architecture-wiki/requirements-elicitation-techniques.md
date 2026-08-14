---
type: concept
title: Requirements Elicitation Techniques
description: >
  Trawling for requirements combines several active investigation
  techniques — apprenticing, interviewing, workshops, brainstorming, mind
  mapping, and artifact analysis — chosen to surface tacit knowledge
  stakeholders don't think to state.
sources:
  - title: Mastering the Requirements Process
    resource: "Mastering the Requirements Process: Getting Requirements Right (Suzanne Robertson, James Robertson), ch. 5"
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 19"
  - title: Deciphering Data Architectures
    resource: "Deciphering Data Architectures (James Serra), ch. 15"
---

"Trawling" is the active process of discovering how a business actually
works and what it actually needs, as opposed to passively transcribing
what one stakeholder says in one conversation — see [requirements
discovery vs. gathering](requirements-discovery-vs-gathering.md). The
standard techniques, used in combination rather than alone:

- **Apprenticing / observation** — sitting with a hands-on user and
  watching them work, asking clarifying questions as you go. Reveals tacit
  knowledge that users have stopped noticing and won't mention unprompted.
- **Interviewing** — structured or semi-structured conversation. Ask
  open-ended questions, focus on the underlying business goal rather than
  the current UI, and watch for the analyst's own assumptions leaking into
  the questions. A specific tactic worth naming: after the interviewee
  explains something, repeat it back in your own words and ask "is that
  right?" rather than nodding along — this surfaces both confirmation (you
  understood correctly) and misunderstanding (you didn't) productively,
  instead of letting a wrong assumption ride silently to the next question.
- **Requirements workshops** — facilitated sessions bringing users, SMEs,
  developers, and sponsors together, effective for resolving
  cross-department conflicts quickly rather than discovering them late.
- **Brainstorming** — generating candidate capabilities without immediate
  filtering or criticism. Generation is only half the technique: see [idea
  reduction after brainstorming](idea-reduction-after-brainstorming.md) for
  turning a raw idea set into a workable candidate list afterward.
- **Mind mapping** — visual capture of concepts and their relationships as
  they emerge during interviews or workshops.
- **Shadowing and artifact analysis** — inspecting the physical forms,
  reports, spreadsheets, and legacy schemas people actually use, to trace
  what data is really needed versus what a person merely says they need.
- **Prototyping** — having end users build a rough version of the
  deliverable themselves (e.g. sample reports with the reporting tool
  that will actually be used), rather than only reacting to one the
  analyst produced. Most end users are unaware of a tool's full
  capabilities, so a hands-on build during elicitation surfaces both
  requirements the user wouldn't have thought to state and features the
  eventual solution should expose more prominently than the user assumed
  possible. See [requirements are discovered, not
  gathered](requirements-discovery-vs-gathering.md) for why a concrete
  candidate — whether analyst-built or user-built — reliably surfaces
  requirements an abstract conversation does not.

Which technique surfaces which kind of gap differs: observation catches
what people do but don't think to mention; workshops catch conflicting
requirements across stakeholder groups; artifact analysis catches data
needs nobody remembers to state verbally. Choosing one technique and
skipping the others tends to leave exactly the kind of gap that technique
was suited to catching. See also [persona for
requirements](persona-for-requirements.md) for a complementary technique
aimed specifically at capturing how different classes of user differ from
each other, [story-based elicitation
questions](story-based-elicitation-questions.md) for a specific,
research-backed refinement of the interviewing technique above, and
[context-free interview template](context-free-interview-template.md) for
a fixed question structure that works across domains, reducing how much
the interviewer's own framing shapes what gets discovered.

For eliciting requirements specifically for a decision-support interface —
what judgments the task actually requires and which cues experts rely on
to make them — see [decision requirements
analysis](decision-requirements-analysis.md).

For eliciting requirements specifically for an analytical data model, see
[dimensional modeling's four-step
elicitation](dimensional-modeling-four-step-elicitation.md) — a
domain-specialized workshop sequence (business process, grain, dimensions,
facts) that plays the same role here that the Quality Attribute Workshop
plays for quality-attribute requirements. See [data-driven vs.
reporting-driven requirements
analysis](data-driven-vs-reporting-driven-requirements-analysis.md) and
[proactive requirements analysis](proactive-requirements-analysis.md) for
the higher-level strategic question a data-warehouse project has to settle
first — which source of evidence (operational source data, existing
reports, or neither) requirements discovery draws on — before any of these
workshop techniques run.

A specific interviewing tactic for the common case where a stakeholder
insists they don't know a quantitative target: offer a deliberately
absurd bound first ("would 24 hours be an acceptable response time?"),
provoke the predictable "no," and progressively tighten ("1 hour? 5
minutes? 10 seconds?") until they land on something they can actually
live with. This extracts a usable range even from someone who genuinely
believes they have no opinion, and the range itself is often enough to
drive very different design choices — a 24-hour, 10-minute, 10-second, and
100-millisecond response requirement each imply a completely different
architecture. See [Quality Attribute Workshop](quality-attribute-workshop.md)
and [business-goal-driven requirements](business-goal-driven-requirements.md)
for structured, multi-stakeholder workshop formats built on the same
elicitation discipline, specialized for surfacing [architecturally
significant requirements](architecturally-significant-requirement.md).
