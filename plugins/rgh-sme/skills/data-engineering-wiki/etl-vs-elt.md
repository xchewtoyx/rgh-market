---
type: concept
title: ETL vs. ELT
description: >
  Whether transformation happens in a dedicated tool before loading (ETL) or
  inside the target platform after loading (ELT), and why the latter has
  become the default with cloud warehouses.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 3"
---

**ETL** (Extract, Transform, Load): Extract pulls from source systems,
Transform cleans/standardizes/applies business logic in a dedicated
processing tool (often producing a fairly modeled, warehouse-ready shape),
and Load pushes the result into the target — historically a
[warehouse](data-warehouse-architecture.md), often into per-department data
marts. Transformation happens *before* the data
lands in the target platform.

**ELT** (Extract, Load, Transform): data moves nearly directly from the
source into a raw staging area *inside* the target platform, and
transformation happens there afterward using the target platform's own
compute. This became the dominant pattern once cloud warehouses got cheap,
elastic compute and could absorb transformation workloads that used to
require a separate ETL tool — see
[compute/storage separation](compute-storage-separation.md). ELT also works
in streaming form: CDC events are staged raw, then transformed in-warehouse.
A related historical variant, "transform-on-read," arose in the Hadoop
ecosystem — store data raw and interpret its schema only at query time (see
[data lake architecture](data-lake-architecture.md)).

The practical trade-off: ETL keeps transformation logic and its compute
outside the target platform (useful when the target has limited or costly
compute, or when transformation needs a tool the target can't run), while ELT
keeps everything in one system and lets the target's engine do the heavy
lifting, at the cost of tying transformation logic to that platform's
compute and dialect. Neither is universally correct — the right choice
follows from where compute is cheap and where the transformation logic needs
to live.

Two further mechanical differences follow from where the transform runs.
**Extraction cost falls on the source in both approaches, but ETL pays it
twice as often**: because the transform tool typically consumes its input
once and doesn't retain a raw copy, a bug discovered in the transform logic
forces a fresh extraction from the source to rerun it — hitting the source
system's performance a second time — whereas ELT's raw landed copy lets a
fixed transform be rerun against already-loaded data with no repeat source
load. **Grain of transformation also differs**: traditional ETL tools often
transform one record at a time, which is slower at volume; ELT transforms in
batches inside the target platform's engine, closer to how that engine
processes everything else it runs.
