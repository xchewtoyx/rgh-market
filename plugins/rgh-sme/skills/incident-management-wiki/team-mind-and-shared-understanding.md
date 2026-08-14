---
type: concept
title: Team Mind and Shared Understanding
description: Treating a response team as a cognitive unit with its own working memory, attention, and blind spots, and the specific failure where one member's correct knowledge never reaches the group.
sources:
  - title: "Sources of Power: How People Make Decisions"
    resource: "Sources of Power: How People Make Decisions (Gary Klein), ch. 14"
---

A team facing an incident can be usefully studied as a single cognitive
unit — with its own working memory (what's currently being discussed),
long-term memory (information that needs to be deliberately duplicated
across more than one person or it's lost when that person leaves the
channel), and limited attention (the team, like an individual, can really
focus on only one thing at a time). Three levels of team knowledge matter,
and the gaps between them are where failures live:

- **Behavior**: what the team visibly does — directly observable.
- **Collective consciousness**: what's actually been said out loud and
  shared among the group.
- **Preconscious**: information an individual member holds but has never
  actually voiced to the rest of the team.

The dangerous case is when a piece of correct, safety-relevant information
sits in one person's preconscious and never surfaces into the team's
collective consciousness — nobody consciously withheld it, it simply never
came up, and no one else knows to ask for it. In one studied case, a
technical detail one specialist knew (a component wasn't actually available
despite general assumption otherwise) never got voiced, and other team
members made a decision believing the opposite — the team's shared,
acted-upon understanding was wrong even though the correct information was
present in the room. This is a sharper, sharper failure mode than a
simple communication breakdown: it's not that someone spoke and wasn't
heard, it's that the accurate answer to a question no one happened to ask
never got said at all. The practical countermeasure is the same discipline
behind [CAN reports](can-report.md) and a live [incident state
document](incident-state-document.md): actively pull status from each
function rather than assuming silence means agreement, and explicitly poll
people who hold specialized knowledge rather than waiting for them to
volunteer it.

## Team maturity

A team's shared cognition develops along recognizable stages, similar to
how an individual's does: basic competencies and routines become automatic
first; a shared **identity** develops next (members start thinking in terms
of what the *team* needs, not just their own assigned task — an immature
team's members resist context ["just tell me what to do"] while a mature
team's members actively want overall status so they can compensate for
each other); only once competency and identity are established does the
team gain the attentional slack for higher-order **cognition** (shared
situation understanding, a realistic time horizon, and comfort acting on
incomplete information) and eventually **metacognition** — noticing when
its own process is breaking down and correcting it.

A concrete diagnostic sign of immaturity: a leader who abandons their
coordinating post to personally execute a task (a real case shows a crisis
manager leaving his command position to hand-write and proofread a status
message himself) — at that moment the team effectively has no leader,
whether or not anyone realizes it yet. Compare a fireground commander who
built a deliberate personal discipline against his own impulse to jump into
hands-on rescue work: he carried a milk crate to every fire specifically to
have a physical, fixed command post, keeping a foot on it at all times so
his crew could always find him for a decision. Command structure only works
if the commander stays findable — see [command
presence](command-presence.md) and [span of control](span-of-control.md)
for the structural side of the same discipline.

A team's own sense of reaction time also needs to be realistic: a crisis
team that berated itself for a security response "having no effect" after
only 31 minutes had simply never worked out that assembling and moving
real personnel takes several hours end to end — the team was, in effect,
grabbing at where the situation used to be rather than where it currently
was. Knowing your own team's actual assembly and execution latency (see
[mean time to assemble](mean-time-to-assemble.md)) is a precondition for
setting realistic expectations mid-incident, not an afterthought.

Over-control is an equally real failure mode as under-control: a leader who
interrupted an already-overloaded team every nine minutes for open-ended
status "caucuses" — without a clear end signal, and without regard for
whether people were mid-task — degraded performance as badly as a team with
no coordination discipline at all. The fix in both directions is the same:
a defined, bounded briefing cadence (an [operational
period](unified-command.md)) that people can plan around, not an
improvised interruption pattern in either direction.
