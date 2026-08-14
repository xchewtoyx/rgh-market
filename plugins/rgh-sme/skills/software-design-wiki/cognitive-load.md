---
type: concept
title: Cognitive Load (Software Design)
description: >
  Cognitive load is the complexity symptom measuring how much a developer
  must know to correctly complete a task in a given piece of code.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 2"
---

Higher cognitive load means more time spent learning the information needed
to make a change safely, and higher risk of bugs from missing something that
mattered. A concrete example: a C function that allocates memory but expects
the *caller* to free it raises cognitive load on every caller and creates an
ongoing risk of memory leaks — better for the same module to take
responsibility for freeing what it allocates, so callers don't have to know or
remember the rule.

Common sources of cognitive load: APIs with many methods to learn, global
variables, inconsistent conventions, and dense webs of inter-module
[dependencies](dependencies-as-a-cause-of-complexity.md).

Cognitive load is not the same thing as lines of code, and equating the two is
a mistake: a short implementation built on a framework or a clever one-liner
can carry far higher cognitive load than a longer, more explicit one, if it's
unclear what those few lines actually do. Sometimes more lines really is
simpler. The opposite of high cognitive load (together with low
[unknown unknowns](unknown-unknowns.md)) is an
[obvious system](code-obviousness.md): one where a developer can guess
what to do quickly and be confident the guess is right.

Cognitive load is one of the three observable symptoms of
[complexity](complexity.md), alongside
[change amplification](change-amplification.md) and
[unknown unknowns](unknown-unknowns.md).
