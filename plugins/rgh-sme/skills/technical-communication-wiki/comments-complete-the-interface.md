---
type: concept
title: Comments Complete the Interface
description: >
  A structural signature alone can't convey behavior, meaning, or
  constraints, so a reader who has to read the underlying implementation
  to use something correctly has been handed an incomplete abstraction,
  not a self-explanatory one.
sources:
  - title: "A Philosophy of Software Design"
    resource: "A Philosophy of Software Design (John Ousterhout), ch. 12"
---

"Good code is self-documenting" is a comforting claim that doesn't survive contact with what an interface actually needs to convey. Strong naming and clean structure reduce how much explanation is needed, but they cannot eliminate the need for it, because a large share of what a reader has to know to use something correctly simply has no home in its formal structure at all: a function signature can state parameter and return types, but it can't state what a boundary value does, what a result actually means, why a particular approach was taken, or under what conditions the thing should be called at all. That informational gap doesn't close itself just because the surrounding code is well written — it has to be filled explicitly, in prose, or it isn't filled.

The tempting alternative — "if you need to know how it behaves, go read the implementation" — feels like it saves the writer work, but it doesn't actually work at scale. Reading an implementation to reconstruct its behavior is slow, error-prone, and doesn't compose: understanding one piece this way usually means having to first understand everything it calls, all the way down. It also rewards the wrong incentive — if a reader is expected to read the source to understand something, there's no real pressure to keep any single explanation self-contained, and structure fragments into pieces that are only meaningful together. A description that requires reading the thing being described isn't a description; it's a promise that a real explanation exists somewhere for anyone willing to reconstruct it themselves.

This is why a bare signature or heading is not, by itself, a finished abstraction — see [labeling systems for clarity](labeling-systems-for-clarity.md) for the parallel point that a label alone can only compress so much before a reader needs the fuller text behind it. The explanation that completes an abstraction is deliberately written in plain prose rather than a rigid or formal notation, not because prose is more rigorous — it usually isn't — but because it's more expressive: it can carry a nuance, an exception, or a piece of rationale that no fixed notation would have a slot for.
