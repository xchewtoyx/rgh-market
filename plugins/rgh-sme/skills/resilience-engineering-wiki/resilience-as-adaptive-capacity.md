---
type: concept
title: Resilience as Adaptive Capacity, Not a Static Property
description: >
  Organisational resilience is not a fixed safety margin a system either has
  or lacks — it is a set of ongoing capabilities to recognise, steer away
  from, and recover from the edges of safe operation.
sources:
  - title: "Drift into Failure: From Hunting Broken Components to Understanding Complex Systems"
    resource: "Drift into Failure (Dekker), ch. 5"
  - title: "Thinking in Systems: A Primer"
    resource: "Thinking in Systems (Meadows), ch. 3"
---

Resilience engineering starts from a premise that sounds alarming but is
meant descriptively, not pejoratively: every open system operating under
[goal conflict](goal-conflicts-and-production-pressure.md) is continually
adrift somewhere inside its own safety envelope. The field's move is to
reframe that continual adrift-ness not as a defect to be engineered away but
as the normal condition of a working system — the real question is not "how
do we stop drifting" but "how capable is this organisation at handling the
fact that it drifts." That capability decomposes into four parts:

1. The capability to **recognise** the boundaries of safe operation as they
   actually are (not as originally designed).
2. The capability to **steer back** from those boundaries in a controlled
   way once approaching them is recognised.
3. The capability to **recover** from an actual loss of control, rather than
   only trying to prevent one.
4. The capability to **detect** when margins are being skirted or crossed at
   all, given that [decrementalism](decrementalism.md) makes this
   structurally hard.

These are process capabilities — whether the organisation actually exercises
them in time. The structural properties they act on ([buffering capacity,
margin, and tolerance](buffering-margin-and-tolerance.md)) are a separate,
complementary framework: a system can have ample buffering capacity and
still fail if these four capabilities are absent.

Woods frames the same distinction as **first-order versus second-order
adaptability**. First-order adaptability is competence within the
disruptions a system's designers anticipated — performance inside the
textbook envelope. Second-order adaptability, which is what "resilience"
is reserved for, is the capability to handle perturbations that fall
*outside* that envelope entirely, arising either because the organisation's
model of its own competence was always incomplete or flawed, or because the
environment shifted and created pressures the model never covered. Failing
at second-order adaptability while still executing first-order competence
flawlessly is Mitroff's **error of the third kind**: an organisation solving
the wrong problem, persisting with textbook plans despite accumulating
evidence that the situation itself has changed and needs a different
assessment — not better execution of the old one. Resilience engineering's
role is to monitor the boundary of the current competence envelope and make
the organisation's internal model of its own safety visible, so that model
can be revised before an accident forces the revision at much higher cost.
Pursuing first-order adaptability by standardising and pre-planning every
anticipated response is not neutral with respect to second-order
adaptability — it actively erodes the improvisational skill second-order
adaptability depends on, which is [the irony of
resilience](irony-of-resilience.md).

This is also why resilience should not be reified into a static system
property in the first place. Hollnagel names the underlying error the
**reification fallacy**: treating an ongoing process as if it were a fixed
entity a system simply *has*. Safety is something a system *does* — a
quality of its performance under ongoing variability — not something it
possesses once and keeps. The practical consequence follows directly:
organisations can only ever measure a system's *potential* for resilience
(its current buffering capacity, margin, and the four abilities above), not
resilience itself, because resilience only exists as an enacted quality of
performance against a disruption that has not happened yet. This is also why
resilience cannot be engineered simply by multiplying procedures,
safeguards, or barriers — that approach treats resilience as a quantity of
static stuff to add, when it is a continuously exercised capability that
static barriers can support but never substitute for. See [the four
abilities of resilient performance](four-abilities-of-resilient-performance.md)
for what "exercised" actually decomposes into, and [resilience as
control](resilience-as-control.md) for the specific constraints that block
each ability.

This distinguishes resilience sharply from **reliability**: reliability is a
component-level property (a part's failure rate against a specification),
the same lens quality control uses. A part can be perfectly reliable and the
system still unsafe, because [safety is an emergent, whole-system
property](systems-theoretic-accident-model.md) that lives in the
relationships between parts, not in any part's individual conformity to
spec. Building more reliable components is therefore not the same project
as building a more resilient organisation, and can even work against it by
[adding relationships that increase
complexity](redundancy-can-increase-complexity-risk.md).

The open management question resilience engineering poses is how an
organisation monitors its own ongoing adaptation to scarcity and competitive
pressure — adaptation that is simultaneously shaping the [local
rationality](local-rationality-principle.md) of the people doing the
monitoring — while its knowledge of its own [unruly
technology](unruly-technology.md) stays permanently incomplete. This is the
organisational-capability counterpart to the individual-level programme of
[studying normal work](studying-normal-work.md).

**Resilience is routinely traded away for measured productivity or
stability, without anyone deciding to make that trade** — [the law of
stretched systems](law-of-stretched-systems.md) is why: any gain gets
consumed by higher tempo and complexity rather than kept as reserve. Meadows's systems-
theory formulation of the same idea: resilience comes from a system's
redundant, overlapping feedback loops operating at different timescales and
through different mechanisms, so that one can compensate if another fails —
and that redundancy looks like slack or inefficiency right up until the
moment it is needed. Just-in-time delivery, single-species forestry
optimised for yield, and a growth hormone that raises milk output by
diverting metabolic energy from other bodily functions are all cases of a
visible, measurable gain purchased with an invisible loss of the reserve
capacity that would have absorbed the next unplanned shock. The asymmetry is
structural, not a failure of vigilance: stability is directly observable
week to week, but resilience is not observable at all until its limits are
actually exceeded — a system "pays more attention to its play than to its
playing space," so the same drift that erodes
[chronic unease](chronic-unease.md) can proceed for years under a record of
uneventful, even improving, short-term performance.
