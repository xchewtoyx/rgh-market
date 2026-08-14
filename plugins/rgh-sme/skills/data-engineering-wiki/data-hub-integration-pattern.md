---
type: concept
title: Data Hub Integration Pattern
description: >
  A centralized exchange point that replaces point-to-point interfaces
  between operational systems, distinct from a lake or warehouse because its
  job is distribution, not analytics.
sources:
  - title: Deciphering Data Architectures
    resource: "Deciphering Data Architectures (Serra), ch. 6"
---

A **data hub** collects, integrates, and redistributes data among systems,
with a purpose distinct from either a [data lake](data-lake-architecture.md)
or a [warehouse](data-warehouse-architecture.md): those two exist primarily
to serve analytics, while a hub exists primarily to be a communication and
exchange point *between operational systems themselves*, with analytics as a
secondary consumer at most. Its core payoff is structural: without a hub, N
systems that all need to exchange data with each other require on the order
of N² point-to-point interfaces; routing every exchange through one central
hub instead collapses that to N connections, one per system, each pointed at
the hub rather than at every other system individually.

A hub typically stores data raw or only lightly processed, leaves most
transformation and analysis to external tools rather than doing it
internally (unlike a warehouse's extensive in-place ETL), and is more likely
than a lake to ship with built-in cataloging, [lineage](data-lineage.md),
and access-control capabilities rather than depending on third-party
tooling bolted on afterward. It commonly spans a wider mix of underlying storage technologies
than a lake or warehouse does — relational databases, NoSQL stores, and lake
storage combined — because its job is fitting whatever storage each
connected operational system already uses, not standardizing on one.

Hubs, lakes, and warehouses are complementary rather than substitutes: a hub
is often deployed alongside both, acting as the intermediary layer for
exchange and governance while the lake and warehouse continue doing the
analytical work a hub isn't built for. A related but distinct concept worth
naming for contrast: a **data marketplace** handles data buying, selling, and
sharing *across organizations*, stores no data of its own, and can itself be
fed from a hub — the hub manages distribution within an organization, the
marketplace handles commercial exchange across organizational boundaries.
