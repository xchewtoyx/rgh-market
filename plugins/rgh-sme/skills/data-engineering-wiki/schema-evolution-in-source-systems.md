---
type: concept
title: Schema Evolution in Source Systems
description: >
  Why source-system schema is expected to change over time, and the two
  models (schemaless vs. fixed) a pipeline has to accommodate.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 2"
---

Source systems handle schema one of two ways. **Schemaless** systems (message
queues, flat files, blob storage, document stores) let the *application*
define schema at write time — this does not mean there is no schema, only that
the storage layer doesn't enforce one. **Fixed-schema** systems (traditional
RDBMS) enforce schema in the database itself; every write must conform.

Schema evolution — new fields, renamed fields, changed types — is expected and
even encouraged under Agile application development. That's precisely what
makes a downstream pipeline's job harder over time: a transformation written
against yesterday's schema can silently break or silently corrupt output
against today's.

A pipeline needs an explicit answer to "how are schema changes communicated
downstream?" before it goes live — whether that's a
[schema registry](schema-registry.md), a [contract](data-contract.md) with
the owning team, or automated drift detection — rather than
discovering the change when a job fails or, worse, when it doesn't fail but
produces wrong output.

**A warehouse or pipeline layer between the source and its consumers absorbs
this cost on their behalf**: when a source application renames a table or
field (a common side effect of an application upgrade), only the ingestion
job that reads that source needs to change — every downstream report and
dashboard built against the warehouse's own schema keeps working unmodified.
Consumers see stale data until the ingestion fix ships, but they see an error
far less often than they would querying the source directly through its new,
incompatible shape. This insulating effect is one of the concrete payoffs of
[warehouse layering](warehouse-layering-source-staging-presentation.md) — the
raw/source layer is exactly the boundary that absorbs a source-side rename
so it never has to propagate past it.
