---
type: concept
title: User Story
description: >
  A user story is a brief, deliberately incomplete placeholder for a
  requirement — "As a [role], I want [activity] so that [benefit]" — that
  defers detailed specification to a later conversation rather than trying
  to capture it up front.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise (Dean Leffingwell), ch. 6"
---

A user story is the agile-team-level replacement for a written
[atomic requirement](atomic-requirement-shell.md): a short statement of
intent — "As a `<role>`, I want `<activity>` so that `<business value>`" —
kept deliberately brief and detail-free. The role names *who* needs this
(and lets the same product serve different [personas](persona-for-requirements.md)
differently); the activity is the requirement itself; the benefit clause
keeps the team anchored to the business [rationale](requirement-rationale.md)
rather than to the activity as an end in itself.

Where a Volere Snow Card front-loads a requirement's detail into fixed
fields, a user story defers that detail on purpose, via the three Cs:

- **Card** — the brief written statement, small enough to fit on an index
  card (physical or digital).
- **Conversation** — the discussion between the team and whoever owns the
  requirement that fills in the actual behavior; the card is "a promise for
  a conversation," not the specification itself.
- **Confirmation** — the acceptance criteria that both sides agree
  constitute "done." Acceptance criteria are conditions of satisfaction,
  not the same thing as functional or unit tests: criteria state what
  satisfies the story's intent; tests go on to cover every functional
  flow, exception path, and boundary condition needed to verify it. The
  card gets discarded once built, but the resulting [acceptance test is
  the durable record](story-acceptance-test-as-durable-record.md) of what
  the story actually committed to.

This makes a story closer to a *placeholder* for a requirement than a
requirement fully specified in writing — appropriate when the team and the
requirement's owner can have the conversation quickly and cheaply, and a
poor substitute for a written [fit criterion](fit-criterion.md) when that
conversation can't happen (a remote vendor, a compliance auditor, a future
maintainer with no access to the original team). See [good-enough
requirements](good-enough-requirements.md) for the general trade-off this
technique makes concrete: a story is that trade-off's agile expression,
betting on cheap, fast conversation over expensive, front-loaded
completeness.

Story quality is checked against the [INVEST
criteria](invest-criteria-for-user-stories.md); stories too large or too
uncertain to satisfy INVEST are decomposed further — see [story splitting
patterns](story-splitting-patterns.md) and, for stories too uncertain to
estimate at all, [spike](spike-story.md).

Stories written in isolation have a real limitation once a system is
genuinely composed of multiple actors, subsystems, or cooperating
applications: a card carries no situational context on its own, and
nothing forces the team to think through the edge cases that make up most
of the actual work. See [use case as a source of contextualized
stories](use-case-as-story-source.md) for how a use case supplies that
missing context and generates a coherent set of stories from it, rather
than leaving each story to stand alone.
