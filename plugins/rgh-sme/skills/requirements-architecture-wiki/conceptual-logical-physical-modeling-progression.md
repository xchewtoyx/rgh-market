---
type: concept
title: Conceptual, Logical, and Physical Modeling Progression
description: >
  A data model matures through four distinct stages — conceptual, logical,
  physical, transformational — each adding detail the previous stage
  deliberately omitted, so the right level of technicality reaches the
  right audience at each point.
sources:
  - title: Data Modeling with Snowflake
    resource: "Data Modeling with Snowflake (Serge Gershkovich), ch. 2"
---

A [data model view](data-model-view.md) is not produced in one pass; it
matures through four stages, each adding detail the previous one
deliberately left out so the model stays readable by the audience that
needs it at that point:

- **Conceptual** — business-facing and collaborative, not a technical
  exercise. Identifies entities, their relationships, and enough
  granularity (cardinality, optionality) to state a rule like "a superhero
  must have exactly one superhero type," without yet fixing data types or
  keys. Produced *with* business stakeholders, not delivered to them —
  the diagram is a by-product; the real value is the conversation that
  surfaces disagreements about what the business actually does, which is
  exactly the discovery this stage exists to force. A model inferred only
  from a data sample rather than validated against the actual business
  rule risks generalizing wrong from too little evidence — see
  [requirements are discovered, not
  gathered](requirements-discovery-vs-gathering.md) for the general
  version of this failure mode.
- **Logical** — adds the technical detail a business audience doesn't
  need but a database design does: data types, unique identifiers,
  subtype/supertype inheritance, and resolving many-to-many relationships
  into an explicit associative structure — while staying database-agnostic,
  not yet committed to any specific engine's syntax or storage.
- **Physical** — the deployable blueprint for a specific database
  platform: native types, constraints, indexing/clustering, and other
  engine-specific properties. This is where [architecture modeling
  notations](architecture-modeling-notations.md) stop being illustrative
  and start being literally implementable. An existing, undocumented
  schema can be reverse-engineered back into a physical (and partially
  logical) model — a fast way to recover documentation for a system that
  never had it, though naming-pattern-inferred relationships lack the
  business context a real logical model would have carried.
- **Transformational** — covers derived data: views, `CREATE TABLE AS
  SELECT`, and other logic that reshapes already-structured data into new
  structures for a specific business question. Unlike the other three
  stages, a diagram alone doesn't tell the full story here — a lineage
  diagram (source-to-target column mapping) shows *what* moved where, but
  only the accompanying SQL shows *how* and *why*, so this stage's
  documentation pairs a lineage graph with the transformation code itself
  rather than relying on either alone.

Each stage answers a different question — what does the business consist
of, how is that expressed as data, how is that data actually stored, and
how is stored data reshaped for use — and skipping a stage (jumping
straight from a business conversation to physical DDL) tends to produce a
model that is technically deployable but never actually validated against
the business rule it was supposed to encode.

Tooling that keeps all three structural stages as [views](view-and-viewpoint.md)
over one underlying model — rather than three separately hand-drawn
diagrams — avoids the specific failure mode of a conceptual diagram
quietly drifting out of sync with the physical schema it was supposed to
describe, since there is only one model to update and each stage is just a
different level of detail shown from it.
