---
type: concept
title: Automation Bias
description: >
  Humans who rely on automated tools for long enough lose the situational
  awareness and manual skill needed to intervene effectively when the
  automation fails or behaves unexpectedly.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 7"
  - title: "Thinking in Systems: A Primer"
    resource: "Thinking in Systems: A Primer (Meadows), ch. 5"
  - title: "Drift into Failure: From Hunting Broken Components to Understanding Complex Systems"
    resource: "Drift into Failure (Dekker), ch. 6"
---

# Automation Bias

The more consistently automation handles an operation correctly, the less
often a human performs — or even watches — that operation manually. Over
time this erodes the operator's own understanding of the system and their
practiced skill at doing the task by hand. The failure mode this produces is
an irony rather than a simple tradeoff: the automation is introduced
*because* the manual task is failure-prone or slow, but its long-term
success quietly removes the human capability that would be needed to take
over cleanly the one time the automation itself fails or hits a case it
wasn't built for.

This risk grows as automation moves up the [automation maturity
spectrum](automation-maturity-spectrum.md) — the more autonomous the
system, the rarer and more unfamiliar manual intervention becomes, and the
more a real incident depends on skills nobody has exercised recently.

Bainbridge's irony of automation is the automation-specific case of a
broader pattern, Pariès's [irony of resilience](irony-of-resilience.md):
any blunt-end effort to eliminate operational variability — not just
automating a task, but standardizing and proceduralizing it — trades away
sharp-end adaptive capacity for efficiency inside the cases it anticipated.

There's a second, independent irony sitting underneath this one:
introducing automation as a redundancy or reliability layer doesn't
eliminate human work, it converts it into a different and harder kind —
monitoring a system that is highly reliable almost all of the time.
Sustained vigilance for a rare deviation is a task humans are
constitutionally bad at, so the very success of the automation being
watched is what erodes the quality of the watching. This means adding an
automated layer specifically *to* catch a failure mode can introduce a new
failure pathway of its own (an unwatched watcher) even as it closes off
the original one.

A related but distinct failure is [automation
surprise](automation-surprise.md): where automation bias is the skill an
operator loses from disuse over time, automation surprise is the
moment-to-moment gap between what the automation is doing and what its
operator believes it is doing, regardless of how skilled that operator
still is.

This is a specific case of a general systems-theory pattern sometimes called
"shifting the burden to the intervenor": an intervention (here, automation)
relieves the symptom of a struggling manual process, but if it also erodes
the system's own underlying capability to perform that process, the system
becomes steadily more dependent on the intervention just to stay where it
is — and reverting becomes progressively more painful the longer the erosion
continues. The general defense isn't refusing to automate; it's noticing
when an automated system is being asked to substitute for a capability
rather than merely relieve its drudgery, and deliberately preserving that
capability — through periodic manual drills, forced fallback exercises, or
game days — before it atrophies past the point of being available when the
automation itself fails. Not every drill rebuilds the capability equally:
see [unbriefed surprise exposure](unbriefed-surprise-builds-uncertainty-competence.md)
for why a scripted, pre-briefed drill rehearses template-matching rather
than the genuine adaptive competence a real surprise would demand. This is the human-skill counterpart to
[confidence decay in unpracticed
safeguards](confidence-decay-in-unpracticed-safeguards.md): the same
disuse that lets a failover mechanism quietly rot also lets the people who
would need to operate it manually lose the ability to do so.
