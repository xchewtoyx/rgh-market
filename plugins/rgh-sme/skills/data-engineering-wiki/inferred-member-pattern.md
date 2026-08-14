---
type: concept
title: Inferred Member Pattern for Early-Arriving Facts
description: >
  Assigning a placeholder dimension row with dummy attributes when a fact
  arrives before its dimensional context is known, instead of pointing the
  fact at a shared default row or making the fact wait.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 19"
---

The ideal load order is a fact's full dimensional context arriving before or
with the fact itself, but that's not always available: a transaction can
reference a customer, product, or other entity the pipeline hasn't seen a
dimension record for yet. In a batch pipeline this is often solvable by
simply waiting for the next cycle; in a low-latency pipeline the fact must be
made visible before its dimensional context is fully known — see
[late-arriving data](late-arriving-data.md) for the broader policy question
this forces.

Two ways to handle an unrecognized-but-plausible natural key at fact-load
time:

- **Point at a shared default/"unknown" row.** Simple, but every fact routed
  there still needs a destructive update later, once the entity is actually
  known, to repoint it at the correct dimension row. A more traceable variant
  of this same approach handles a genuinely **invalid** reference (not
  merely "not yet loaded," but a value that will never resolve to a real
  dimension row, e.g. a `product_code` that doesn't exist because of a
  data-entry error): point at a shared row explicitly flagged
  `row_type = "Invalid"` rather than a generic "unknown" row, and carry the
  fact's own transaction identifier on the fact row itself so the specific
  offending row can be found again once someone investigates. An optional
  exception table recording the failed value alongside that transaction
  identifier isn't strictly required, but it's what lets the eventual
  correction be automated instead of hand-searched for.
- **The inferred member pattern**, for a reference that's merely not-yet-seen
  rather than invalid: assign a brand-new surrogate key
  immediately, with dummy/placeholder attribute values, and insert it as a
  genuine new dimension row rather than reusing a shared default. When the
  entity's real attributes eventually arrive, apply them as a
  [Type 1 overwrite](scd-overwrite-load-mechanics.md) onto that same row.
  Because the fact already points at this row's stable surrogate key, filling
  in real attributes later needs no destructive change to any fact table —
  only the dimension row itself is touched.

The inferred member pattern is generally preferable specifically because it
avoids fact-table rewrites entirely; the trade-off is that the dimension
carries a brief window where a row's attributes are known to be provisional.
A useful convention for that window and for any other ETL-assigned default
value: label it distinctively and traceably — e.g. `"Not Yet Assigned
<surrogate key>"` rather than a bare `NULL` or generic `"Unknown"` — so
provisional rows don't get silently lumped together in reports and remain
individually identifiable for later correction.

A third option shows up specifically under tight [latency
constraints](latency-tier-triage.md): rather than creating a placeholder row
at all, post the fact against whatever dimension version is already
available — even if it's known to be stale — because there's no time budget
left to resolve or create a dimension row before the fact must become
visible. This trades a brief, explicit window of dimensional inaccuracy for
never blocking fact visibility on dimension resolution; whether a revised
dimension then gets applied immediately or held for the next batch pass is a
separate policy choice layered on top.

This same repoint-vs-inferred-row choice reappears for a **late-arriving
Type 2 update**: when a correction to a dimension's history arrives after
facts have already loaded against the pre-correction row, the fix is to add
the revised row with its own new surrogate key, then scan forward and
destructively repoint every affected fact row's foreign key and reset
effective dates — unlike the inferred-member case, this one is unavoidably
destructive, because the facts were already loaded against a version of
history that has since changed underneath them. The concrete selection rule
for which fact rows need repointing: find every fact row for that natural
key whose own transaction date falls **after** the newly-inserted version's
effective date — those are exactly the facts that should have been keyed to
the new version had it existed at load time, and are now pointing at a
version that's been superseded underneath them.
