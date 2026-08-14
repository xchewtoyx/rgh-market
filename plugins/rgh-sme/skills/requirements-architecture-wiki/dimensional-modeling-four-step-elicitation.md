---
type: concept
title: Dimensional Modeling's Four-Step Elicitation Method
description: >
  Kimball's four-step method — business process, grain, dimensions, facts
  — structures requirements-discovery workshops for an analytical data
  model, and its outputs should be treated as a binding contract between
  business and technical teams because later stages are expensive to
  unwind.
sources:
  - title: Data Modeling with Snowflake
    resource: "Data Modeling with Snowflake (Serge Gershkovich), ch. 7"
---

A specialized [elicitation technique](requirements-elicitation-techniques.md)
for the specific case of building an analytical (data warehouse) model,
run as facilitated workshops with business stakeholders in a fixed order:

1. **Define the business process** — the natural transactions the business
   performs (selling, registering, manufacturing), starting from the core
   function and radiating out to supporting ones until every relevant
   department is represented.
2. **Declare the grain** — the lowest level of detail meaningful for
   analyzing that process. Default to **atomic grain** (the lowest level
   the process itself actually captures) rather than a pre-aggregated
   level, because building at atomic grain future-proofs the model against
   rollup requirements nobody has asked for yet, whereas building
   pre-aggregated forecloses them. A single table must never mix grains —
   discovering this only after data is flowing is expensive to unwind.
3. **Identify the dimensions** — the who/what/where entities the grain
   discussion surfaces (customers, products, locations), which become the
   descriptive tables surrounding the eventual fact table.
4. **Identify the facts** — the metrics recorded at the intersection of
   the process and its dimensions.

The four steps are deliberately sequential and each depends on the last
being settled first, mirroring the general discipline that a
[requirement should be separated from the design decision that satisfies
it](requirement-vs-design-decision.md) — grain is a requirements question
("what does the business need to distinguish"), not a storage-efficiency
question, and answering it well before physical design begins is what
lets the later [conceptual, logical, and physical modeling
stages](conceptual-logical-physical-modeling-progression.md) proceed
without re-litigating the process/grain/dimension/fact decisions each time.

The outputs of these workshops should be treated as **binding contracts**
between business and technical teams, on the same footing as any other
[requirement rationale](requirement-rationale.md) capture — grain and fact
definitions are exactly the kind of decision that is cheap to get right
during elicitation and expensive to discover wrong once a fact table is
already loaded and downstream reports depend on its shape.

The same method also runs in reverse against an *existing*, undocumented
physical schema: reverse-engineer table structure into candidate
dimensions and facts by naming convention and constraint inspection, then
take the resulting draft back to the business as a hypothesis to confirm
or correct — going from "what is" to "what ought to be." Data alone can
never conclusively confirm a grain or a business-process boundary; a table
with no duplicate values under a candidate key is suggestive, not proof,
and only the domain expert can settle whether two superficially similar
fact tables actually represent one business process or two.
