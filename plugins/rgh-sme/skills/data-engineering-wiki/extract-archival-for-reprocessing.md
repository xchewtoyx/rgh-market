---
type: concept
title: Archiving Staged Extracts for Reprocessing
description: >
  Keeping raw extracted data on disk after each major pipeline stage by
  default, because re-extracting it from the source later may no longer be
  possible.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 19"
---

Staging data to disk after each major pipeline stage — extracted, cleaned and
conformed, delivered — is cheap relative to the risk it avoids. The default
should be to archive all staged data indefinitely, unless a conscious
decision has been made that a particular data set will never need to be
recovered.

The reason this defaults to "keep it" rather than "delete it": the source
system that produced an extract may not be able to reproduce it later. Source
data gets purged, overwritten, or reshaped by the time a bug is discovered
weeks or months after the fact, so an extract that looked safe to discard at
the time can turn out to be the only copy of data that a
[backfill](idempotent-and-replayable-jobs.md) would need to reprocess
correctly. Every archived data set needs accompanying
[lineage](data-lineage.md) metadata, so a later reprocessing effort can find
the right archived extract instead of only knowing that "some archive
somewhere" has it.

This is the input-side complement to
[idempotent and replayable jobs](idempotent-and-replayable-jobs.md): a job
being safe to re-run is only useful if the exact input it originally ran
against is still available to re-run it against.
