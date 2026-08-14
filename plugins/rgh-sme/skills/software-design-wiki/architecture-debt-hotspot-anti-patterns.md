---
type: concept
title: "Architecture Debt Hotspots: Six Multi-File Anti-Patterns"
description: >
  Six recurring, automatically-detectable coupling and cohesion failures
  that disproportionately drive maintenance cost when they involve a
  cluster of files rather than a single one — each pointing to a specific,
  targeted remediation.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th ed. (Bass, Clements, Kazman, with Yuanfang Cai), ch. 23"
---

Where a [code smell](red-flags-as-design-smells.md) typically flags a
problem inside one file or class, these six anti-patterns flag a problem
in the *relationship* between several — a **hotspot** is a cluster of
mutually coupled files, decoupled from the rest of the system, that
together carry a disproportionate share of a codebase's bugs and change
cost. Each anti-pattern implies a different, targeted fix rather than a
generic "reduce coupling" instruction:

- **Unstable interface** — an influential file representing an important
  service or abstraction that changes frequently alongside its many
  dependents. A large dependent count paired with frequent co-modification
  means the "interface" isn't actually stable enough to insulate callers
  from its changes — the whole point of an interface in the first place.
- **Modularity violation** — structurally independent files (no call or
  inheritance relationship) that nonetheless change together often; see
  [evolutionary coupling](evolutionary-coupling.md) for the diagnosis and
  fix — an unencapsulated shared secret needs an explicit owning
  abstraction.
- **Unhealthy inheritance** — a parent class depending on its own child, or
  a client depending on both a parent and one of its children at once.
  Either inverts or blurs the intended direction of an inheritance
  hierarchy, where a parent is supposed to be usable — and understandable
  — without knowing anything about its children. Remediation is usually
  relocating the dependent functionality from child up to parent, removing
  the parent's dependency on the child entirely.
- **Cyclic dependency / clique** — a set of files whose structural
  dependencies form a cycle: a path exists from any member back to any
  other. Cycles spanning many files are effectively impossible for any one
  person to hold in mind, and won't be visible without tooling to detect
  them. Remediation: break the clique by removing or reversing one
  dependency in the cycle.
- **Package cycle** — the same clique pattern one level up, at the package
  or module level, where packages depend on each other rather than forming
  a clean, acyclic hierarchy.
- **Crossing** — a file with both high fan-in and high fan-out (many
  dependents *and* many dependencies) that also co-changes substantially
  with both groups — sitting at a genuine traffic intersection in the
  architecture, where a large share of the system's total change activity
  has to pass through one place.

Not every file inside a hotspot need be tightly coupled to every other file
in it — the cluster as a whole is what's decoupled from the rest of the
system, and each cluster is a distinct, separately prioritizable
refactoring candidate. Because each anti-pattern has a specific structural
signature, all six are automatable: a file's participation can be scored
directly from structural dependency data plus [evolutionary
coupling](evolutionary-coupling.md) data mined from revision-control
history, without a human having to spot the pattern by inspection first —
see [quantifying refactoring ROI](quantifying-refactoring-roi.md) for
turning that participation score into a prioritized, business-justified
refactoring plan.
