---
type: concept
title: Interface and Implementation Should Have Different Abstractions
description: >
  A class's public interface should normally look different from its
  internal representation; if they share the same abstraction, the class
  probably isn't very deep.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 7"
---

This is [different layer, different abstraction](different-layer-different-abstraction.md)
applied to a single class's own boundary: interface on one side, private
representation on the other, and they should not mirror each other.

Worked example: a text-editor class storing text internally as separate
lines, whose public API also exposed a line-oriented interface (`getLine`,
`putLine`) matching that internal structure directly. This made the class
[shallow](shallow-modules.md) and awkward, because higher-level UI code
routinely needs to insert mid-line or delete across line boundaries — forcing
every caller to manually split and join lines, duplicating that logic across
the UI layer.

The fix keeps the line-based internal storage but exposes a
**character-oriented** interface instead (`insert`/`delete` over arbitrary
text ranges or positions, potentially spanning newlines). All line-splitting
and line-joining complexity moves inside the text class — deepening it — and
every caller gets simpler. The gap between the character-oriented interface
and the line-oriented internals *is* the class's value: it's exactly the
functionality [information hiding](information-hiding.md) is supposed to
provide.
