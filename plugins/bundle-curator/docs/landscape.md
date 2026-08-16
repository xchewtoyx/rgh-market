# Landscape mapping

Cross-bundle scan that tells later, per-domain passes which bundles a fleeting
note might belong to, before they pay the cost of reading it.

Used by `/curate --landscape` and, optionally, by `/curate --focused`'s
researcher-dispatch gather step; also by `/onboard`'s post-onboard pass, which
runs a landscape-mode dispatch immediately after writing a batch of new notes
and then charter-scores whatever bundles it identifies — see Onboard flow below.
Writes only to the shared landscape cache (`landscape/overlap.jsonl`). Never
curates, never ledger-writes, never edits `fleeting/` or a domain bundle, never
writes `ratings/<domain>.jsonl`.

## Why a separate mode from charter scoring

`fleeting-researcher`'s charter-scoring mode (`docs/curation.md`, Ratings cache)
knows one domain's charter and returns a confidence score for that domain alone
— it has no way to know a note also belongs to three other bundles it was never
shown. Landscape mode inverts the knowledge: it is shown every domain's In scope
definition and, for each note, returns every bundle whose scope the note
overlaps. The two modes compose: landscape mode answers "which domains should
even look at this note", charter scoring answers "how well does it fit this one
domain's charter" for whichever domains landscape mode said yes to.

## Landscape cache

Single shared append-only JSONL file at `landscape/overlap.jsonl` — not
per-domain, unlike `ratings/<domain>.jsonl` (see Concurrency below for why that
is safe here). One line per fleeting note the researcher has mapped:

```json
{
  "path": "fleeting/some-source/03-example.md",
  "bundles": ["<domain-slug-a>", "<domain-slug-b>"]
}
```

- `bundles` is `[]`, not a missing entry, when a note does not meaningfully
  overlap any bundle's scope — the note is still "mapped", so it is not
  rescanned on a later landscape pass.
- **Recall bar:** include a bundle when the note has material that domain's
  curator would plausibly want to read in full, even if the note's primary
  subject lies elsewhere — roughly the "tangential or thin; defer" floor
  (confidence ≥ 0.4) from the charter-scoring rubric in
  `fleeting-researcher.md`, not the higher bar a curator or a later
  charter-scoring pass eventually applies. Landscape mode is a broad net;
  narrowing to "worth curating" is charter scoring's job, not this pass's.
- **Boundaries do not remove a bundle from the list.** A domain charter's
  Boundaries section assigns ownership of the full treatment of a topic to a
  neighbour — it does not mean the topic is invisible to your bundle (see
  `docs/curation.md`, "Reading your charter's Boundaries"). Landscape mode
  follows the same rule: a note can, and often does, land in more than one
  bundle's list.

## Concurrency

Charter scoring shards its cache per domain (`ratings/<domain>.jsonl`) because
`/curate --focused` dispatches one researcher per domain and those dispatches
can run concurrently — see `docs/curation.md`'s Concurrency rules. Landscape
mode has no per-domain shard: it is dispatched as a **single** researcher run
over a path set, never run concurrently with another landscape-mode dispatch
over an overlapping set. That single-writer invariant is what makes one shared
file safe — do not parallelize landscape dispatches the way domain curators or
per-domain focused researchers are parallelized.

## Flow (`/curate --landscape` → `/curate --focused` pre-filter)

1. **Gather (supervisor, path-only):**
   `python3 scripts/list-landscape-unmapped.py` prints fleeting paths with no
   `landscape/overlap.jsonl` entry yet — the whole backlog, across every source
   ever onboarded, not scoped to any one run.
2. **Map (`fleeting-researcher`, landscape mode):** reads every domain curator
   charter (`.claude/agents/*-curator.md`), reads each unmapped note in full,
   and appends one `{path, bundles}` line per note immediately after mapping it
   — checkpoint-per-note, the same discipline as charter scoring and the curator
   ledgers.
