---
type: concept
title: Data Mesh Domain Data Types (Source-Aligned, Aggregate, Consumer-Aligned)
description: >
  The three roles a domain's analytical data product can play in a data mesh
  — origin, cross-domain combination, or consumer-specific fit — and why
  telling them apart matters for pipeline ownership.
sources:
  - title: Deciphering Data Architectures
    resource: "Deciphering Data Architectures (Serra), ch. 13"
---

Under [data mesh](data-mesh.md)'s domain-ownership principle, not every
domain's analytical data plays the same role. Dehghani names three:

- **Source-aligned domain data** sits closest to where data originates: a
  domain copies its own operational systems' data and transforms it into
  general-purpose analytical form, without shaping it for any one consumer.
  A domain can draw on more than one operational source, and sometimes on
  other domains' data too. The hard part is usually organizational, not
  technical: if the company is currently divided into *application* domains
  (one per system) rather than *business* domains (one per business
  capability), a single business domain's pipeline may need to ingest from
  several applications' operational databases at once.
- **Aggregate domain data** combines two or more other domains' data,
  typically for query performance — building an easier-to-use, pre-joined
  model rather than forcing every consumer to join source-aligned domains
  live, which gets slow once domain data lives in physically separate
  stores. This is the mesh's analogue of a [conformed](conformed-dimension-publish-subscribe.md)
  cross-domain rollup: a customer-360 domain assembling demographic,
  behavioral, transactional, and feedback data from many source-aligned
  domains — and running it through [deduplication and survivorship](deduplication-and-survivorship.md)
  once, centrally — is a canonical aggregate domain, replacing every
  consuming domain independently pulling and mastering the same customer
  data itself. Building an aggregate domain across independently-owned
  source-aligned domains surfaces the same
  [surrogate-vs-business-key](surrogate-vs-business-keys.md) problem a
  single warehouse has when it conforms multiple source systems, at larger
  scale: without a coordinated identifier scheme, two domains can each mint
  the "same" customer or product ID for two different real entities,
  silently corrupting counts and sums the moment the aggregate domain joins
  across them. The fix is the same class of solution — a shared GUID scheme,
  a centralized ID-issuing service, or per-domain code namespacing — agreed
  on before domains start minting IDs independently, since retrofitting ID
  coordination after collisions already exist means reconciling every
  affected fact row after the fact.
- **Consumer-aligned domain data** reshapes a source-aligned domain's data
  for a specific downstream audience — almost always derived from a
  source-aligned domain, not from raw operational systems directly.
  Manufacturing data modeled with manufacturing jargon for manufacturing
  staff (source-aligned) versus the same data simplified and de-jargoned for
  outside departments or for training an ML model (consumer-aligned) is the
  standard example.

For a pipeline engineer, the practical payoff of naming these three
separately is knowing where a given pipeline's output actually sits: a
pipeline feeding a consumer-aligned domain has a narrower, more opinionated
contract with one audience, while a source-aligned domain's pipeline is
deliberately kept general because it doesn't yet know every future consumer.
Getting this wrong up front is expensive to fix — redesigning domain
boundaries months into a mesh rollout, once dozens of pipelines already
depend on the original boundaries, costs far more than getting the split
right before build starts.
