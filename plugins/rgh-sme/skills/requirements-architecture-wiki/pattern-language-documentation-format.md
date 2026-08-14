---
type: concept
title: Pattern-Language Documentation Format
description: >
  A pattern is documented as a named, recurring problem paired with a
  concrete solution structure mined from real practice, giving designers a
  shared vocabulary that a one-off design narrative cannot provide.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Unmesh Joshi), ch. 1-2"
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann, Stocker, Lübke, Zdun, Pautasso), ch. 3"
---

Originating with architect Christopher Alexander's "pattern language" and
popularized in software by the Gang of Four, a **pattern** is documented as:
a **name** for the recurring solution, the **problem**/context that provokes
it, a **concrete-enough solution structure** (specific enough to show real
code or a real mechanism, not just a principle), and typically a list of
**known uses** — real systems that independently arrived at the same
structure. Patterns are mined empirically, by studying multiple existing
codebases for a recurring shape, rather than designed top-down.

This differs in kind from viewpoint-based [architecture documentation](architecture-documentation-package.md),
which documents *one system's* actual structure. A pattern instead documents
a reusable solution shape that many different systems' structures can
instantiate — closer to a vocabulary entry than a description of a
particular design. The payoff of naming a pattern well is the same payoff
[architectural tactics](architectural-tactic.md) provide at a finer grain:
a design conversation or decision record can cite "Leader and Followers" or
"Two-Phase Commit" and both parties immediately share the problem, the
solution shape, and its known trade-offs, without re-deriving or
re-explaining the mechanism from scratch. A single **narrative walkthrough**
that chains patterns together in the order their problems arise from one
another (each pattern's solution surfacing the next problem) is itself a
useful documentation device for showing how a catalogue of patterns
composes into a real system, separate from documenting each pattern in
isolation.

When patterns catalogue **architectural decisions** rather than
implementation mechanisms, a useful narrative format is: name the
**decision** (the topic being resolved), present each candidate as a
**pattern** entry (problem statement, solution shape), then list
**decision criteria** drawn from the pattern's forces (pros, cons, and
constraints), good-practice recommendations, and finally a **sample
decision outcome** as an [architectural decision
record](architectural-decision-capture.md) using a why-statement that
names the chosen option, neglected alternatives, intended benefit, and
accepted negative consequences. Each pattern's documented forces become
the inspection checklist in [documenting trade-offs](documenting-trade-offs.md)
before committing.

The engineering substance of any specific pattern (e.g. the mechanics of a
write-ahead log or a quorum-based commit protocol) is outside this domain's
scope — it belongs to whichever domain owns that technique. What belongs
here is the documentation form itself: naming and structuring recurring
design solutions so they can be cited by name in [requirement rationale](requirement-rationale.md)
and [documenting trade-offs](documenting-trade-offs.md) instead of restated.
