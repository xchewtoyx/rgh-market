---
type: concept
title: Data Catalog
description: >
  A centralized metadata store spanning operational and analytical sources
  that makes datasets findable and their relationships and lineage visible.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 6"
---

A data catalog is a centralized metadata store across an organization —
not a storage layer itself, but something that integrates with every
storage system a pipeline touches. It typically spans both operational and
analytical sources, incorporates [lineage](data-lineage.md) and
dataset-relationship views, and allows human-editable descriptions on top of
whatever it captures automatically.

In practice a catalog is populated two ways: applications ideally push
metadata directly to the catalog's API as they write data, but most
catalogs actually rely on automated scanning layers that pull metadata out
of lakes, warehouses, and operational databases after the fact — sometimes
inferring relationships or flagging sensitive fields along the way. A
human-facing "data portal" layer often sits on top, letting analysts,
scientists, and engineers search and browse relationships, sometimes with
wiki-style annotation.

A catalog is the concrete answer to the discoverability problem that
[pipeline metadata categories](pipeline-metadata-categories.md) describes in
the abstract — a lakehouse table's actual discoverability, for instance,
depends directly on whether its metadata made it into the catalog at all.
