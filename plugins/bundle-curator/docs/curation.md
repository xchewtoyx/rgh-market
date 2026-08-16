# Curation procedure

How a curation pass runs for one domain. Every curator agent follows this
procedure; the domain-specific charter lives in the curator's agent definition
under `.claude/agents/` (canonical for Claude Code, Antigravity, Cursor, and any
other harness).

## Before you start

1. Read `docs/wiki-rules.md` in full — it defines how notes are written, named,
   linked, and scoped. Do not write or edit any bundle note before reading it.
2. Read your ledger file at `curation/<domain-slug>.txt`. Lines starting with
   `#` are comments; every other line is the path of a fleeting note this domain
   has already reviewed.

## Reading your charter's Boundaries

Your charter's Boundaries section assigns **ownership of the full treatment** of
a topic to a neighbouring bundle. It does **not** forbid the topic from
appearing in your bundle. Bundles are the retrieval unit and links never cross
them, so any concept your bundle's users need that exists only in a neighbouring
bundle is invisible to them — a boundary read as "never write about X here"
punches a hole progressive disclosure cannot route around.

Apply boundaries as a depth-and-perspective rule:

- **Cover** neighbouring material to the depth an agent working in _your_ domain
  needs, written from your domain's angle, linking it into your own graph. The
  owning bundle carries the full treatment; you carry the working subset.
- **Do not shallow-mirror** another domain's corpus. If a concept adds nothing
  beyond what the owning bundle would say and your users would never need it
  mid-task, leave it out — that is the scope-creep the boundary exists to
  prevent.
- The same concept may legitimately exist in several bundles, each at its own
  depth and angle. Converge on one canonical note per concept _within_ your
  bundle (per `docs/wiki-rules.md`); across bundles, duplication is expected and
  fine. Cite `sources:` faithfully so parallel treatments can be reconciled
  against the same text if they drift.

## Selecting input & Batching

3. List all Markdown files under `fleeting/` (any depth). The set to review is
   every fleeting note whose path does not appear in your ledger.
4. **Honour the batch limit from the supervisor**: Your dispatch prompt includes
   a limit `N` (default 15) or `all`. Review at most `N` unreviewed notes in
   this pass, then stop and report — do not silently continue into another
   batch. If the limit is `all`, keep going until the backlog is empty, still
   checkpointing after each note. The default one-batch stop keeps runs
   reviewable and supports smoke-testing curator instructions; the user (or a
   later `/curate`) covers the rest.
5. **Read each unreviewed note in full**: You must open and read the full text
   of every single note using your file viewing tools before making a relevance
   decision and updating the ledger. **Never make shortcut decisions based
   solely on directory names, file prefixes, or other heuristics, and never
   bulk-append files to the ledger without reading them first.** Decide whether
   it contains material inside your domain charter. Many notes will be relevant
   to several domains, and some will have nothing for yours — both are normal.

## Curating

6. For notes with relevant material, follow the Process section of
   `docs/wiki-rules.md`: decompose into atomic concepts, search your bundle for
   existing coverage, extend or create notes one concept at a time, linking as
   you go. Carry the fleeting note's source citation into each wiki note's
   `sources:` frontmatter.

   **Before writing any new note file, search first — this step is mandatory,
   not a suggestion.** Run
   `.venv/bin/okf search --bundle <domain-slug> "<concept>"` and/or
   `.venv/bin/okf list-concepts --bundle <domain-slug>` for the concept you're
   about to write, using the concept's likely title, synonyms, and any
   distinctive terms from the fleeting note. Only create a new file once you've
   confirmed no existing note already covers the concept under a different slug;
   if one exists, extend it in place per the one-canonical-note rule instead. A
   grep for an exact slug guess is not sufficient — near-duplicate notes get
   different slugs precisely because two curation passes chose different words
   for the same concept, especially when a normal pass and a later `--focused`
   pass both touch the same source's chapters without one checking the other's
   coverage first. Searching before writing is what catches that at curation
   time, before duplicate note pairs under divergent slugs have a chance to
   accumulate.

