---
type: concept
title: Telling the Story of the System
description: A live exercise where one person must explain a system's architecture starting from the barest essential summary and adding detail only as needed, forcing the team to separate what's essential from what's merely expedient.
sources:
  - title: "Working Effectively with Legacy Code"
    resource: "Working Effectively with Legacy Code (Feathers), ch. 17"
---

A structured conversation exercise for building shared architectural understanding: one person asks "what is the architecture of this system?" and the other must answer using only a small handful of core concepts — as if explaining it to someone who knows nothing about it — then progressively add the next-most-important fact only as the conversation calls for it. The discomfort of deliberately leaving things out is the point: it forces whoever is telling the story to separate what's actually essential to understanding the system from what's merely expedient detail that happened to end up in the implementation.

## Why This Beats a Written Architecture Document

A diagram or document tends to flatten everything to the same level of importance, because whoever wrote it optimized for completeness rather than for what a newcomer actually needs first. The live, incremental version can't do that — it has to commit to an ordering, starting from what genuinely matters most, and a listener can push back in the moment ("wait, why does it also need X?") in a way a static document can't respond to. The resulting simplified story becomes a working mental model the team can reuse: a roadmap for a newcomer, and a way of making a complicated system feel less intimidating without pretending it's simpler than it is.

## Using the Story to Guide Design Decisions

Once a team has an honest, shared "story" of the system, it becomes a tiebreaker for design decisions: when two implementation choices are otherwise comparable, prefer whichever one keeps the team's story of the system true, rather than the one that quietly adds an exception the story would have to grow a new clause to cover. A component whose existence can't be worked into the story without contorting it is a signal that it doesn't belong where it currently lives, not just a documentation gap.

## A Standing Check: Does the Team's Vocabulary Match the Code?

The same instinct extends into an ongoing discipline, not just a one-time exercise: pay attention to the vocabulary people naturally reach for when *talking* about the design, and compare it against the vocabulary actually present in the code. A team that fluently discusses a "locking policy" in conversation while implementing it as raw counters bumped inline in arrays has let its shared mental model and its code drift apart — usually because the code was never allowed to evolve toward how the team actually thinks about it. When conversation and code diverge like this, treat it as a prompt to bring the code's vocabulary back in line with the story, not as a merely cosmetic naming complaint.

## Why This Matters for Handover

The story draws on whichever [structural view](structural-views-for-onboarding.md) — module, runtime, or deployment — the current question calls for; it is the narrative connecting those views, not a substitute for any of them. Architectural understanding that lives only in a few people's heads doesn't survive their departure, and a single dedicated "architect" role doesn't fix this unless that person stays embedded in day-to-day work — otherwise the code and the official architecture silently diverge until the architect's own mental model stops matching what's actually running. Getting the whole team able to tell a consistent, honest story of the system — practiced and refreshed periodically, not written once and filed away — is what makes the architecture something a newcomer can actually inherit, rather than something only reconstructable by asking around for whoever still remembers.
