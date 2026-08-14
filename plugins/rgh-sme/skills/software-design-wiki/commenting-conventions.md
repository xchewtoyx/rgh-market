---
type: concept
title: Commenting Conventions and the Four Comment Categories
description: >
  Settling on a fixed set of commenting conventions gives consistency and a
  forcing function, and comments fall into four categories with very
  different importance: interface, data-structure member, implementation,
  and cross-module.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 13"
---

If a doc-generation tool exists for your language (Javadoc, Doxygen, godoc),
follow its conventions even though none are perfect — the tooling benefit
outweighs any convention quirks. Absent existing conventions, borrow from a
similar language or project rather than inventing from scratch, to ease
cross-developer understanding. Conventions serve two purposes: consistency
(easier to read across a codebase) and a forcing function — without a clear
plan for what and how to comment, it's easy to end up writing nothing.

Four categories, in descending order of importance:

1. **Interface** — precedes a class, function, or method declaration,
   describing the module's [interface and abstraction](module-interface-and-implementation.md).
   See [interface documentation](interface-documentation.md).
2. **Data structure member** — next to a field declaration.
3. **Implementation** — inside a method body, explaining internal workings.
   See [implementation comments](implementation-comments.md).
4. **Cross-module** — documents dependencies spanning module boundaries; the
   rarest and hardest to write, but very important when needed. See
   [cross-module design decisions](cross-module-design-decisions.md).

Interface and data-structure-member comments are the most important: every
class needs an interface comment, every class variable needs a comment, every
method needs an interface comment (rare, obvious exceptions like some
getters/setters aside — but it's easier to comment everything by default than
to keep second-guessing necessity case by case). Implementation comments are
frequently unnecessary.