7. Write only inside your own domain folder. Never edit another domain's bundle,
   and never edit the fleeting notes themselves — they are shared raw input for
   all curators.
8. **Checkpoint the ledger immediately, one note at a time — this is mandatory,
   not optional.** As soon as you finish a note (decided it had nothing
   relevant, or finished writing/extending wiki notes from it), append its path
   to `curation/<domain-slug>.txt` right then, before moving to the next note.
   One path per line, relative to the repo root, e.g.
   `fleeting/the-scout-mindset/03-motivated-vs-accurate-reasoning.md`. The
   ledger records "reviewed", not "used" — append it whether or not the note
   yielded any wiki content.

   Never batch ledger writes until the end of a run. Curation is
   token-expensive; a run that dies partway through (interruption, error,
   context limit) must not lose credit for notes already reviewed. Do not read
   ahead through multiple notes before writing any ledger entries, even if the
   notes feel cross-cutting or easier to reason about together — checkpoint
   after each one regardless.

## Finishing

9. If the `okf` CLI is available (installed into the repo-local `.venv/` by
   `scripts/setup.sh`; use `.venv/bin/okf` unless `okf` is on your PATH),
   validate your work from the repo root:

   ```sh
   .venv/bin/okf validate --bundle <domain-slug>
   .venv/bin/okf graph --bundle <domain-slug> --broken
   ```

   Fix any error-severity findings and any broken links you introduced. If `okf`
   is not installed, check your frontmatter and links manually.

10. Report back: how many fleeting notes you reviewed, whether the batch limit
    stopped the run, roughly how many unreviewed notes remain for your domain,
    how many wiki notes you created or extended, and anything you deliberately
    left for another domain's curator.

## Resuming after an interruption

If you are picked back up mid-pass (context limit, API error, or any other stop)
with a message telling you to continue: you _are_ the curator agent for this
domain, mid-run. Do not spawn or delegate to another curator instance — there
isn't one. Re-read your ledger to see how far you got, then resume directly at
step 5 with the next unreviewed note (or the next selected path, if this was a
focused pass).

## Focused / bootstrap passes

When the supervisor dispatches you with an explicit candidate path list (from
`/curate --focused`, after `fleeting-researcher` scored notes against your
charter and persisted the scores to the ratings cache):

1. Curate **only** the listed paths, in the order given. Do not pull other
   unreviewed notes from `fleeting/` during this pass.
2. Still follow steps 1–2 and 5–10 above: read `docs/wiki-rules.md`, read each
   selected note **in full**, atomize or skip with judgment, and **checkpoint
   the ledger after each selected note** (including reviewed-not-used).
3. Notes not on the list — including researcher near-misses and anything below
   the confidence threshold — remain **unreviewed**. Do not append them to the
   ledger. A later normal or focused pass may still pick them up.
4. Report that this was a focused pass: how many listed notes you reviewed, how
   many yielded wiki content, and that non-listed notes were left untouched in
   the ledger.

The researcher never writes your ledger. Only you do, and only after a full read
of a note you were asked to curate.

## Ratings cache (`/curate --focused`)

Focused/bootstrap passes persist researcher confidence scores so repeated runs
don't re-read and re-score notes already assessed against the same charter. This
section is the full picture; `agents/fleeting-researcher.md` and
`skills/curate/SKILL.md` implement the pieces below.

### File layout

One JSONL file per domain: `ratings/<domain-slug>.jsonl`, one JSON object per
line, no in-place rewrites (append-only, mirroring the
`curation/<domain-slug>.txt` ledgers' checkpoint-per-note discipline). Each
line:

```json
{
  "path": "fleeting/.../03-example.md",
  "bundle": "<domain-slug>",
  "confidence": 0.82
}
```

**Why per-bundle files, not one flat `ratings.jsonl`:** the same
collision-free-concurrent-dispatch argument this repo already applies to the
per-domain curator ledgers (see Concurrency rules below and
`curation/<domain-slug>.txt`). `/curate --focused` dispatches one researcher per
domain, and `/curate` (normal mode) already runs multiple domain curators in
parallel today. A single flat journal would put every concurrently running
researcher's appends into the same file; per-bundle files mean each writer (one
researcher per domain per focused invocation) owns only its own file — no lock,
no interleaving risk, the same posture as the ledgers.

