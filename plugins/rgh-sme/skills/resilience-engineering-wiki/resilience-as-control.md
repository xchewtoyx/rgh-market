---
type: concept
title: Resilience as a Form of Control
description: >
  A system is "in control" to the extent it can minimise unwanted
  performance variability in itself and its environment — and loss of
  control traces to one of four specific constraints, not a single generic
  cause.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), epilogue"
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 7"
---

A control-theoretic reading of resilience, complementary to
[systems-theoretic accident models](systems-theoretic-accident-model.md): a
system is *in control* insofar as it can minimise or eliminate unwanted
performance variability, whether that variability originates inside the
system or in its environment. Loss of control is not a single phenomenon —
it traces back to one (or several, compounding) of four universal
constraints:

1. **Lack of time** — the system is purely reactive, running on feedback
   loops alone. Detecting a change and marshalling a response both take
   time, and a purely reactive system is structurally always behind the
   events it is responding to.
2. **Lack of knowledge** — the system's working model of its own world is
   deficient, or the people running it lack **requisite imagination**
   (Westrum's term): the capacity to look past what has actually happened
   before and genuinely expect the unexpected, rather than treating the
   historical record as the boundary of what's possible. This is the
   knowledge-side analogue of [Westrum's typology of organisational
   culture](westrum-typology.md) — a culture that suppresses dissenting
   information also suppresses the imagination needed to anticipate what
   hasn't happened yet. Requisite imagination is trainable, not fixed:
   scenario-based auditing — running leadership through guided simulations
   that confront their assumptions with what work actually looks like — is a
   deliberate "broadening check" built specifically to cultivate it, the
   leadership-facing counterpart to [studying normal
   work](studying-normal-work.md) at the sharp end.
3. **Lack of competence** — the operational understanding of what to do and
   how to do it is simply missing, independent of whether the danger was
   correctly anticipated.
4. **Lack of resources** — the physical, technical, or human capital needed
   to execute the intended response does not exist, even when the response
   itself is well understood.

The observable behavioural signature of shrinking time and knowledge is
[Hollnagel's four control modes](hollnagel-four-control-modes.md): as these
constraints bite, an actor's behaviour visibly downgrades from strategic
through tactical and opportunistic to scrambled control, in that order.

These four constraints correspond directly to the [four abilities of
resilient performance](four-abilities-of-resilient-performance.md):
anticipation fails specifically from lack of knowledge, monitoring fails
specifically from lack of time, response fails specifically from lack of
competence or resources — which makes the framework diagnostic, not just
descriptive: naming which constraint bit tells you which ability to invest
in, rather than treating "be more resilient" as a single undifferentiated
goal.

**Detecting hazards is not the same as being in control of the response to
them**, and organisations can build extensive capability for the former
while never building the latter. The 2005 California tsunami warning system
after the underlying earthquake is the illustrative failure: external hazard
detection worked, but the warning that reached different regional centres
was contradictory (Alaska's centre and Hawaii's centre broadcast differing
information), and local terrain and line outages prevented the warning from
reaching some coastal communities at all. The system had safety technology
and procedures aimed outward, at the hazard, but no internal self-monitoring
capability verifying that its own communication feedback loops were
actually functioning — it was watching the earthquake and not watching
itself.
