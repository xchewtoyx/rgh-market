---
type: concept
title: Conversation Scrutiny
description: >
  Compare the vocabulary a team naturally uses when talking about a design
  against the vocabulary actually present in the code — a strong mismatch
  means either the code hasn't evolved toward the team's mental model, or
  the model itself needs to shift.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 17"
---

Pay attention to the vocabulary people naturally use when *talking* about a
design, and compare it against the vocabulary actually present in the code.
Worked anecdote: an otherwise experienced, competent team designing a
multi-threaded locking scheme kept talking fluently about a "locking
policy" while about to implement it as raw counters bumped inline in
arrays — until someone proposed literally naming a `LockingPolicy` class
with methods matching the language already being used in conversation.
"There is something mesmerizing about large chunks of procedural code: They
seem to beg for more [of the same]" — the pull toward the familiar
implementation style can override language the team already agrees is the
right conceptual model.

General principle: **"if there isn't a strong overlap between conversation
and code, it's important to ask why"** — usually either the code hasn't
been allowed to evolve toward the team's actual mental model, or the team's
mental model itself needs to shift. The goal is to put some of that
understanding into the code, since conversational language is itself an
attempt to make a design understandable to another person — the same
instinct [naming as documentation](naming-as-documentation.md) applies to
individual identifiers, applied here at the scale of a whole class or
subsystem.
