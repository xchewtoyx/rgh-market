---
type: concept
title: Recovering Deleted Records via Forward-Leading Insertion
description: >
  Detecting a physically deleted source row in a delta-loaded fact table by
  inserting a zeroed logical-deletion record on the next load, instead of
  scanning backward to find what's missing.
sources:
  - title: Data Modeling with Snowflake
    resource: "Data Modeling with Snowflake (Gershkovich), ch. 14"
---

A [full dimension load](insert-only-history-pattern.md) can detect deletion
easily — compare today's set of primary keys against a prior load, and any
key that's disappeared was deleted. A fact table usually can't take this
approach: it's too voluminous for a full reload and is normally loaded as a
[delta](incremental-vs-full-extraction.md) of changes since the last run.
When a source physically deletes a row rather than recording a proper
cancellation, that row simply never appears in a delta extract again — there
is no direct signal that it's gone, and the warehouse silently drifts out of
sync with the source. Detecting this by looking backward (aggregating and
comparing historical load batches with window functions) is expensive
exactly where it matters most: on the largest, highest-volume tables.

**Forward-leading insertion turns the problem around.** Instead of scanning
history to notice an absence, the pipeline inserts an explicit **logical
deletion record** into the *next* load batch for the affected key — zeroing
out its additive measures and flagging it as a deletion. The deletion then
flows through the warehouse as a completely ordinary forward-moving load
event (through [reverse-balance loading](reverse-balance-fact-loading.md) or
whatever load mechanism the fact table already uses), rather than requiring
a special backward-reconciliation pass. The deletion flag also does double
duty: it prevents the same logical deletion from being re-inserted on every
subsequent load, and it gives a concrete, auditable answer if anyone asks
why the warehouse shows a row the source system no longer has.

The identification step itself only needs to look one hop ahead, not
backward through full history: for each parent grouping (an order, say),
find its next load date, then flag any child record (a line item) that has
no corresponding next-load appearance even though its parent kept being
loaded — narrowing the expensive lookahead computation to the much smaller
parent grain before applying it at the finer child grain keeps the detection
step itself cheap. This generalizes beyond any one fact-table design: the
logical-deletion insert has to happen in the landing/staging area regardless
of which downstream load pattern consumes it from there.
