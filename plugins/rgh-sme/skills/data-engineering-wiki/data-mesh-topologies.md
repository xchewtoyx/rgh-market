---
type: concept
title: Data Mesh Infrastructure Topologies (Type 1–3)
description: >
  Three levels of technology decentralization a self-serve data mesh
  platform can adopt, trading operational simplicity against domain
  autonomy.
sources:
  - title: Deciphering Data Architectures
    resource: "Deciphering Data Architectures (Serra), ch. 13"
---

[Data mesh](data-mesh.md)'s "self-serve infrastructure as a platform"
principle still leaves open how much technology domains actually share.
Three topologies sit on a spectrum from centralized control to decentralized
agility:

- **Type 1**: every domain runs the same shared technology stack (one cloud
  provider's storage, pipeline tooling, security, warehousing, reporting,
  [catalog](data-catalog.md), MDM, virtualization, APIs, ML), and each
  domain has its own infrastructure *except* storage — instead of separate
  per-domain
  [data lakes](data-lake-architecture.md), one enterprise lake holds each
  domain in its own container or folder, logically separate but physically
  unified. This is the most commonly adopted topology in practice: it avoids
  the query-performance penalty of joining across physically distant lakes,
  and keeps security, monitoring, and disaster recovery centralized to one
  system instead of many.
- **Type 2**: the same shared technology stack as Type 1, but each domain
  also gets its own *physical* data lake — genuinely decentralized
  infrastructure, at the cost of the technical work needed to link separate
  lakes together and still get acceptable cross-domain query performance.
- **Type 3**: each domain picks any technology and any cloud provider it
  wants, including its own data lake on whatever platform fits — one domain
  on Azure Synapse, another on SQL Server in a VM, another on AWS or GCP
  entirely. This is the "pure" decentralization the original data mesh
  concept describes, and it comes with a matching list of costs: divergent
  security models per domain, needing specialist staff across many products
  and clouds, building governance standards that still hold across that
  variety (the mesh's federated-governance principle gets harder, not
  easier, the more heterogeneous the stack), building shared infrastructure
  automation flexible enough to span it, and combining data across
  fundamentally different products and clouds when an aggregate domain needs
  to.

Choosing a topology is really choosing how much of the mesh's promised
domain autonomy an organization is actually willing to pay for in
operational complexity. Type 1 delivers most of data mesh's organizational
benefit (domain ownership, self-serve access) while keeping the technical
footprint close to a single [modern data warehouse](modern-data-warehouse-architecture.md)
or [lakehouse](data-lakehouse.md) platform's operability; Type 3's full
technology autonomy is rarely worth its governance and staffing cost, which
is why implementations converge on Type 1 or 2 far more often than on Type 3
in practice.
