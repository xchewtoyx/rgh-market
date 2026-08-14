---
type: concept
title: Kotter's Eight-Step Change Model
description: >
  An ordered sequence for turning a decision to change something
  into a change that actually sticks — from establishing urgency
  through institutionalizing the new norm.
sources:
  - title: "The Site Reliability Workbook: Practical Ways to Implement SRE"
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne, eds.), ch. 21"
---

A decision to change how an organization works is not the same
as the change actually happening. Kotter's eight-step model
(from *Leading Change*, 1996) sequences the work of making it
happen, in order:

1. **Create urgency** — establish that the status quo is
   genuinely not sustainable, so people feel a real reason to
   change rather than being asked to change for its own sake.
2. **Build a guiding coalition** — assemble a small,
   cross-functional group with the credibility and standing to
   drive the change, not just formal sponsors.
3. **Form a strategic vision** — articulate what the changed
   state looks like clearly enough that people can recognize
   progress toward it.
4. **Enlist a volunteer army** — recruit people beyond the
   coalition who will actively participate, not just tolerate
   the change.
5. **Enable action by removing barriers** — clear the specific
   obstacles (technical, procedural, or organizational) that
   would otherwise block the volunteers from making progress.
6. **Generate short-term wins** — bank visible, concrete
   progress early, both to prove the direction is working and
   to build momentum for what remains.
7. **Sustain acceleration** — use each win to justify further
   investment and pull in more of the organization, rather than
   treating an early win as the finish line.
8. **Institute the change** — make the new way of working the
   normal, expected one, so it survives after the coalition
   that drove it moves on to other work.

A documented case (Waze's rebuild of a message-queue system
buckling under growth) shows the sequence emerging even without
anyone deliberately following the model: a genuine operational
crisis supplied step 1; two engineers plus a senior engineer
formed the coalition; the vision was a custom-built replacement,
since off-the-shelf options couldn't meet the required scale;
other teams were enlisted to trim their own message volume,
buying time to build and prove a prototype; incremental,
dual-write migration (low-traffic flows first) produced early
wins that justified completing the cutover; the old system was
then formally deprecated. The team's own retrospective lesson:
**incremental change is far easier to manage than jumping
straight to the theoretically perfect solution** — describe the
destination broadly, stay flexible about the path, and let each
step's results decide whether to keep investing or cut losses
cheaply.

This model organizes several narrower techniques already used
elsewhere into a single ordered sequence: step 1 overlaps with
[building-a-case-for-change](building-a-case-for-change.md); step
2 with finding the right person for
[sponsorship-versus-mandate](sponsorship-versus-mandate.md) and
with not overlooking someone who holds
[informal-blocking-power](informal-blocking-power.md); steps 4–5
overlap with
[stakeholder-buy-in-sequencing](stakeholder-buy-in-sequencing.md).
What Kotter's model adds is the back half — short-term wins and
sustained acceleration — that those narrower techniques don't
individually cover: a decision's coordinated-action plan should
name what an early, visible win looks like and how it will be
used to pull in the next wave of participants, not just how
initial agreement will be secured.
