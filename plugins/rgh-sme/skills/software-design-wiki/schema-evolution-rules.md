---
type: concept
title: Schema Evolution Rules for Structured Data Formats
description: >
  Concrete rules that let a structured data schema change over time without
  breaking readers or writers on either version — never repurpose a field
  identifier, add new fields as optional with defaults, and never make
  removing a field silently unsafe.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 4"
---

When a structured data format (a schema-driven wire format, a persisted
record format, a serialized message) needs to change, a handful of
concrete rules deliver [backward and forward
compatibility](backward-and-forward-compatibility.md) simultaneously,
rather than leaving compatibility to be discovered by trial and error:

- **A field's identifier must never change or be reused for a different
  meaning.** Whether the identifier is a name or a numeric tag, once
  something has been written to storage or sent over the wire under that
  identifier, every future reader needs it to mean the same thing forever
  — reusing a retired identifier for a new, unrelated field silently
  corrupts old data being reinterpreted through the new definition.
- **New fields must be added as optional, with a sensible default,** never
  as required. A reader running old code that predates the field simply
  never sees it (forward compatibility); a reader running new code against
  older data that lacks the field falls back to the default (backward
  compatibility). A field added as *required* breaks exactly the old
  writers who could never have populated it.
- **A field can only be removed if it was already optional**, and its
  retired identifier must never be reused — removing a field that was
  required breaks every reader still expecting it to be present.
- **Unrecognized fields must be preserved, not silently dropped**,
  especially through any read-modify-write cycle: if an older reader loads
  a record containing fields it doesn't recognize (because a newer writer
  added them), modifies some other field, and writes the record back, the
  fields it didn't understand must still be there afterward. Silently
  stripping unknown data on every pass through old code is a slow, easy-to-
  miss way to lose information that newer code depends on.

These rules generalize past wire formats and databases to any structured
contract that outlives a single version of the code reading or writing it
— they're the mechanical discipline underneath the [extension technique of
interface evolution](interface-evolution-deprecation-versioning-extension.md):
"leave the original untouched, add new resources alongside it" only
actually delivers compatibility if the addition itself follows rules like
these.
