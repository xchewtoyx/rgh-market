---
type: concept
title: Conversational Vocabulary as a Documentation Diagnostic
description: >
  When the words people naturally use while talking through a system
  don't match the vocabulary its documentation or code actually uses,
  that mismatch is a reliable signal that the written artifact has
  drifted from the team's real mental model.
sources:
  - title: "Working Effectively with Legacy Code"
    resource: "Working Effectively with Legacy Code (Michael C. Feathers), ch. 17"
---

People describing a system out loud reach for whatever vocabulary actually matches how they think about it — and that vocabulary is worth deliberately comparing against the terms the system's own documentation or interface actually exposes, because a strong, sustained mismatch between the two is a reliable, checkable signal that something has drifted. If a team talks fluently and specifically about a concept — a named policy, a named role, a named workflow stage — but the artifact describing the system has no term for it at all, or splits it awkwardly across several unrelated terms, that's not a superficial labeling gap: it usually means the artifact was never updated to reflect an idea the team's own understanding has already settled on.

The diagnostic runs in both directions once the gap is found. Sometimes the fix is to bring the documentation's vocabulary into line with how people actually talk — naming the thing the team already has a name for, rather than continuing to describe it only in terms of its constituent mechanics. Other times, surfacing the gap reveals that the team's spoken mental model itself is ahead of, or subtly different from, what the system genuinely does — in which case the conversation is the thing that needs correcting, not the documentation. Either way, the mismatch itself is the useful signal; noticing it is what prompts the question "why isn't there a name for the thing we keep talking about" or "why do we keep calling this something the documentation doesn't say" — a question that's easy to never ask if the two vocabularies are never explicitly held up against each other.

This is the spoken-language counterpart to [precise and consistent naming](precise-and-consistent-naming.md): naming discipline is usually framed as getting the term right once and reusing it consistently in what's written down, but this technique catches the case where the term is already right in speech and simply hasn't made it into the artifact yet.
