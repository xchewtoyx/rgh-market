---
type: concept
title: Decision-Influence Concentration
description: >
  Adding people to a decision does not by itself add diversity of
  judgment — measure how concentrated real influence is across the
  room, not just how many people are in it.
sources:
  - title: "Drift into Failure: From Hunting Broken Components to Understanding Complex Systems"
    resource: "Drift into Failure (Sidney Dekker), ch. 7"
---

A room with more people in it is not automatically a room with more
diverse judgment — it depends on how much weight each person's voice
actually carries, not on the headcount. A junior participant who
defers completely contributes nothing to diversity even though they
are present and counted; a senior participant who dominates can make
a five-person decision behave, in practice, like a one-person one.

A concentration index makes this visible instead of assumed. Assign
each participant an estimated share `s` of real decision-making
influence (not formal seniority — actual weight in how the call gets
made) and compute the Herfindahl-style index `H = Σs²`. Because
squaring exaggerates large shares, `H` rewards genuinely distributed
influence and punishes domination even when it is dressed up as
consultation:

- Several roughly equal voices (say four people near 25% each)
  produce a low `H`, close to genuine diversity.
- One dominant voice at 80%, with the rest splitting the remainder,
  produces a high `H` close to a monopoly — even with several other
  people nominally "in the room."
- Adding a senior voice who takes over the room can *raise* `H` (less
  diversity) despite adding a person, while adding a participant who
  visibly defers barely moves it at all.
- Training or facilitation that deliberately flattens deference —
  explicitly inviting minority views, giving junior participants an
  earlier or protected turn to speak — can markedly lower `H` for the
  same headcount, which is the concrete, measurable effect that
  facilitation technique is trying to produce.

The number is a diagnostic, not a target to game: the point is to
notice when a decision that looks consultative is actually
concentrated, and to treat that as a specific, nameable gap rather
than a vague sense that "someone talks too much." It gives
[matching-seniority-in-the-room](matching-seniority-in-the-room.md)'s
compositional fix (avoid mixed-seniority rooms in the first place) a
way to check whether it worked, and complements
[group-risk-decision-biases](group-risk-decision-biases.md) — a group
whose stated position has polarized or drifted is worth checking for
high concentration first, since a monopolized room is one of the most
common ways an individual's view gets mistaken for the group's.
