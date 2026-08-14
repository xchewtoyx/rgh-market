---
type: concept
title: Blue-Green Migration for Stateful Infrastructure
description: Extending the blue-green change pattern to databases and other stateful resources with an explicit replicate, dual-write, then cut-over-reads-then-writes sequence, rather than a single traffic-switch moment.
sources:
  - title: Infrastructure as Code Patterns and Practices
    resource: "Infrastructure as Code, Patterns and Practices (Rosemary Wang), ch. 9"
---

A [blue-green change](blue-green-infrastructure-change.md) for stateless infrastructure is a single moment of cutover: build the new instance, redirect traffic, tear down the old one. Stateful infrastructure — a relational database, an object store, a message queue — can't do this in one step, because the new (green) instance starts out with none of the data the old (blue) instance holds, and switching traffic instantly would mean losing or silently forking that data.

The stateful version breaks the cutover into explicit stages: provision the new stateful instance with its updated schema or topology; run an idempotent, out-of-band replication process that copies existing data from the old instance to the new one; configure the application layer to *dual-write* every change to both instances simultaneously, so neither one falls behind while replication catches up and cutover is prepared; once the new instance is confirmed current, cut *reads* over to it first, while writes still go to both; finally cut *writes* over exclusively to the new instance, archive a final snapshot of the old one for safety, and only then decommission it.

This is one concrete way of applying [data continuity strategies](data-continuity-strategies.md) — specifically combining segregation (data-holding resources handled distinctly from stateless compute) with replication — to the specific problem of changing the schema or topology of a stateful resource that's actively serving production traffic, without the downtime or data-loss risk of an in-place migration.
