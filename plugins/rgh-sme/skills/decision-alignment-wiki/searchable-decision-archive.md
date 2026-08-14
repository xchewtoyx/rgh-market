---
type: concept
title: Searchable Decision Archive
description: >
  Publish decision records centrally and make them searchable
  so a future similar decision starts from what was already
  learned instead of re-litigating it from scratch.
sources:
  - title: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations"
    resource: "The DevOps Handbook (Gene Kim, Jez Humble, Patrick Debois, John Willis, Nicole Forsgren), ch. 19"
---

A decision record that only lives in a meeting or a private
document does nothing for the next person who hits the same
question. Two habits determine whether it does:

- **Central, searchable location.** When decision and review
  documents are kept in one place everyone can search — not
  scattered across ad hoc wiki pages, chat threads, or
  personal drives — teams that face a familiar-sounding
  problem read the closest prior record first, before
  re-deriving the answer. Purpose-built tooling for this
  (structured fields, tags, linked follow-up tickets) measurably
  increases how often records get written at all, especially
  for the smaller, easy-to-skip decisions that would otherwise
  go undocumented.
- **Publish, don't just retain.** Some organizations make
  records genuinely public, sanitized where necessary; even
  internal-only publication with organization-wide visibility
  is what makes "search first" a viable habit rather than
  something only the original team can do.

This is what makes
[judgment-pre-commitment](judgment-pre-commitment.md) and
similar defensibility practices pay off over time: a decision
recorded with its reasoning is available to whoever revisits
the topic later, so the question can be answered by pointing
at the record instead of re-running the whole alignment
process. Feed each decision's follow-up work through
[action-item-closure-tracking](action-item-closure-tracking.md)
so the archive shows not just what was decided but whether it
was actually carried out.

**Distinguish confirmed-fresh from merely-untouched.** A record's
age alone does not say whether it still reflects the current
decision — an old record nobody has looked at recently and an
old record that was checked last month and found still correct
look identical if the only timestamp tracked is when it was
first written. Increment a "last reviewed" date on every
scheduled revisit, even when the revisit concludes with no
change, so a reader can tell "reviewed recently and still
holds" apart from "nobody has revisited this in years." Pair
this with a standing revisit schedule declared on the record
itself (e.g. monthly while new, stretching to yearly once
proven stable) — a scheduled check-in, even a two-minute one
that changes nothing, is what keeps the archive trustworthy
enough that people actually read it before re-deciding.
