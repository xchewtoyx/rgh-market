---
type: concept
title: Design Is a Continuous Activity
description: >
  Software design is never "done" — the malleability of software makes
  incremental, ongoing redesign both possible and necessary, unlike one-shot
  physical engineering.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 1"
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 2"
---

Physical engineering disciplines (buildings, ships, bridges) mostly finalize
design before construction, because construction is expensive to redo. Software
is different: it's malleable enough to support genuine mid-course design
changes, which makes design a continuous, lifelong activity rather than a
phase that completes.

This is why the **waterfall model** — discrete phases (requirements → design →
coding → testing → maintenance) with design frozen once its phase ends — fails
for software: a large system's implications generally can't be fully
visualized before it's built. Discoveries made during implementation have no
sanctioned path back into the design, so they get patched around instead of
folded into a redesign, producing an explosion of complexity over time.

**Incremental development** (e.g. agile) works with software's grain instead:
design a subset, implement it, evaluate, fix problems found, then move to the
next subset. Each iteration's fixes benefit every feature built afterward. The
practical consequence is that developers should expect to spend some fraction
of their time on continuous redesign, because the first design for anything is
almost never the best one — and should budget for it rather than treating
"design" as a one-time upfront task.

[Refactoring](refactoring-preserves-behavior.md) is the concrete mechanism
that makes this possible in practice: it undermines the older view that
architecture must be substantially finished before coding starts, since on
that view architecture can only decay afterward through carelessness.
Refactoring instead enables continuous architectural revision on running,
years-old production software — the same behavior-preserving discipline
that lets you improve a single function safely also scales up to revising a
system's structure over time. [YAGNI](yagni.md) is the design posture this
capability licenses: build only for currently-understood needs, and refactor
the architecture as understanding grows, rather than guessing at flexibility
up front.