**Header:** none. JSONL has no `#`-comment convention the way the
`curation/<domain-slug>.txt` ledgers do (a leading `#` line would fail
`json.loads` on every reader), so the format is documented here and in
`fleeting-researcher.md` instead of inline in the file. A new or lagging domain
does not need an empty placeholder file first — `ratings/<domain>.jsonl` is
created on first write; both the cache-first gather step and
`scripts/select-focused-candidates.py` treat a missing file as "nothing cached
yet" (empty result, not an error).

### Charter-drift handling (decided)

**Decision: accepted staleness, no invalidation.** A cached confidence score
reflects the domain charter at scoring time. If `/charter-review` later edits
that charter (`docs/charter-review.md`), existing cache entries for that domain
are **not** automatically invalidated, re-flagged, or purged.

Rationale:

- The repo has no existing mechanism that retroactively re-validates
  already-_curated_ wiki notes against a charter edit either —
  `docs/charter-review.md`'s own re-curation guidance is a human-directed,
  sampled "ledger reopen candidates" review, not an automatic sweep. Adding
  automatic invalidation for the ratings cache (a lower-stakes signal than
  committed wiki content) would be new machinery inconsistent with how the rest
  of the repo already treats charter drift.
- The blast radius of a stale score is small and self-correcting: a stale cached
  score can at most defer a note that would now score differently (a fresh
  researcher pass over that path is cheap and catches it) or surface a note
  slightly off the current charter — but the domain curator still fully reads
  every selected note and can reject it on the curator's own charter-grounded
  judgment. The cache never bypasses the curator's full read; it only avoids
  repeating the researcher's read.
- `docs/charter-review.md` already treats charter drift as something later
  passes absorb gradually (light drift sampling, human-directed reopen
  candidates) rather than something that forces a synchronous rewrite of derived
  state.
- Building invalidation would require tracking which charter version scored each
  cache entry and diffing charters on every `/charter-review` run —
  disproportionate machinery for a lower-stakes derived cache.

