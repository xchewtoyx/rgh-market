---
type: concept
title: OLAP Cube
description: A multi-dimensional grid of pre-computed aggregations used for rapid query execution.
sources:
  - title: "Designing Data-Intensive Applications"
    resource: "Designing Data-Intensive Applications (Martin Kleppmann), ch. 3"
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 3"
---

An OLAP cube (or data cube) is a multi-dimensional array of pre-computed aggregations designed to accelerate query execution in [OLTP vs. OLAP](oltp-vs-olap.md) workloads. It is implemented on a **multidimensional database (MDB)** — the alternative to a relational [star-schema](star-schema.md) for physically implementing a dimensional model, storing precomputed combinations of dimension and fact values so users can study them interactively.

A cube is constructed by grouping and summarizing raw facts across different dimension axes. For example, a three-dimensional cube might aggregate sales by:
$$\text{date} \times \text{product} \times \text{store}$$

### Trade-offs
*   **Query Speed and interactivity:** By pre-aggregating values (such as `SUM` or `COUNT` of sales) along the dimension coordinates, queries requesting point-aggregates return almost instantly without scanning raw event rows. This gives instantaneous feedback as users slice, dice, and drill through the data interactively, unlike a star schema's query-and-response interaction pattern, which issues a fresh SQL query for every change in view.
*   **Expressiveness:** Cubes aren't limited by SQL's expressive gaps — they natively support running totals, rankings, and statistical operations SQL historically lacked, and may offer built-in support for ragged recursive hierarchies (which require a [bridge table](bridge-table.md) in the relational world).
*   **Flexibility:** OLAP cubes lack the granular flexibility of a raw [star-schema](star-schema.md). If an analyst needs to query details not pre-calculated in the cube (e.g., filtering by a specific transaction attribute or custom timestamp), they must fall back to querying the raw [fact-table](fact-table.md) and [dimension-table](dimension-table.md)s.
*   **Scalability:** Storage requirements explode combinatorially as the number of dimensions and their cardinalities grow, limiting a cube's ability to scale to large data volumes; measures taken to control this (fewer attributes, coarser [grain](grain.md)) reduce the cube's benefits in turn.
*   **Access:** Cubes are accessed through often-proprietary interfaces — MDX has gained standard-like acceptance, but the pool of MDX-literate practitioners and MDX-compatible tools is smaller than SQL's.

### Implementation variations

Some MDB products are full DBMS engines managing a cube natively; others embed the cube inside a specific front-end OLAP application; a third style, **ROLAP** (relational OLAP), assembles cube-like slicing and dicing dynamically from queries issued against an ordinary relational database rather than a native multidimensional store. The line between relational and multidimensional technology is fading — many RDBMS products add multidimensional storage as a performance layer, and some tools auto-generate cubes from relational tables or rewrite SQL queries as MDX (or vice versa).

### Cube as primary storage versus a supplementary layer

A cube can replace relational storage outright as the *primary* store for a subject area's dimensional data (common in smaller, tightly-scoped domains like packaged budgeting analytics), or it can *supplement* a star schema, built as a derived, secondary store loaded from the relational data. As primary storage, the cube's scalability limits are a real concern — especially when it is loaded straight from operational data with no separate atomic repository behind it, since any aggregation performed in the cube is analytic detail permanently lost. Used as a supplement instead, the star retains comprehensive, granular data while the cube adds fast interactive query capability on top, serving the same purpose as [aggregate fact table](aggregate-fact-table.md)s — this pairing, star for scale plus one or more cubes for speed, is described as the foundation of many successful implementations, and many multidimensional products are built specifically to generate cubes from an underlying star.

A cube built to summarize *another* cube, by contrast, usually delivers little benefit — a cube is already a high-performance structure with facts precomputed across its dimension members, so re-aggregating an already-aggregated cube rarely pays for itself. The exception is a product that lets an administrator dial down a cube's own degree of pre-summarization to improve storage scalability (cubes traditionally scale worse than stars, growing combinatorially with more dimensions) at a performance cost — in that configuration, pairing a storage-tuned base cube with a separate, more heavily pre-summarized aggregate cube can make sense, mirroring the same base/aggregate relationship a relational [aggregate fact table](aggregate-fact-table.md) has with its own base star.
