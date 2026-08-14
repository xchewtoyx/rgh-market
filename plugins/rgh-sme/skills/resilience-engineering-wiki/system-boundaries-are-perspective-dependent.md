---
type: concept
title: System Boundaries Are Perspective-Dependent
description: >
  Where a system's boundary is drawn is not a fact about the system but a
  choice tied to the observer's objective — so different legitimate
  observers of the same system see different systems, and each is blind to
  couplings the others can see.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 13"
---

A system boundary is not a fixed physical fact waiting to be discovered — it
is drawn relative to the observer's own perspective and objective, and
different legitimate observers of the same underlying system draw it in
genuinely different places. In financial services: a global economist's
boundary includes macro-economic systems and international markets; a
micro-prudential regulator's boundary is drawn tightly around one regulated
entity; a macro-prudential regulator's boundary spans the cross-institutional
interactions between many entities. None of these three is wrong — each is a
legitimate, working boundary for a different question.

**The consequence is a structural blind spot, not a correctable oversight.**
An observer whose boundary is drawn around a single institution cannot see
[functional couplings](functional-resonance-analysis-method.md) that cross
that boundary, no matter how carefully they analyse what is inside it — the
coupling simply is not represented in their model, by construction of where
they drew the line. This is why a firm-level regulator can find an
individual institution's internal risk management sound right up to the
point of its collapse: the firm's vulnerability was never a property
visible from inside the boundary that regulator was using, because it lived
in a dependency on something outside it (a specific historical instance:
[Northern Rock's dependency on wholesale credit-market
preconditions](functional-resonance-analysis-method.md)).

The practical implication is that "who is monitoring the system" is not a
single question with a single right answer — a genuinely systemic risk
requires an observer whose boundary is drawn wide enough to contain the
coupling, and no observer with a narrower boundary can be faulted, after the
fact, for failing to see what their vantage point structurally excluded.
This generalises past finance to any domain where oversight is distributed
across institutions with different, non-overlapping boundaries: the gap
between what each institution's boundary contains is exactly where a
cross-institutional failure can develop unmonitored by anyone.
