---
type: concept
title: "T2EAM: Taskwork and Teamwork Strategies for Resilient Performance"
description: >
  A field-derived taxonomy of the individual and team cognitive strategies
  air traffic controllers actually use during emergencies — and the finding
  that standard simulator refresher training scores well on every strategy
  while real incidents fail specifically at error management and workload
  redistribution, the two strategies standardised training never exercises.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 8"
---

Malakis and Kontogiannis studied operational air-traffic-control dyad teams
(an Executive Controller and a Coordinating Controller working together) to
identify what cognitive strategies actually produce resilient performance
during emergencies and abnormal situations, distinct from what standard
regulatory refresher training drills. The resulting **T2EAM** model splits
those strategies into individual taskwork and team-level teamwork:

**Individual taskwork strategies:**

1. **Anticipation** — recognising and preparing for likely challenges and
   threats during low-tempo periods, before they arrive.
2. **Recognition** — timely, accurate detection of an emergency's early
   signs, spanning from fast *symptom-fault matching* (classifying a
   suddenly declared emergency) to slower *pattern recognition*
   (interpreting a cue pattern that evolves over time).
3. **Managing uncertainty** — assembling and continuously assessing a model
   of the situation and setting safety goals despite genuine information
   gaps, which matter especially because a flight crew in an emergency is
   often unable or unwilling to communicate its status.
4. **Planning** — either executing a standard prescribed checklist, or
   precautionary *contingency planning* to pre-empt escalation the standard
   script doesn't cover.
5. **Managing workload** — acting as a mental task regulator: switching
   attention, prioritising tasks, and deciding when to be interruptible.

**Teamwork strategies:**

1. **Team coordination** — directing team members, building a shared mental
   model, and clarifying intent across both intrateam and interteam
   dependencies.
2. **Team communication** — proactively pushing status updates and critical
   information without garbling the channel or distracting a teammate
   already at capacity.
3. **Error management** — running an augmented, parallel monitoring
   strategy — built up through experience, not specified by procedure — to
   catch a teammate's error promptly and feed back correction without
   breaking the flow of the primary task.
4. **Change management** — detecting and actively counteracting an emerging
   imbalance in task distribution between team members as backlog builds.

**The training-realism gap this model exposed is the finding with the
widest reach.** Across 21 dyadic teams, standard simulator refresher
training produced consistently high scores across every T2EAM strategy —
but that result came from familiarity with pre-briefed, standardised
scenarios, and the near-absence of errors in those scenarios meant
controllers had almost no opportunity to actually practise error recovery
or workload redistribution under stress. In one emergency-descent scenario
run in simulation, two separation losses occurred because the Executive
Controller under-corrected a vertical deviation (issuing a 5–15° heading
change where more than 40° was required) and the Coordinating Controller
never prompted or questioned the inadequate correction. A separate analysis
of 14 *real* incidents under genuine heavy workload, interruption, and
distraction found separation losses traced overwhelmingly to the same two
specific strategies — error management and change management — breaking
down: the Coordinating Controller failed to detect or flag the emerging
loss, while the Executive Controller was caught by surprise, lost time
questioning the pilot rather than acting, and executed a delayed or
inadequate resolution.

This is a concrete, measured instance of [the irony of
resilience](irony-of-resilience.md): training built around pre-planned,
low-error scenarios produces controllers who score well on every strategy
the training actually exercises, while leaving exactly the two
teamwork-under-stress strategies — error management and change management —
untrained, because a low-error simulator scenario structurally cannot
generate the errors those two strategies exist to catch. The gap is not a
training-intensity problem fixable by running the same scenarios more
often; it is a training-*design* problem, because the scenario design
itself removes the very condition (frequent, unexpected error) the missing
strategies need practice against.
