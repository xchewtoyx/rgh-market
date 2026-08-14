---
type: concept
title: Backward and Forward Compatibility During Rollout
description: >
  A rolling deployment forces old and new code to read each other's data
  simultaneously, so a safe schema or wire-format change must satisfy both
  compatibility directions at once, not just one.
sources:
  - title: "Designing Data-Intensive Applications"
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 4"
---

# Backward and Forward Compatibility During Rollout

Two distinct compatibility properties are easy to conflate but protect
against opposite failures:

- **Backward compatibility**: newer code can read data written by older
  code. This is the easy direction — new code can be written with explicit
  handling for the old shape.
- **Forward compatibility**: older code can read data written by newer
  code. This is the hard direction — old code, already deployed and
  unaware the new fields exist, has to cope with them anyway (typically by
  ignoring unknown fields, per the [tolerant reader pattern](tolerant-reader-pattern.md)).

A [rolling deployment](rolling-deployment.md) needs *both* directions to
hold simultaneously, not just one, because for the whole duration of the
rollout old and new instances are running side by side and reading each
other's output: messages one service produces and another consumes,
records one version writes to a shared store and another later reads back.
Getting only backward compatibility right is not enough — it protects the
new code from old data, but says nothing about what happens when old code
downstream of the new code encounters a payload it wasn't written to
understand.

This is why schema-evolution rules in wire formats (optional fields with
defaults, never reusing or repurposing a field identifier, additive-only
changes for anything short of a major version) exist specifically to keep
both directions true throughout a deploy window — the same discipline that
[expand-and-contract schema migration](expand-and-contract-schema-migration.md)
applies at the database layer and [parallel API version coexistence](parallel-api-version-coexistence.md)
applies at the service-contract layer.

A rollback is a special case worth calling out on its own: it reintroduces
old code but does not undo data already written by the new code, so a
rollback specifically depends on forward compatibility holding for
whatever the new version already wrote before the rollback happened — see
[progressive rollout data-layer isolation](progressive-rollout-data-layer-isolation.md)
for a case where missing forward compatibility turned a rollback into a
worse outage than the one it was meant to fix.