3. **Consume:** `scripts/filter-by-landscape.py <domain-slug>` narrows a
   domain's already-computed unscored-candidate list (per `docs/curation.md`,
   Ratings cache) to paths whose landscape entry includes that domain —
   **fail-open**: a path with no landscape entry yet still passes through
   unfiltered, so a note the landscape sweep has not reached behaves exactly as
   it would without this filter. This step is optional and additive; it only
   ever narrows the researcher's read list, never widens it beyond what the
   existing gather step already computed.

## Onboard flow (`/onboard` post-onboard pass)

The same two modes, run back-to-back by `/onboard` right after it writes a batch
of new notes, scoped to exactly that batch rather than the whole backlog — see
`skills/onboard/SKILL.md`, Post-onboard: landscape mapping + scoring.

1. **Gather (supervisor, path-only):** the paths this onboard run just wrote —
   already known from the note-writing or chapter-writer step, not re-derived
   from `scripts/list-landscape-unmapped.py` (that would also pull in any older
   unmapped backlog, which belongs to a `/curate --landscape` run instead).
2. **Map:** one landscape-mode `fleeting-researcher` dispatch over exactly those
   paths, same as step 2 above.
3. **Identify:** `scripts/list-bundles-for-paths.py`, fed the same path list on
   stdin, prints the deterministic union of bundles this batch's notes overlap —
   the connector this flow needs that the `/curate --focused` flow above does
   not, since that flow already knows its one target domain.
4. **Score:** for each identified bundle,
   `scripts/filter-by-landscape.py <bundle>` (same path list on stdin) narrows
   to that bundle's subset, then a charter-scoring `fleeting-researcher`
   dispatch over that subset appends to `ratings/<bundle>.jsonl` — the same
   charter-scoring mode `/curate --focused` uses, just triggered from onboard
   instead.

Net effect: after onboarding a source, `/curate --focused` (or a normal
`/curate` pass) for any bundle this batch touched already has ratings-cache
entries for those notes, instead of discovering them cold on its own next gather
step.

## Score-catchup flow (`/score-catchup`)

Landscape mode never scores — a note can sit landscape-tagged for a bundle
indefinitely until something dispatches charter scoring for it, and
`/curate --focused` scores its _entire_ unreviewed backlog rather than
specifically the landscape-tagged slice. `/score-catchup`
(`skills/score-catchup/SKILL.md`) targets that gap directly:
`scripts/select-score-catchup-candidates.py`, per bundle, keeps notes that are
unreviewed **and** landscape-mapped to that bundle **and not already rated for
it at any confidence** — the same round-loop shape as `/catch-up` below
(dispatch up to `--max-parallel` at once, repeat until empty), but dispatching
`fleeting-researcher` in charter-scoring mode instead of a domain curator, since
there is no score yet to curate against.

## Catch-up flow (`/catch-up`)

Both flows above are groundwork — they only ever populate
`landscape/overlap.jsonl` and `ratings/<domain>.jsonl`, never curate.
`/catch-up` (`skills/catch-up/SKILL.md`) is the consumer that closes the
loop: `scripts/select-catchup-candidates.py` reads both caches together and, per
bundle, keeps only notes that are unreviewed **and** landscape-mapped to that
bundle **and** rated at or above a confidence threshold — a hard, three-way
intersection, unlike `filter-by-landscape.py`'s fail-open pre-filter above.
Bundles with any qualifying note are dispatched a focused curation batch (up to
`--max-parallel` at once), looping until nothing qualifies anywhere. See
`skills/catch-up/SKILL.md` for the full round-loop procedure.

Run in order — `/curate --landscape` maps, `/score-catchup` scores what mapping
found, `/catch-up` curates what scoring cleared — and each stage is
independently safe to run repeatedly: none of them widen what a later stage sees
beyond what its own cache already recorded.

## Non-goals

- Landscape mode never scores or ranks — membership in a bundle's list is the
  only signal; confidence-style thresholds stay charter scoring's job.
- Landscape mode never selects curation candidates, writes ledgers, or writes
  wiki notes.
- Not a replacement for charter scoring or a curator's own full read — a note in
  a bundle's landscape list still needs a scoring pass (or direct curator
  judgment in normal mode) before it is ever curated.
