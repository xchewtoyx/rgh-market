---
type: concept
title: Telling the Story of the System
description: >
  A team's ability to narrate its architecture aloud, in a few essential
  concepts, is a cheap diagnostic for shared understanding — and a
  persistent gap between what people say the system does and what the
  code actually does is itself a design smell worth acting on.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Michael C. Feathers), ch. 17"
---

Formal [architecture documentation](architecture-documentation-package.md)
answers "what did we decide and why" for someone who wasn't there. A
different, complementary question — "does the team currently share one
mental model of this system at all" — is cheaper to check and easy to let
go stale silently, especially once a system has been touched by enough
people over enough time that no single view of it is authoritative anymore.

**Telling the story of the system**: one person asks "what is the
architecture of this system?" and another must answer using only a
handful of core concepts, as if explaining it to someone who knows
nothing about it, then progressively layer in the next-most-important
facts only as asked. The discomfort of leaving things out is the point —
it forces a distinction between what's essential and what's merely
expedient, and the resulting simplified account becomes a shared
reference point rather than an exhaustive spec. A system that turns out to
be more complicated than its honest simplest story isn't necessarily
broken; real systems accumulate necessary complexity. What matters is
using the story as a live check: when two implementation choices are
otherwise comparable, prefer the one that keeps the team's honest story of
the system true, because a design that can no longer be told truthfully in
the team's own simplified terms has usually accumulated an unnoticed,
undocumented responsibility that a reader would need before trusting the
existing [architecture views](view-and-viewpoint.md) at all.

Two related lightweight techniques for surfacing where the shared model
has drifted from the code, both social rather than diagrammatic:

- **Naked CRC** — narrating a design using blank index cards as physical
  stand-ins for object instances (not classes), moved and overlapped on a
  table in real time to represent interaction and collection. The value is
  in the motion and narration, not in any artifact retained afterward.
- **Conversation scrutiny** — comparing the vocabulary people use when
  *talking* about a design against the vocabulary actually present in the
  code. A team that fluently discusses a "locking policy" while the code
  has no `LockingPolicy` anywhere is a concrete, checkable signal that the
  code hasn't been allowed to evolve toward the team's actual mental
  model, or that the mental model itself needs to be reconciled with what
  the code really does.

The underlying claim behind all three techniques is that architecture is
"too important to be left exclusively to a few people": a single embedded
architect can keep a personal model current, but if the rest of the team
doesn't share it, the code and the official architecture silently diverge
regardless of how good that one person's documentation is. These
techniques are a low-cost way to test, on an ongoing basis, whether the
team's shared understanding still matches the system — a narrower,
conversational counterpart to the [architectural reality
check](architecture-codex.md) that checks stated intent against code
directly, useful precisely because it costs nothing but a conversation and
can be run informally, at any time, without special tooling.
