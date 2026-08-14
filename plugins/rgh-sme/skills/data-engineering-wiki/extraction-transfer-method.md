---
type: concept
title: Extraction Transfer Method (File-Based vs. Streaming)
description: >
  Whether an extract step writes to an intermediate file before loading or
  pipes data directly into the target, and the restartability trade-off
  between them.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 19"
---

Independent of whether a pipeline is [batch or streaming](batch-vs-streaming-ingestion.md)
at the ingestion-cadence level, a single extract step can move data out of a
source system one of two ways:

- **File-based**: extract to a file, transfer the file to the pipeline
  environment, then transform and load it. Easier to restart from a known
  point after a failure, easier to compress and encrypt in transit, and
  easier to verify (a row count on the file catches truncation or corruption
  before it reaches the target).
- **Streaming transfer**: data flows from source through the transform step
  directly into staging as one continuous process, with no intermediate file.
  Operationally more appealing — no extra storage, no extra hop — but harder
  to restart cleanly, since there's no durable intermediate artifact to
  resume from if the process dies partway through.

When transferring extract files over a network, **compress before encrypting,
not after** — an encrypted file is high-entropy and doesn't compress
meaningfully, so compressing first can cut transfer time substantially over a
constrained or public link, while encrypting is worth doing whenever the
transfer crosses a public network (and often even on an internal one).

This is a narrower, transfer-level decision than
[batch vs. streaming ingestion](batch-vs-streaming-ingestion.md): a batch
pipeline can use either transfer method for a given extract, and the choice
should be driven by how much restart and verification safety the specific
source's reliability and size demand.
