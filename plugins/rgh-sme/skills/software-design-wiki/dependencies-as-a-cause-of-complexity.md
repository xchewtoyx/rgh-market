---
type: concept
title: Dependencies as a Cause of Complexity
description: >
  A dependency exists when a piece of code cannot be understood or modified
  in isolation, and dependencies are one of the two underlying causes of
  software complexity.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 2"
---

Dependencies are unavoidable, and even intentional — every class's public API
is a dependency that its callers take on deliberately. The design goal is not
to eliminate dependencies but to minimize how many of them exist and to make
the ones that remain as simple and obvious as possible.

A method signature is a dependency between an implementation and every call
site: add a parameter, and every invocation must be updated. This is exactly
the mechanism behind [change amplification](change-amplification.md) and
contributes to [cognitive load](cognitive-load.md) — the more dependencies
touch a piece of code, the more places a change has to account for and the
more a developer has to hold in mind. [Coupling](coupling.md) is the
formal, probabilistic face of the same phenomenon: the likelihood that a
change to one module requires a change to another.

The banner-color example is again illustrative: hardcoding a background color
on every page created a hidden dependency among all of the pages (they all had
to agree on the same value). Centralizing it into a shared variable plus an
API didn't remove the dependency — every page still depends on that one
value — but it made the dependency single, explicit, and enforceable (a
compiler or linter can catch a stale reference to a renamed variable; it
can't catch a hardcoded value drifting out of sync).