If a stale score turns out to matter in practice (a charter edit meaningfully
redraws a domain's boundaries), the fix is a fresh focused pass after manually
deleting or editing the affected domain's `ratings/<domain-slug>.jsonl` — an
explicit human/agent action, not automatic invalidation.

### Cache-first flow, end to end

1. **Gather (supervisor, path-only):** unreviewed paths (fleeting paths not in
   `curation/<domain-slug>.txt`) minus already-cached paths (paths present in
   `ratings/<domain-slug>.jsonl` for that domain) = the unscored set. Only the
   unscored set is dispatched to the researcher — on a repeated focused pass
   over an already-warm cache, this is the only new work.
2. **Score (fleeting-researcher):** for each unscored path, the researcher
   defensively re-checks the cache before opening it (skip — do not re-open or
   re-score — any pair already cached, even if it slipped through the
   supervisor's gather step), opens and scores the rest against the domain
   charter, and appends one line to `ratings/<domain-slug>.jsonl` immediately
   after scoring each note — checkpoint-per-note, the same discipline as the
   curator ledgers. Cache writes are never batched to the end of a run.
3. **Select
   (`python3 scripts/select-focused-candidates.py <domain> --min-confidence T`,
   deterministic):** reads all cached ratings for the domain (this run's new
   entries plus everything already cached), filters out paths already in
   `curation/<domain-slug>.txt`, sorts the remainder descending by confidence,
   and walks from the top, stopping at the first entry below `T`. Because the
   list is sorted, one sub-threshold hit is sufficient to stop — no need to scan
   the rest. Prints the surviving paths, highest confidence first. The
   supervisor takes at most the batch limit `N` from the top of that output;
   this is deterministic tooling, not researcher/supervisor reasoning.
4. **Curate (domain curator, unchanged):** the curator reads each selected path
   in full and checkpoints `curation/<domain-slug>.txt` one note at a time,
   exactly as in a normal pass.

### Landscape pre-filter (optional)

Step 1's unscored set (unreviewed minus already-cached) can optionally be
narrowed further before it reaches the researcher, using a separate cache:
`landscape/overlap.jsonl`, written by `fleeting-researcher`'s **landscape mode**
— a different dispatch from the charter-scoring mode this section describes,
shown every domain's charter at once instead of just one. See
`docs/landscape.md` for the full mode and cache spec.

Pipe the unscored set through
`python3 scripts/filter-by-landscape.py <domain-slug>` before dispatching the
researcher. The filter is **fail-open**: any path without a landscape entry yet
passes through unchanged, so running it never hides a note this domain would
otherwise have seen — it only skips notes a landscape pass has already
determined do not overlap this domain's scope, saving the researcher a full read
it would likely have scored low anyway. Skipping this step entirely (no
landscape data yet, or choosing not to run `/curate --landscape` first) leaves
charter scoring exactly as it behaves without this section.

Landscape data, and often a domain's ratings-cache entries themselves, may
already exist by the time a `/curate --focused` gather step runs at all:
`/onboard`'s post-onboard pass runs both modes automatically right after writing
a batch of new notes, scored against whatever bundles its own landscape sweep
identified for that batch (see `docs/landscape.md`, Onboard flow). This
section's pre-filter step still applies unchanged on top of that — it is the
same fail-open filter either way, regardless of whether the landscape cache it
reads was populated by `/curate --landscape` or by `/onboard`.

Landscape data can also outrun scoring: a note can be landscape-mapped to a
bundle with no ratings-cache entry for it yet. `/score-catchup`
(`skills/score-catchup/SKILL.md`) targets exactly that: per bundle,
notes that are unreviewed **and** landscape-mapped **and not yet rated at any
confidence**, computed by `scripts/select-score-catchup-candidates.py` and
dispatched to `fleeting-researcher`'s charter-scoring mode the same way this
section's Researcher dispatch works — just driven automatically across every
bundle with a gap, instead of one `--focused` invocation at a time. See
`docs/landscape.md`, Score-catchup flow.

Once both caches have accumulated entries across many bundles, `/catch-up`
(`skills/catch-up/SKILL.md`) is the automation that drains what they
together already vetted — a **hard** (not fail-open) intersection of unreviewed
∩ landscape-tagged ∩ rated-above-threshold, computed per bundle by
`scripts/select-catchup-candidates.py`, driving parallel focused curation
batches across every bundle at once instead of one `/curate --focused`
invocation at a time. See `docs/landscape.md`, Catch-up flow.

**Ledger-write timing is unchanged by this cache:** a cached low-confidence or
deferred score never causes a `curation/<domain-slug>.txt` write — only the
curator writes the ledger, and only after a full read of a note it was actually
dispatched to curate. Scoring (cache write) and curating (ledger write) remain
separate events, exactly as they were before this cache existed — the cache
changes _when the researcher needs to read a note again_, not who writes the
ledger or when.

## Concurrency rules

Multiple domain curators may run in parallel. The layout makes this safe as long
as each curator:

- writes only inside its own domain folder,
- appends only to its own `curation/<domain-slug>.txt` ledger,
- treats `fleeting/` as read-only.

The same argument extends to focused-mode researchers: multiple domains'
`--focused` passes may run concurrently (mirroring normal-mode's parallel
curator dispatch), and each `fleeting-researcher` invocation appends only to its
own domain's `ratings/<domain-slug>.jsonl` — never a shared flat journal — so
concurrent researchers cannot collide on the same file. See Ratings cache above
for why this shaped the file-layout decision.
