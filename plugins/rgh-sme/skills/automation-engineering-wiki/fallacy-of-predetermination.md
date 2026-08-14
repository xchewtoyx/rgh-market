---
type: concept
title: Fallacy of Predetermination
description: >
  Detailed planning and rule-writing create the illusion that all future
  operational states have been anticipated, when no realistic amount of
  upfront rules can actually cover every situation a system or its
  operators will eventually meet.
sources:
  - title: Resilience Engineering in Practice
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 2"
---

# Fallacy of Predetermination

Mintzberg's (1994) **fallacy of predetermination** is the belief that
detailed planning and rule-making can anticipate all future operational
states — that writing enough procedures, checklists, and standard operating
boundaries in advance is equivalent to controlling what will actually
happen. Each additional rule feels like it closes a gap; in aggregate, the
rules foster an illusion that the world will unfold as prescribed, rather
than a realistic assessment of how much of the state space they actually
cover.

Evidence of the gap this creates: a French DGAC study of airline pilot
cognitive competence (the ACCOMPLI project) found newly trained First
Officers highly confident handling routine operations and pre-trained,
anticipated abnormal scenarios — exactly the cases their training's rules
covered — but reporting real anxiety and a lack of preparation for
everything the rules didn't: operating at the edges of standard operating
procedures or in SOP ambiguity, genuine unanticipated surprises, borderline
conditions, variable interpersonal dynamics, and multitasking under
interruption. The training architecture itself reinforced the gap:
emergency exercises were pre-briefed, run once, and debriefed, so trainees
practiced matching a recognized scenario to its procedure rather than
coping with the cognitive shock of a real, unscripted surprise.

This is the planning-side counterpart to [safeguards against runaway
automation](safeguards-against-runaway-automation.md)'s observation that a
rule-based system's judgment is inherently limited to the cases its rules
cover — the fallacy of predetermination is what makes designers and trainers
keep expanding the rule set as if that limitation could eventually be
engineered away, rather than treating "the rules will run out" as a
permanent property to design around. It is one of the two mechanisms behind
the [irony of resilience](irony-of-resilience.md): proceduralizing further
in response to this fallacy is exactly what narrows the sharp end's adaptive
range for the cases the rules still won't cover.
