---
name: catch-up
description: >-
  Loop dispatching parallel focused curation batches across every bundle whose
  backlog has notes already landscape-mapped to it and scored above threshold,
  repeating until nothing qualifies anywhere.
argument-hint:
  "[bundle-slug ...] [--min-confidence T] [--max-parallel N] [--limit N]"
---

# Catch up: drain the landscape-mapped, scored backlog

`/curate --landscape` (see `docs/landscape.md`) and `/curate --focused` (see
`docs/curation.md`, Ratings cache) each do one piece of groundwork — mapping
which bundles a note overlaps, and scoring how well it fits one bundle's charter
— but neither actually curates. Once enough of that groundwork has landed across
many bundles, picking bundles one at a time to run `/curate --focused` against
is manual and easy to leave stale. This skill automates that last step: find
every bundle with fully-vetted, ready-to-curate notes, dispatch curation for as
many as `--max-parallel` at once, and keep going until nothing is left.

catch-up never dispatches `fleeting-researcher` itself (neither landscape nor
charter-scoring mode) and never runs the researcher-dispatch parts of
`/curate --landscape` or `/curate --focused` — it only consumes the caches those
skills already wrote. A bundle with backlog but no ready candidates is expected,
not an error; that backlog needs a landscape sweep or a scoring pass first, run
separately.

## Arguments

- Zero or more `bundle-slug` values — same domains as `/curate`
  (`skills/curate/SKILL.md`, Domains; get them with
  `python3 scripts/domains.py`). No slugs means every domain. Reject unknown
  slugs.
- Optional `--min-confidence T` or `min-confidence=T`, a number in `0–1`
  (default **`0.7`**) — passed straight through to
  `scripts/select-catchup-candidates.py`.
- Optional `--max-parallel N` (default **`4`**) — how many bundles get a curator
  dispatch in a single round.
- Optional `--limit N` (default **`15`**) — how many candidates a single
  bundle's curator is dispatched with in one round, taken from the top of that
  bundle's already confidence-sorted candidate list. Matches `/curate`'s own
  default batch size.

## What "ready" means

A note only becomes a catch-up candidate for a bundle once it is in **all
three** of:

1. **Unreviewed** — not yet in `curation/<bundle>.txt`.
2. **Landscape-mapped to this bundle** — its `landscape/overlap.jsonl` entry
   lists this bundle (see `docs/landscape.md`).
3. **Rated at or above `--min-confidence` for this bundle** —
   `ratings/<bundle>.jsonl` (see `docs/curation.md`, Ratings cache).

This is a hard, three-way intersection — unlike `scripts/filter-by-landscape.py`
(used ahead of _scoring_, deliberately fail-open so an unmapped note still gets
a chance to be scored), a note missing a landscape entry, or scored below
threshold, or scored for a _different_ bundle only, is never a catch-up
candidate. catch-up only ever touches notes both a landscape sweep and a
charter-scoring pass have already vetted for that specific bundle.

`scripts/select-catchup-candidates.py` computes this intersection
deterministically, per bundle, and prints one JSON line per bundle with at least
one candidate — already sorted by priority (highest max candidate confidence
first, then most candidates, then bundle slug for a stable tiebreak). The
supervisor never opens a fleeting note body or judges readiness itself; that
script is the only selection step before dispatch.

## Procedure

1. Parse arguments: bundle slugs (default every domain, reject unknown),
   `--min-confidence` (default `0.7`), `--max-parallel` (default `4`), `--limit`
   (default `15`).
2. **Round loop:**
   1. Run
      `python3 scripts/select-catchup-candidates.py [bundle-slugs...] --min-confidence <T>`
      (repo root). Each output line is one ready bundle, already
      priority-sorted, with its full candidate list.
   2. If the script prints nothing, the backlog is drained — stop the loop and
      go to Finish.
   3. Drop any bundle already marked **stuck** this run (see step 4 below).
   4. Take the top `--max-parallel` bundles from the (already-sorted) remaining
      output.
   5. For each, cap its candidate list to the first `--limit` paths (already
      confidence-sorted descending by the script).
   6. Dispatch that bundle's curator agent in focused mode, **in parallel**
      across this round's batch, using the exact prompt and harness mapping in
      `skills/curate/SKILL.md` (Harness dispatch → curator, Focused
      prompt) with `<CANDIDATE_PATHS>` set to this bundle's capped list (the
      exact paths output by `scripts/select-catchup-candidates.py` for this
      bundle — never substitute, hand-edit, or supply fallback paths) — see
      Harness dispatch below.
   7. Collect each curator's report: candidates offered, notes reviewed, how
      many yielded wiki content.
3. **Stuck-bundle detection (run once per round, after dispatch):** for every
   bundle you dispatched a curator to **last** round, compare its candidate list
   from this round's script output to what it had last round. If a bundle you
   dispatched is still ready with an **identical** candidate list, its curator
   made no ledger progress — mark it **stuck**, exclude it from dispatch for the
   rest of this run, and report it (see Rules). A bundle that was ready but
   **not** dispatched last round (because a higher-priority bundle won the
   `--max-parallel` slot instead) is not stuck — it is simply waiting its turn
   and is reconsidered normally.
4. Repeat from step 2.1.

## Harness dispatch

Reuses the curator dispatch from `/curate --focused` verbatim — see
`skills/curate/SKILL.md` (Harness dispatch → curator, Focused prompt,
and the harness-mapping table beneath it: Claude Code Agent tool, Antigravity
`define_subagent`/`invoke_subagent`, Cursor Task tool). catch-up does not repeat
that prompt or mapping here; use it exactly, once per ready bundle per round,
with this bundle's capped candidate list.

## Finish

Report:

- total rounds run
- per bundle touched, across all rounds: candidates offered, notes reviewed,
  notes that yielded wiki content
- any bundle marked stuck, and why (dispatched but made no ledger progress)
- confirmation the loop stopped because `scripts/select-catchup-candidates.py`
  returned nothing for the remaining (non-stuck) bundles — not because of an
  arbitrary round cap; there isn't one

Suggest `/curate --landscape` and/or `/curate --focused <bundle>` for bundles
whose backlog is large but not yet ready (unreviewed notes that are missing a
landscape entry, or landscape-mapped but not yet scored) — catch-up does not do
that groundwork itself, only the curation step once it exists.

## Rules

- Never read fleeting note bodies or judge readiness in the supervisor —
  `scripts/select-catchup-candidates.py` is the only selection step; the
  dispatched curator is the only one that reads note bodies (in full, per
  `docs/curation.md`'s focused-pass rules).
- Never dispatch more than `--max-parallel` curators in a single round.
- Never dispatch two curators for the same bundle concurrently within a round —
  the script emits at most one entry per bundle, so this holds naturally; do not
  manually split one bundle's candidates across two simultaneous dispatches.
- Stuck-bundle exclusion is per-run, not persisted anywhere: a bundle marked
  stuck in this run is eligible again the next time `/catch-up` is invoked.
- catch-up never dispatches `fleeting-researcher` in either mode and never runs
  `/curate --landscape` or `/curate --focused`'s researcher-dispatch step itself
  — it only consumes `landscape/overlap.jsonl` and `ratings/<bundle>.jsonl`, the
  caches those skills already wrote.
- Do not commit or push unless the user asked for that.
