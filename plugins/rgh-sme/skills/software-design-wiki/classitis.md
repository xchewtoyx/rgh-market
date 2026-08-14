---
type: concept
title: Classitis
description: >
  Classitis is the pathological belief that if classes are good, more and
  smaller classes must be better — it produces many shallow classes whose
  accumulated interfaces raise system-level complexity even though each
  individual class looks simple.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 4"
---

Conventional wisdom that classes and methods should be small — sometimes
codified as hard line-count thresholds as low as ten lines — pushes toward
[shallow modules](shallow-modules.md). Each small class contributes little
functionality but still carries its own interface and boilerplate; those
interfaces accumulate into large system-level complexity even as each
individual unit remains easy to read in isolation, and the overall style
becomes verbose.

Java's `FileInputStream` → `BufferedInputStream` → `ObjectInputStream`
composition is a canonical classitis example baked into standard-library
culture (not a language requirement). Buffering is wanted almost universally,
yet must be requested by explicitly constructing an extra wrapper object;
forgetting it silently degrades I/O performance with no error, and the first
two intermediate objects become dead references once the third is built. See
[interfaces should make the common case simple](interfaces-should-make-the-common-case-simple.md)
for the contrasting design that avoids this trap.
