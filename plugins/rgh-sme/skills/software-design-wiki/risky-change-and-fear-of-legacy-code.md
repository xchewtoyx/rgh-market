---
type: concept
title: Risky Change and the Fear of Legacy Code
description: >
  Avoiding structural change to minimize risk backfires — existing methods
  and classes just grow larger and harder to understand, and avoidance
  atrophies the very skill needed to change code confidently.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 1"
---

Mitigating the risk of a change means being able to answer three questions:
what changes do we have to make, how will we know we've done them correctly,
and how will we know we haven't broken anything? A common team anti-pattern
manages risk instead by minimizing the number of changes, new classes, or new
methods created — "if it's not broke, don't fix it," inlining new logic into
an existing method "where I can see it" instead of extracting it properly.
This avoidance strategy backfires: existing methods and classes just grow
larger and harder to understand over time, which is the opposite of reducing
risk.

The psychological framing matters: in a well-structured system, the process
of learning an area before changing it ends in calm confidence. In a poorly
structured one, it feels like "jumping off a cliff to avoid a tiger" —
hesitation, uncertainty about whether you're actually ready to make the
change. Avoiding change atrophies the skill of changing code (decomposing a
large class is easy if you do it regularly, hard and unfamiliar if you
don't), and breeds a compounding, often unconscious fear across a team — a
fear that only becomes visible in retrospect, once better techniques make it
fade.

"Just try harder" or "hire more people to scrutinize the code more" isn't a
real alternative: more analysis time doesn't tell you whether you actually
got the change right. The actual answer is tests and fast feedback — see
[characterization tests](characterization-tests.md) and
[edit and pray vs. cover and modify](edit-and-pray-vs-cover-and-modify.md).
