---
type: concept
title: Design for Ease of Reading, Not Ease of Writing
description: >
  A convenience that saves the writer a few keystrokes, like a generic
  container in place of a purpose-specific type, costs every future reader —
  and the reader's time should win that trade almost every time.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 18"
---

Generic containers (Java's `Pair`, C++'s `std::pair`) are tempting for
bundling multiple return values quickly —
`return new Pair<Integer, Boolean>(currentTerm, false);` — but the resulting
accessor calls (`result.getKey()`, `result.getValue()`) carry zero semantic
meaning about what's actually inside. A reader has no way to tell what a
"key" or "value" represents here without chasing the call site. The fix is a
small, purpose-specific class or struct instead, with meaningful field names
and room for its own documentation — something a generic container
structurally cannot offer.

This generalizes to an explicit design maxim: software should be designed
for ease of reading, not ease of writing. A generic container is a
convenience for the person typing the code in the moment, at the direct
expense of every future reader; the few extra minutes spent defining a
specific type is clearly worth that trade, because code is read far more
often than it's written. This is the same underlying priority behind
[precise names](precise-names.md) and
[comments written for a first-time reader](comments-describe-non-obvious-things.md).
