---
type: concept
title: Three Conditions for Effective Learning
description: >
  Effective learning requires frequent opportunities, cases similar enough to
  generalise across, and a chance to verify the lesson before it matters —
  accidents in safe systems structurally fail all three, which is why
  learning from everyday normal work outperforms learning from accidents.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 14"
---

Classical safety management assumes learning is grounded in things that went
wrong: incidents, accidents, catastrophes. This assumption conflicts with
what learning in general actually requires — three conditions, all of which
have to hold together:

1. **High frequency of opportunities** — the situations that could teach a
   lesson have to recur often enough that an earlier lesson is not forgotten
   before it is needed again.
2. **Sufficient similarity for generalisation** — cases have to share
   underlying reasons and causes, not merely similar-looking outcomes, for a
   pattern to be extractable across them at all.
3. **Opportunity to verify the lesson** — comparable events have to keep
   happening often enough, after a lesson is drawn, to confirm the lesson
   learned was actually the right one, well before a major event puts it to
   the real test.

Accidents in a mature, safe operational domain fail all three simultaneously,
structurally, not by bad luck: they are rare (violating frequency), each one
differs from the last roughly in proportion to how severe it was — the worse
the outcome, the more idiosyncratic its specific path there tends to be
(violating similarity) — and there is essentially no chance to verify a
drawn lesson against a next comparable case before it would matter for real
(violating verification). This is the learning-theory argument for why
resilience engineering privileges [studying normal
work](studying-normal-work.md) over accident investigation as the primary
information channel: everyday operations satisfy all three conditions where
accidents structurally cannot, and the underlying premise — that success and
failure are produced by the exact same source, ordinary performance
variability — is [Safety-II's core claim](safety-i-and-safety-ii.md), not a
separate assumption bolted on to justify the shift.

This also explains why learning cannot be reduced to mechanical data
collection or statistical counting: satisfying these three conditions
requires actively identifying *the right thing* to learn from, not just
accumulating more records of whatever already gets reported. Two named
principles capture the trap of getting this wrong: **What-You-Look-For-Is-
What-You-Find** (WYLFIWYF) — an investigation's initial assumptions about
mechanism constrain what evidence even gets gathered, the same premise
behind [why your accident model shapes what you
find](accident-model-shapes-what-you-find.md) — and its corollary,
**What-You-Find-Is-What-You-Learn** (WYFIWYL, Lundberg et al., 2009): an
organisation can only ever learn about the dynamics it actively went looking
for, so a narrow search produces narrow learning regardless of how much data
it processes.

Learning is not one capability sitting alongside [anticipation, monitoring,
and response](four-abilities-of-resilient-performance.md) as an independent
fourth item — it directly enables and reshapes the other three. Response
improves as a system observes and evaluates how well its predefined
responses actually performed and adapts them; monitoring indicators are
themselves established through practice and learning rather than derived
from a pre-existing formal model (though indiscriminately adding a new
indicator after every incident is its own failure mode, distinct from not
learning at all); and anticipation depends on learning to keep the system's
model of future possibilities realistic, rather than frozen at whatever it
was set to originally. No amount of strength in the other three
capabilities compensates for weakness in this one, because each of the
other three is partly built out of what this one supplies.
