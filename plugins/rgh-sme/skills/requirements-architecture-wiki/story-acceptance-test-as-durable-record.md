---
type: concept
title: Story Acceptance Test as the Durable Requirement Record
description: >
  A user story is meant to be discarded after implementation; the story
  acceptance test built through team conversation is what actually
  persists as the record of what the system does.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise (Dean Leffingwell), ch. 10"
---

A common objection to agile's lightweight [user story](user-story.md)
practice is: if the story card carries almost no detail and is thrown
away once built, how does anyone later know what the system is actually
supposed to do? The answer is that the story was never meant to be the
durable artifact — its **acceptance test** is. The story is a deliberately
disposable placeholder for a conversation; the acceptance test that comes
out of that conversation is a black-box, business-domain-language check of
the story's conditions of satisfaction, and it is what keeps running
(ideally as automation) for as long as the behavior it checks still
matters. Discarding the story once it's built is safe specifically because
the acceptance test — not the story text — is doing the job of recording
the requirement going forward, functioning as living documentation and as
a regression guard against future changes at the same time.

This only works if the test is written to the same standard as any other
requirement: unambiguous and covering the real scenarios, which usually
means refining the story itself until it's concrete enough to produce a
test like that (a story that resists being turned into a clean
acceptance test is a sign the story needs rework, not that the test should
be sloppy). See [executable specification](executable-specification.md)
for writing that test precisely enough to run automatically, and [fit
criterion](fit-criterion.md) for the same discipline applied to a single
requirement statement rather than a whole story.

**Acceptance test-driven development (ATDD)** extends test-first practice
from unit tests up to this story level: the team writes the story's
acceptance test *before* writing the code that satisfies it. The reason
this is more than a process preference is economic — rediscovering or
reconciling a misunderstanding after code exists is never actually free,
so finalizing the team's shared understanding of required behavior by
writing the test first (rather than deriving the test from whatever got
built) removes that rework cost at the point it's cheapest to remove. This
is the story-level counterpart to the "Testable" clause of the
[INVEST criteria](invest-criteria-for-user-stories.md) — a story that
can't yield an acceptance test before coding starts is not yet ready to be
built.
