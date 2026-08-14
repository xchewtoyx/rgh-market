---
type: concept
title: Backward vs. Forward Schema Compatibility
description: >
  The precise, non-symmetric definitions behind "backward compatible" and
  "forward compatible," and the reader/writer schema mechanism a schema
  registry uses to resolve them.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 4"
---

"Backward compatible" and "forward compatible" get used loosely, but they
name two distinct, non-symmetric properties, and a pipeline needs to know
which one a given rollout actually requires:

- **Backward compatibility**: newer code can read data written by older
  code. This is the easier direction — new code can be written to explicitly
  understand and handle whatever the old, already-known format looked like.
- **Forward compatibility**: older code can read data written by newer code.
  This is harder, because the old code has to gracefully ignore fields or
  structure it was never written to know about, rather than erroring on
  seeing something unfamiliar.

Both directions matter in practice because of **rolling upgrades**: deploying
a code change incrementally across nodes creates a window where old and new
versions run simultaneously against the same data — a consumer on the old
code version may read a message a newer producer just wrote (needs forward
compatibility), and a consumer on the new code version may read data a
not-yet-upgraded producer wrote (needs backward compatibility). A schema
change that's only backward compatible will work fine once every producer
has upgraded, but breaks any consumer still running old code during the
rollout window itself.

**How a [schema registry](schema-registry.md) resolves this mechanically**:
a message carries (or references) the **writer's schema** — whatever schema
the producer that encoded it was using — and the consumer decodes using its
own **reader's schema**. The registry's job is letting a consumer look up
the specific writer's schema a given message was encoded with (by version ID
embedded in the message), then resolving field-by-field differences between
the writer's and reader's schemas by matching on field name — a new field the
reader's schema doesn't know about is dropped, and a field the reader expects
but the writer's schema doesn't have falls back to a declared default. This
is precisely why schema evolution rules for a format like Avro or Protobuf
boil down to a short list of hard constraints: new fields need a default
value (or must be optional), and an identifier (a field tag or field name) 
must never be reused for a different meaning once retired — violating either
constraint breaks the matching-and-fallback resolution the registry relies
on to make old and new schemas cooperate at all.
