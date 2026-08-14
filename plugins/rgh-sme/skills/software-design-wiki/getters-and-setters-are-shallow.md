---
type: concept
title: Getters and Setters Are Shallow Methods
description: >
  Paired accessor methods are, at best, damage control for a class that has
  already decided to expose implementation state — the better fix is not to
  expose instance variables at all.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 19"
---

The common Java-community pattern of paired `getFoo`/`setFoo` accessor
methods around an instance variable isn't strictly required, since a field
could simply be made public — the argument in favor is that accessors leave
room to later add logic (updating derived values, notifying listeners,
enforcing constraints) without changing the class's external interface, even
if that logic isn't needed on day one.

The better position is not to expose instance variables in the first place.
Getters and setters are, at best, damage control for a class that's already
decided to expose implementation state — the exposure itself violates
[information hiding](information-hiding.md) and swells interface complexity,
since part of the internal implementation becomes externally visible
regardless of whether it's mediated by an accessor method. Getters and
setters are themselves classic [shallow methods](shallow-modules.md),
typically a single line each — pure interface surface with essentially no
functional depth, cluttering the class's interface without meaningfully
hiding anything. This is a direct instance of the meta-risk in
[design patterns](design-patterns-as-reusable-solutions.md) generally: once a
pattern becomes established as "good," developers tend to overuse it
reflexively, which is the direct cause of getter/setter overuse across the
Java ecosystem.
