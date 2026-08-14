---
type: concept
title: Splitting and Joining Methods
description: >
  Two legitimate ways to split a method exist — extracting a cleanly
  separable child, or splitting into two independently useful methods — and
  joining shallow methods back together is often the better move.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 9"
---

Given that [method length alone isn't a good reason to split](method-length-is-not-a-design-criterion.md),
two techniques do justify a split:

- **Extract a subtask into a child method.** Valid when the subtask is
  cleanly separable: the child needs no knowledge of the parent, and the
  parent needs no knowledge of the child's implementation — only its
  interface — so the parent's own external interface stays unchanged. A good
  sign the split works: the child method could plausibly be reused elsewhere
  (it's naturally somewhat [general-purpose](general-purpose-modules-are-deeper.md)).
  If you keep flipping between parent and child to understand either, the
  split was a mistake — see [conjoined methods](conjoined-methods.md).
- **Split into two separate, both-externally-visible methods.** Valid when
  the original method's interface was overloaded because it did multiple,
  not-closely-related things; the split should make *each* resulting
  method's interface simpler than the original, and ideally most callers only
  need to call one of the two. If callers routinely have to call both and
  pass state between them, the split is probably a bad idea — it degenerates
  into two [shallow](shallow-modules.md) methods. This form of split is less
  often a good idea than extracting a child method; judge it strictly by
  whether it genuinely simplifies things for callers.

Joining methods can simplify a system just as much as splitting one: replacing
two shallow methods with one deeper one can eliminate code duplication,
remove [dependencies](dependencies-as-a-cause-of-complexity.md) or
intermediate data structures between the originals, consolidate knowledge
that was scattered across multiple places into one, or produce a simpler
overall interface (see [better together or apart](better-together-or-apart.md)).
