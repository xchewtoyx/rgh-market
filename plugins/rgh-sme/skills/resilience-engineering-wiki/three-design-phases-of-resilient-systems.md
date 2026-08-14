---
type: concept
title: Three Design Phases Where Resilience Deficiencies Originate
description: >
  Systemic and knowledge deficiencies that surface as an operational failure
  were usually built in far earlier, across three distinct engineering
  design phases — so an investigation confined to the moment of failure
  misses where the fix actually belongs.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 15"
---

Traditional engineering design assesses a system across three sequential
phases (Stoop), and a genuine forensic investigation has to be able to trace
a deficiency back to whichever phase actually produced it, not just to the
operational moment it eventually surfaced in:

1. **Conceptualisation** — selecting the design concepts, configurations,
   and control arrangements themselves. This is where inherent safety
   properties get decided: fail-safe mechanisms, crashworthiness, and how
   control is distributed or delegated in human-centred parts of the
   system.
2. **Function allocation** — deciding which accident scenarios are
   acceptable within the system's intended operational context, given the
   functions it is meant to fulfil. This is where the system's emergent
   properties get shaped: redundancy, robustness, reliability,
   reconfigurability, rescue and recovery capability, and resilience
   itself.
3. **Materialisation** — quantifying operational failure probabilities and
   consequences, measured against safety standards, accident frequency
   targets, or formal integrity levels.

**Deficiencies split into two kinds, and both can originate in any of the
three phases above** — neither kind is specific to the execution phase where
a failure actually happens:

- **Knowledge deficiencies** — gaps in understanding how the system actually
  behaves under extreme or previously unstudied conditions.
- **Systemic deficiencies** — flaws in decision-making, in the assumptions a
  design carried forward unexamined, or in the organisational structures
  around the system.

The practical consequence for investigation scope: a review that only
examines the moment of technical failure is looking exclusively at
materialisation-phase symptoms of a deficiency that may well have been
locked in during conceptualisation, years or decades earlier and several
organisational layers removed from the operational team. This is the same
scope failure the [root-cause fallacy](root-cause-fallacy.md) warns against
at the level of a single accident chain, generalised to the life of a whole
system: stopping the search for causes at "the execution phase" is just as
arbitrary a stopping point as stopping at "the last human act." A genuinely
forensic investigation — one aiming to give the [epistemic-distance sweet
spot](epistemic-distance-in-post-accident-learning.md) something substantive
to work with — has to be willing to trace a deficiency all the way back to a
conceptualisation-phase decision made well before the system that failed was
ever operational.
