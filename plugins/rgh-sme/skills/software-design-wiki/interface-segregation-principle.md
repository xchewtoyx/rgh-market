---
type: concept
title: Interface Segregation Principle
description: >
  When a large class's clients each use only a slice of its public surface,
  give each group its own narrower interface onto the same class — clients
  no longer see methods they don't use, and no longer recompile whenever
  unrelated parts of the class change.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 20"
---

A useful diagnostic before reaching for this: try to state a class's job in
one sentence. If you keep needing to append more clauses ("it does this, and
this, and this..."), you've likely found several responsibilities rather
than one. This can show up at two different levels, and they call for
different fixes:

- **Interface-level violation** — the public surface itself implies many
  unrelated duties (a bloated interface that reads like several classes'
  worth of methods stitched together).
- **Implementation-level violation** — whether the class actually *does* all
  that work internally, or is really just delegating to smaller classes
  already (i.e. it's a facade). This is the more important one to fix
  first, since a delegating facade is "easier to manage" even while its
  interface still looks large from the outside — see
  [extracting a class without tests](extract-class-without-tests.md) for
  how to get there incrementally.

**The Interface Segregation Principle**: "When a class is large, rarely do
all of its clients use all of its methods... If we create an interface for
each of these groupings... each client can see the big class through that
particular interface... The clients no longer have to recompile whenever
the large class does." Fixing the interface-level violation this way means
identifying whether some of the classes a large class already delegates to
internally could be handed to clients **directly**, through client-specific
narrower interfaces, rather than routing every client through the one large
class's full surface.

The natural end-state of pursuing this is inverting the relationship
entirely: instead of the big class delegating out to some controller
object, a standalone controller delegates *into* the now-smaller original
class, letting genuinely control-specific methods migrate off of it
altogether. This is harder than it sounds in practice: it typically requires
temporarily exposing more of the original class's internals so the new
front-end class has what it needs, and every client has to be migrated
(safely, meaning under test) to the new class one at a time.
