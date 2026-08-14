---
type: concept
title: Requirements Prioritization
description: >
  Requirements are ranked using multiple factors together — business
  value, cost, risk, dependency order, and how satisfied or dissatisfied
  a stakeholder would be — rather than by whoever asked loudest.
sources:
  - title: Mastering the Requirements Process
    resource: "Mastering the Requirements Process: Getting Requirements Right (Suzanne Robertson, James Robertson), ch. 16, ch. 17"
---

Requirements prioritization combines several factors rather than ranking
on a single scale: business value or urgency, cost of implementation,
technical risk or complexity, and dependency order (some requirements
can't be built before others regardless of their individual priority).

A specific technique for capturing business value is a Kano-style rating
attached to each requirement: **customer satisfaction** (1–5, how pleased
the stakeholder would be if this is implemented) alongside **customer
dissatisfaction** (1–5, how upset they'd be if it's omitted). High
satisfaction paired with low dissatisfaction marks a "delighter" — nice to
have but not expected. Low satisfaction paired with high dissatisfaction
marks a basic, expected requirement — invisible when present, glaring when
missing. This distinction changes how a requirement should be treated
under schedule pressure: cutting a delighter and cutting a basic
expectation are not equivalent risks, even if their raw "priority" looks
similar.

The full Kano model actually names three categories, not two: alongside
**basic** (threshold) and **delighter** (nonlinear, differentiating) sits
a **linear** category, where satisfaction scales roughly proportionally
with how much capability is delivered rather than jumping at a threshold
or an unexpected extra. The strategic implication is what makes the
three-way split useful beyond scoring individual requirements: a team
that is behind competitors on basic-feature parity can still rationally
choose to under-invest in catching up and instead invest in delighters,
because customers tolerate a credible "basics are coming" story paired
with visible differentiation more than they reward parity alone — chasing
pure basic-feature parity against a moving competitor is often a losing
race regardless of investment level.

Prioritization happens inside the [atomic requirement
shell](atomic-requirement-shell.md) as an explicit field, not as an
after-the-fact ranking exercise — recording it at the point a requirement
is written keeps the reasoning attached to the requirement rather than
living only in whoever ran the prioritization meeting.

A complementary four-lens model, aimed at comparing candidate needs before
they've become requirements at all (an [opportunity solution
tree](opportunity-solution-tree.md)'s siblings, in agile-discovery
vocabulary), widens the comparison beyond a single satisfaction score:
**sizing** (how many customers are affected, and how often — two separate
dimensions), **market factors** (competitive positioning and external
trend exposure), **company factors** (fit with strategic objectives and
the political capital required), and **customer factors** (how important
this is to affected customers versus how well they're already served).
The deliberate discipline here is *not* to collapse these four lenses into
one numeric score and rank by it — that manufactures false precision for
what is a genuinely subjective, relative judgment call, and different
lenses legitimately disagreeing with each other (one option wins on
sizing, another on strategic fit) is a normal, informative outcome to
surface in the prioritization record, not a problem to average away.

At the scale of a single backlog item due for [just-in-time
elaboration](just-in-time-requirement-elaboration.md), a narrower
three-factor scheme applies the same "don't collapse to one score
carelessly" spirit to a smaller, more local decision: **independent user
value** (value relative to other backlog items, usually set from domain
knowledge), **iteration value** (how much the item helps meet the current
iteration's specific objectives, which can outrank its general value), and
**risk reduction** (the value of the information completing this item
would surface, lowering risk in later work). This third factor is why a
low-user-value item — a [spike](spike-story.md), for instance — can
legitimately outrank higher-value items once its risk-reduction
contribution is weighed in: its payoff isn't the deliverable itself, it's
the uncertainty it removes from everything downstream of it.

A coarser, faster complementary technique for triaging a large candidate
set before detailed prioritization: plot each candidate on a two-axis grid
of business impact against feasibility. High-impact, high-feasibility
candidates are the obvious next work; low-impact, low-feasibility
candidates are dropped outright; low-impact-but-feasible candidates are a
trap teams fall into precisely because they're easy, not because they're
valuable; high-impact-but-currently-infeasible candidates are worth
recording as a target for whoever can close the feasibility gap, rather
than being silently dropped alongside the low-impact ones.

See [ordinal weighted-score pitfall](ordinal-weighted-score-pitfall.md)
for why combining several such ordinal ratings into one multiplied-and-summed
composite score should be avoided even though the individual ratings
above are legitimate.

At the scale of sequencing a set of already-committed features rather than
triaging candidates, [Weighted Shortest Job First](weighted-shortest-job-first.md)
replaces "impact" and "feasibility" with a single ratio — cost of delay
divided by effort — precisely because raw value or raw size alone can
recommend the wrong sequence once how fast each feature's value decays is
taken into account.
