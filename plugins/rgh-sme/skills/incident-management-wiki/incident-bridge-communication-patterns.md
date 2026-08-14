---
type: concept
title: Incident Bridge Communication Patterns
description: The four deliberate speaking patterns an incident commander uses to control an open communication channel, and why polling for support beats seeking consensus.
sources:
  - title: "Incident Management for Operations"
    resource: "Incident Management for Operations (Rob Schnepp, Ron Vidal, Chris Hawley), ch. 3"
---

A conference bridge (or equivalent incident channel) gives everyone equal
access to speak, which means it degrades into noise unless the [incident
commander](incident-command-system.md) deliberately controls the flow. Four
patterns cover most of what an IC needs:

1. **IC to single resource**: isolate one person or function by name,
   silencing or standing by everyone else — e.g., "Database, stand by,"
   acknowledged with "Copy, database standing by."
2. **IC to group**: a general briefing or open question addressed to
   everyone at once, used to disseminate information or kick off broader
   discussion.
3. **SME to SME within a bounded group**: the IC deliberately opens a
   time-boxed discussion among a subset — for example, forming a database
   group under a [group leader](incident-command-system.md) and giving it
   ten minutes to converge on an answer.
4. **Broader heterogeneous discussion**: the IC opens the floor to a wider,
   mixed group (multiple functions, an outside vendor) with explicit ground
   rules and a time box.

A directive on any of these channels should name a specific person or
function rather than a vague "can somebody," state a clear objective and
time frame, and require the receiver to acknowledge and repeat it back.
Communication-medium quality follows a rough ranking — in-person, then
video, then voice, then text last — because text strips out the tone and
hesitation cues a trained commander listens for to judge whether a response
is confident or guessed.

**Seeking support, not consensus** is the deliberate alternative to letting
a group vote its way to a plan: the IC polls each relevant SME explicitly
("Database, do you support the plan?") rather than asking an open "does
everyone agree," because asking about disagreement surfaces objections
faster than asking for affirmation, and a weakly voiced "I support the plan"
is itself a signal worth probing. A plan that some SMEs privately prefer
differently is not the same as a plan that is wrong — 100% agreement isn't
the bar, and treating "different" as "wrong" is what turns support-seeking
back into slow consensus-seeking. Periodic [CAN
reports](can-report.md) give the IC a structured way to re-summarize status
and re-poll support as the incident progresses.
