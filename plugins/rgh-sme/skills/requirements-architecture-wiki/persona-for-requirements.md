---
type: concept
title: Persona for Requirements
description: >
  A persona is a detailed archetypal user profile used during requirements
  discovery to capture how different classes of user differ in
  capability, goal, environment, and usability need.
sources:
  - title: Mastering the Requirements Process
    resource: "Mastering the Requirements Process: Getting Requirements Right (Suzanne Robertson, James Robertson), ch. 5"
---

A persona, in requirements work, is a detailed archetypal profile of a
class of user — "experienced highway supervisor" versus "novice
maintenance worker" — built to make differences in capability, goals,
physical working environment, and usability constraints concrete and
specific rather than averaged away into one generic "the user."

The reason this belongs in [elicitation](requirements-elicitation-techniques.md)
rather than in design is that different user classes frequently need
different [non-functional requirements](non-functional-requirement.md),
not just different interface treatments — a novice user's usability
requirement (e.g. task completion without assistance after a fixed
training time) is a genuinely different, separately-verifiable requirement
from an experienced user's, and collapsing personas into one generic user
loses the distinction before it can even be stated as a
[fit criterion](fit-criterion.md).

Not every persona needs equal weight. A **primary persona** has needs that
can only be satisfied by an interface designed specifically for them; a
**secondary persona** also uses the system but can work through an
interface designed primarily for someone else. This distinction keeps
persona work bounded: the goal is discriminating just enough classes of
user to design correctly for each, not cataloguing every possible user of
the system — a system with several primary personas (e.g. a consumer and
a utility operator using the same platform for unrelated purposes) needs
genuinely distinct interfaces, while a support technician who can reuse
the consumer's interface is a secondary persona whose needs are noted, not
independently designed for. The same primary/secondary distinction applies
to non-human personas — an integrating device or downstream system can be
a "user" of an API with its own capability profile, worth capturing the
same way.
