---
name: score-catchup
description: >-
  Loop dispatching parallel charter-scoring batches across every bundle a
  landscape sweep already tagged but no score exists for yet, repeating until no
  unscored, landscape-tagged notes remain anywhere.
argument-hint: "[bundle-slug ...] [--max-parallel N] [--limit N]"
---

# Score catch-up: drain the landscape-mapped, unscored backlog

The mirror image of `/catch-up`, one stage earlier in the pipeline.
`/curate --landscape` (see `docs/landscape.md`) tells every bundle which notes
it might overlap, but landscape mode never scores — a note can sit
landscape-tagged for a bundle indefinitely until something dispatches a
charter-scoring pass for it. Picking bundles one at a time to run
`/curate --focused` against (which scores its _entire_ unreviewed backlog, not
just the landscape-tagged slice) doesn't target that gap directly. This skill
does: find every bundle with notes a landscape sweep flagged for it that have
never been scored, dispatch charter-scoring for as many as `--max-parallel` at
once, and keep going until nothing is left. The result feeds `/catch-up`
directly — every note this skill scores becomes a `/catch-up` candidate the
moment its score clears that skill's threshold.

score-catchup never dispatches a domain curator and never curates anything — it
only ever appends to `ratings/<bundle>.jsonl`. A bundle with backlog but no
ready candidates is expected, not an error; that backlog needs a landscape sweep
first (`/curate --landscape`), run separately.

## Arguments

- Zero or more `bundle-slug` values — same domains as `/curate`
  (`skills/curate/SKILL.md`, Domains; get them with
  `python3 scripts/domains.py`). No slugs means every domain. Reject unknown
  slugs.
- Optional `--max-parallel N` (default **`4`**) — how many bundles get a
  charter-scoring dispatch in a single round.
- Optional `--limit N` (default **`15`**) — how many candidates a single
  bundle's researcher dispatch is given in one round, taken from the top of that
  bundle's candidate list. Matches `/curate`'s own default batch size.

There is no `--min-confidence` here — that concept belongs to `/catch-up` and to
`/curate --focused`'s selection step, both of which act on scores that already
exist. score-catchup's question is binary: has this (note, bundle) pair been
scored at all, yet?

## What "ready" means

A note only becomes a score-catchup candidate for a bundle once it is in
**both** of:

1. **Unreviewed** — not yet in `curation/<bundle>.txt`. (Curated notes never
   need scoring again — `/catch-up`'s own candidate computation already excludes
   them, so scoring one would be wasted work.)
2. **Landscape-mapped to this bundle** — its `landscape/overlap.jsonl` entry
   lists this bundle (see `docs/landscape.md`).

...**and not already rated for this bundle** — no entry for this
`(path, bundle)` pair in `ratings/<bundle>.jsonl`, at _any_ confidence. A note
scored `0.3` for a bundle still counts as rated; score-catchup does not re-score
it looking for a better number — that's out of scope, not a gap this skill
fills.

`scripts/select-score-catchup-candidates.py` computes this deterministically,
per bundle, and prints one JSON line per bundle with at least one candidate —
sorted by priority (most candidates first, then bundle slug for a stable
tiebreak; there is no confidence signal to rank by before a note has been
scored, unlike `scripts/select-catchup-candidates.py`). The supervisor never
opens a fleeting note body or judges readiness itself; that script is the only
selection step before dispatch.

## Procedure

1. Parse arguments: bundle slugs (default every domain, reject unknown),
   `--max-parallel` (default `4`), `--limit` (default `15`).
2. **Round loop:**
   1. Run `python3 scripts/select-score-catchup-candidates.py [bundle-slugs...]`
      (repo root). Each output line is one ready bundle, already
      priority-sorted, with its full candidate list.
   2. If the script prints nothing, no unscored landscape-tagged notes remain
      anywhere — stop the loop and go to Finish.
   3. Drop any bundle already marked **stuck** this run (see step 3 below).
   4. Take the top `--max-parallel` bundles from the (already-sorted) remaining
      output.
   5. For each, cap its candidate list to the first `--limit` paths.
   6. Dispatch `fleeting-researcher` in **charter-scoring mode**, **in
      parallel** across this round's batch, using the exact prompt and harness
      mapping in `skills/curate/SKILL.md` (Harness dispatch → Researcher
      (focused mode only)) with `<DOMAIN>` set to this bundle and
      `<UNSCORED_PATHS>` set to this bundle's capped list — see Harness dispatch
      below.
   7. Collect each dispatch's report: notes scored vs skipped as already cached.
3. **Stuck-bundle detection (run once per round, after dispatch):** for every
   bundle you dispatched to **last** round, compare its candidate list from this
   round's script output to what it had last round. If a bundle you dispatched
   is still ready with an **identical** candidate list, its dispatch made no
   ratings-cache progress — mark it **stuck**, exclude it from dispatch for the
   rest of this run, and report it (see Rules). A bundle that was ready but
   **not** dispatched last round (because a higher-priority bundle won the
   `--max-parallel` slot instead) is not stuck — it is simply waiting its turn
   and is reconsidered normally.
4. Repeat from step 2.1.

## Harness dispatch

Reuses the charter-scoring researcher dispatch from `/curate --focused` verbatim
— see `skills/curate/SKILL.md` (Harness dispatch → Researcher (focused
mode only), and the harness-mapping table beneath it: Claude Code Agent tool,
Antigravity `define_subagent`/`invoke_subagent`, Cursor Task tool with an
explicit forbid on wiki/ledger/fleeting writes). score-catchup does not repeat
that prompt or mapping here; use it exactly, once per ready bundle per round,
with `<DOMAIN>` set to the bundle and `<UNSCORED_PATHS>` set to this bundle's
capped candidate list.

## Finish

Report:

- total rounds run
- per bundle touched, across all rounds: candidates offered, notes actually
  scored vs skipped as already cached
- any bundle marked stuck, and why (dispatched but made no ratings-cache
  progress)
- confirmation the loop stopped because
  `scripts/select-score-catchup-candidates.py` returned nothing for the
  remaining (non-stuck) bundles — not because of an arbitrary round cap; there
  isn't one

Suggest `/curate --landscape` for bundles whose backlog is large but not yet
landscape-mapped — score-catchup does not do that groundwork itself, only the
scoring step once a landscape entry exists. Suggest `/catch-up` as the natural
next step once scoring lands: every note this run scored above `/catch-up`'s
default threshold is now a curation candidate.

## Rules

- Never read fleeting note bodies or judge readiness in the supervisor —
  `scripts/select-score-catchup-candidates.py` is the only selection step; the
  dispatched researcher is the only one that reads note bodies (in full, per
  `fleeting-researcher.md`'s charter-scoring procedure).
- Never dispatch more than `--max-parallel` researcher dispatches in a single
  round.
- Never dispatch two researcher runs for the same bundle concurrently within a
  round — the script emits at most one entry per bundle, so this holds
  naturally; do not manually split one bundle's candidates across two
  simultaneous dispatches.
- Stuck-bundle exclusion is per-run, not persisted anywhere: a bundle marked
  stuck in this run is eligible again the next time `/score-catchup` is invoked.
- score-catchup never dispatches a domain curator and never runs
  `/curate --landscape`'s or `/catch-up`'s own dispatch steps itself — it only
  reads `landscape/overlap.jsonl` and writes `ratings/<bundle>.jsonl`.
- Do not commit or push unless the user asked for that.
