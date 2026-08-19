# Agent-context growth review

Periodic **reading** pass for the cross-repo
[`docs/agent-context/`](../docs/agent-context/) OKF bundle. This complements
[`scripts/validate-agent-context.py`](../scripts/validate-agent-context.py),
which catches structural decay (link containment, stale index, orphans,
premature subdirectories) but cannot judge whether the bundle has grown into
overlapping, half-atomic documents nobody links to on purpose.

Promotion criteria live in
[`policy/agent-context-promotion.md`](agent-context-promotion.md); growth review
is the maintenance pass for what is already in the bundle.

## Trigger

Run a growth review when **either** condition is true:

1. **Concept-count threshold** — the flat concept count at the bundle root
   crosses a multiple of six (6, 12, 18, …), matching the subdirectory
   threshold in `validate-agent-context.py`. Count concepts listed in
   `docs/agent-context/index.md`, not review artifacts.
2. **Cadence** — at least 90 days since the last recorded review under
   [`docs/agent-context-reviews/`](../docs/agent-context-reviews/).

Also run once as a **baseline** when the bundle is first adopted on a branch,
even if neither condition has fired yet.

## Required mechanical input

Before reading concepts, capture:

```bash
.venv/bin/okf unlinked-mentions --bundle agent-context
```

Install `okf-core` per [`okf-core.toml`](../okf-core.toml) / `requirements-dev.txt`
when the CLI is not already available in the active `.venv`.

Treat every `suggestions` entry as a candidate missing link. `problems` are
format or graph defects — fix or file before closing the review.

## Review questions

Read concepts (not the whole bundle at once — seed from `index.md` or from
`unlinked-mentions` hits) and answer:

| Question | Look for |
|----------|----------|
| **Split** | One document whose title needs "and", or sections that want different onward links |
| **Merge** | Two concepts that always travel together and never stand alone |
| **Dead-weight links** | Links added for graph symmetry, not because a reader here would want that document next |
| **Subdirectory** | Six or more concepts that belong to one knowledge area and should move under a shared subdirectory |

Structural fixes (split, merge, relink, subdirectory creation) may land in the
same PR as the review record or in a follow-up. **Recording is mandatory**;
edits are optional when the baseline is clean.

## Who runs it

In the [documentation loop](../workflows/documentation.md) step **2b**, dispatch a
fresh `reviewer` in a new subagent or session — same fresh-context rule as
[`docs/agent-context/fresh-context-dispatch.md`](../docs/agent-context/fresh-context-dispatch.md).
The reviewer reads; the implementor applies any agreed structural edits.

## Recording

Write one dated file per run:

`docs/agent-context-reviews/YYYY-MM-DD.md`

Each record includes:

- Date and concept count
- Path or summary of the `unlinked-mentions` output
- Findings table: split / merge / dead-weight link / subdirectory — each row
  names the concept(s) and the action (`none`, `follow-up #N`, or what changed)

Review artifacts live **outside** the OKF bundle root so
`validate-agent-context.py` does not treat them as concepts.
