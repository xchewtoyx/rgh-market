---
type: concept
title: The Irony of Resilience
description: >
  The same blunt-end effort to pre-determine every response and eliminate
  operational variability erodes the sharp-end improvisational skill that
  becomes the system's only resource once an event falls outside what was
  pre-determined.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 2"
---

Pariès's irony of resilience is a direct parallel to Bainbridge's older
"irony of automation": automating a task leaves the human operator only the
residual pieces designers couldn't automate, while removing the routine
practice that kept the operator's skill at those pieces sharp — so the
operator is least practised exactly where automation eventually fails and
hands control back. The irony of resilience runs the same trap at the level
of procedure and standardisation rather than automation: blunt-end managers
pursue safety by prescribing procedures, standardising behaviour, and
pre-planning responses to every anticipated contingency. Inside the
anticipated envelope this genuinely works — discipline, predictability, and
efficiency all rise. But when an event falls outside that envelope (see [the
boundary of potential variability](boundary-of-potential-variability.md)),
the system has nothing left to fall back on except sharp-end autonomy,
creativity, and adaptability — the exact capabilities the standardisation
programme spent years suppressing in the name of safety.

This is the applied, organisational-training face of [the adapted-versus-
adaptive trade-off](adapted-vs-adaptive-trade-off.md): efficiency is
adaptation to the standard, expected environment; flexibility is adaptation
bandwidth across the unexpected. Push efficiency far enough and a system
gets cheaper and safer inside its normal envelope while becoming
increasingly brittle at the edges — a desert lizard superbly adapted to
hyper-arid heat that a small climate shift can kill, because there was never
selection pressure to keep the machinery for handling cold.

**Mintzberg's fallacy of predetermination** is the belief driving the
trap: that sufficiently detailed planning and rule-making can anticipate all
future operational states, which quietly slides into believing the world
will actually unfold as prescribed. The ACCOMPLI study of European airline
first officers found the fallacy's real cost directly: new pilots reported
high confidence handling routine operations and pre-trained abnormal
scenarios, and simultaneously widespread anxiety about everything a
predetermination-based syllabus doesn't cover — operating at the ambiguous
edges of standard procedures, genuine surprises, borderline conditions like
unstabilised approaches, and the interpersonal variability of different
captains. Standard training reinforces exactly this gap: emergency drills
are pre-briefed, run once without surprise, then debriefed — which
eliminates the one thing (the cognitive shock of genuine surprise) that
uncertainty-management skill actually requires practice against. Routine,
daily homeostatic adaptation does not build this skill either; it only
develops through recurrent exposure to events that are actually challenging
and unexpected at the moment they happen.

**Training countermeasures aim at reintroducing exactly the surprise
standard training removes**: unbriefed simulator exposure to scenarios
pilots don't know are coming, solo flight experience that forces self-
reliance without a safety-net crew, incident debriefs that keep the
emotional context rather than sanitising it into a technical summary, and
deliberate counterfactual "what-if" mental rehearsal of complications before
they occur — a technique shown to lower mortality among paediatric cardiac
surgeons who rehearsed failure scenarios in advance. This is the training
application of the same imaginative-rehearsal mechanism as the [premortem
technique](premortem-technique.md), aimed at building real-time skill rather
than critiquing a specific plan.

**The systemic answer is coupling anticipation with serendipity, not
choosing between them.** Generic anticipation schemes — abstract sensemaking
frameworks built to wrap around unpredictable variation rather than
enumerate specific action recipes — give the sharp end something to reason
from without prescribing exactly what to do; real-time implementation skill
(serendipity) is what adapts the generic scheme to the actual, specific,
time-pressured situation. Decision-support tools belong inside this
architecture too, engineered to reduce sharp-end cognitive load during a
genuine crisis rather than to replace the judgement the crisis demands — for
instance, a glide-distance management tool that helps a crew work an
all-engines-out descent without consuming the attention that judgement
itself needs.

[T2EAM's air-traffic-control field study](t2eam-taskwork-and-teamwork-strategies.md)
gives this a measured, rather than anecdotal, case: standardised simulator
refresher training produced uniformly high scores across every cognitive
strategy studied, while real incidents failed specifically at the two
strategies — error management and workload redistribution — that a
low-error, pre-briefed scenario structurally cannot exercise.
