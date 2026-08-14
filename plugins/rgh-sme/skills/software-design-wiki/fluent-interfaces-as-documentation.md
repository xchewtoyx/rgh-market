---
type: concept
title: "Fluent Interfaces: Vocabulary Instead of Indirection"
description: >
  A fluent interface or internal DSL renders a call as something close to a
  domain sentence, but it only earns its keep where the vocabulary actually
  clarifies the domain — reached for reflexively, it adds indirection that
  hides ordinary code instead.
sources:
  - title: Living Documentation
    resource: "Living Documentation (Martraire), ch. 8"
---

A fluent interface — a chain of method calls designed to read almost like a
sentence in the problem domain (`order.shippingTo(address).withPriority()`)
— is a way of putting documentation directly into the call site itself,
rather than requiring a comment alongside it. When the chained vocabulary
genuinely matches how domain experts talk about the operation, this can
make an interface's [common case simple](interfaces-should-make-the-common-case-simple.md)
to both write and read, functioning as documentation that's checked by the
compiler rather than prose that can drift.

The risk is reaching for the style reflexively rather than where it earns
its keep. A fluent chain still has to compile to ordinary method calls
underneath, and building one — usually via a builder object accumulating
state across each chained call — adds a layer of indirection between the
call site and what actually happens. Where the resulting vocabulary
doesn't map cleanly onto how the domain is actually discussed, that
indirection is pure cost: harder to step through in a debugger, harder to
search for call sites of a specific underlying operation, and no clearer
to a reader than the plain method call it's hiding. The judgment call is
the same one behind any [design infrastructure](design-cost-benefit-of-infrastructure.md):
build the fluent surface only where its vocabulary removes more confusion
than the builder machinery underneath it costs to understand, not as a
default style choice applied uniformly across an interface.
