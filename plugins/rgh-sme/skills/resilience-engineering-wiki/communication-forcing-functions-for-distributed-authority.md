---
type: concept
title: Communication Forcing Functions for Distributed Authority
description: >
  Under genuine complexity, centralised command breaks down; pushing
  decision authority to the periphery only works safely if paired with an
  explicit, mandatory mechanism that forces cross-boundary communication.
sources:
  - title: "The Checklist Manifesto: How to Get Things Right"
    resource: "The Checklist Manifesto (Gawande), ch. 3-4, 8"
  - title: The Fearless Organization
    resource: "The Fearless Organization (Edmondson), ch. 6"
---

Centralised, top-down decision-making is well matched to
[simple and complicated problems](simple-complicated-complex-problem-taxonomy.md):
a plan made in advance can specify what should happen, because the situation
is predictable enough for a plan to hold. It fails on complex, fast-moving
problems for a structural reason, not a competence one: information from the
periphery cannot reach the centre and come back as a decision fast enough,
so authority has to move to wherever the current, ground-truth information
already is.

The 2005 Hurricane Katrina response makes the contrast concrete. FEMA's
centralised command structure produced an information bottleneck — urgent
field reports of levee breaches and stranded refugees went unacted-on for
days, and unapproved supply shipments were blocked pending central
authorisation, while approved-but-idle resources (buses, boats) sat unused
nearby. Wal-Mart's response, by contrast, explicitly pushed authority to
store managers ("make the best decision you can with the information
available, and do the right thing"), while central leadership scaled a
support function (an 80-operator call centre) rather than trying to
pre-approve field decisions. The difference was not caution versus daring —
it was matching the response's authority structure to the actual difficulty
tier of the problem.

Decentralising authority on its own is not sufficient — it trades one
failure mode (bottlenecked information) for another (uncoordinated action,
unshared local knowledge) unless something *forces* the periphery to
communicate at defined points. This is why well-designed checklists in
complex domains routinely bundle two distinct kinds of item that are easy to
conflate:

- **Procedural items** — verify that a known, previously-agreed step wasn't
  skipped (a routine, low-judgment check).
- **Communication items** — force people who would not otherwise talk, or
  would not otherwise talk *now*, to exchange specific information before
  proceeding (team introductions before surgery, a pre-service staff
  briefing, aviation's rule that the pilot *not* flying is the one who
  challenges the pilot flying).

The communication items are doing the harder work: they are a structural
substitute for the hierarchical deference that would otherwise let a junior
team member's safety-relevant observation go unspoken (see [team
preconscious knowledge](team-preconscious-knowledge.md), and the deadliest
aviation accident in history — Tenerife, 1977 — where a flight engineer's
doubt about a takeoff clearance never became a spoken challenge to the
captain). A team can be assembled from strangers minutes before a crisis
(as US Airways 1549's cockpit and cabin crew were) and still function as a
coordinated unit, provided the forcing function for early communication ran
on schedule.

Forcing functions also operate as **trained reflexes for critical
confirmation** under extreme time pressure. When Sullenberger announced his
intention to land on the Hudson, controller Patrick Harten immediately asked
him to repeat it — "as much a trained reflex as a conscious request." The
link to Tenerife is explicit: the KLM captain misunderstood a non-clearance
for takeoff and hundreds died from the tiniest break in clarity. Outcome-
optimized phrasing is another variant: Sullenberger broadcast "Brace for
impact" rather than "water landing," because the latter would trigger life-
jacket instructions and consume seconds the crew did not have — a deliberate
word choice that let flight attendants execute the brace protocol
immediately. Conversely, [protocols require a speak-up
culture](protocols-require-speak-up-culture.md): for many critical seconds
the cockpit crew worked in efficient silence, concentrating on tasks and
watching each other for visual cues — psychological safety does not imply
excessive talking; it implies saying what matters when it matters.

This is the concrete mechanism behind [high-reliability
organizations](high-reliability-organizations.md)' "decentralization"
ingredient: decentralising alone is not the safety property; decentralising
*combined with* a mandatory, scheduled communication channel back across
organisational or hierarchical boundaries is. Removing the forcing function
while keeping the decentralisation (or vice versa) reproduces one of the two
original failure modes.
