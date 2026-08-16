---
name: curate
description: Dispatch domain curators over unreviewed fleeting notes.
argument-hint:
  "[domain-slug ...] [--limit N|all] [--focused] [--min-confidence T]
  [--landscape]"
---

# Curate fleeting notes into the domain wikis

Dispatch the per-domain curator agents to review unprocessed fleeting notes and
update their wiki bundles.

## Domains

This plugin is domain-agnostic: the set of bundles is whatever the consuming
repo declares in `okf-core.toml`. Get the current slugs with
`python3 scripts/domains.py` (one per line, declaration order) — never
hardcode or assume a domain list. The curator-agent name for a slug is always
mechanical: `<slug>-curator`.

Charters live at `.claude/agents/<slug>-curator.md` (canonical for every
harness) — one file per domain, authored in the consuming repo, not shipped by
this plugin. The procedure each curator follows is `docs/curation.md` — do not
restate or shorten it here.

Focused/bootstrap research and the landscape sweep share one agent,
`agents/fleeting-researcher.md`, run in one of two independent modes per
dispatch — never writes ledgers, fleeting notes, or wiki bundles in either:

- **Charter scoring** (focused mode) — one domain charter, writes
  `ratings/<domain>.jsonl`; selected deterministically by
  `scripts/select-focused-candidates.py`. See `docs/curation.md` (Ratings cache)
  for the full flow.
- **Landscape mapping** (`--landscape`) — every domain charter at once, writes
  the shared `landscape/overlap.jsonl`; consumed by
  `scripts/filter-by-landscape.py` as an optional pre-filter for charter
  scoring's gather step. See `docs/landscape.md` for the full flow.

## Arguments

- Zero or more `domain-slug` values. No slugs means every domain from
  `python3 scripts/domains.py` **in normal mode only**. Reject unknown slugs.
- Optional batch limit (first-class; pick exactly one form):
  - `--limit N` or `limit=N` where `N` is a positive integer
  - `--limit all` or `limit=all` to keep going until that domain's backlog is
    exhausted (still checkpointing per note). **Not allowed with `--focused`** —
    focused mode always uses a numeric limit.
- Optional focused/bootstrap mode:
  - `--focused` or `focused` — requires **exactly one** domain slug
  - Optional `--min-confidence T` or `min-confidence=T` where `T` is a number in
    `0–1` (default **`0.7`**)
- Optional landscape mode:
  - `--landscape` or `landscape` — takes **no** domain slug (it covers every
    bundle in one pass, not one domain). **Not allowed with `--focused`** or
    with any domain slug.
  - Uses the same `--limit N|all` form as normal mode (default **`40`** — see
    Landscape mode below for why the default differs from normal mode's `15`).

**Default limit: `--limit 15`** — one batch, then stop. This conserves token
budget, keeps review tractable, and supports instruction smoke tests. Do not
silently continue past the limit. Remaining backlog is left for a later
`/curate` (or raise `--limit` / use `--limit all` in normal mode).

## Modes

### Normal mode (default)

Path-vs-ledger pre-check, then dispatch each domain's curator over unreviewed
notes up to the limit. Curators choose relevance themselves while reading every
note in full.

### Focused / bootstrap mode (`--focused`)

Use when bootstrapping a new or lagging domain: reach a usable bundle from
high-confidence notes without a full backlog pass. Researcher confidence scores
persist in a per-domain ratings cache (`ratings/<domain>.jsonl`), so repeated
focused passes only pay the read+reasoning cost for notes that have not been
scored yet — see `docs/curation.md` (Ratings cache) for the full flow.

1. Require exactly one domain slug and a numeric `--limit` (default 15).
2. Path-vs-ledger pre-check only (supervisor still must not read note bodies).
3. Cache-first candidate gathering: unreviewed paths (per
   `curation/<domain>.txt`) minus paths already cached for this domain (per
   `ratings/<domain>.jsonl`) = the unscored set. Only that reduced set goes to
   the researcher.
4. Dispatch the **fleeting-researcher** (writes only the ratings cache; still
   never writes ledgers, fleeting notes, or wiki bundles) with the domain
   charter and the unscored path list — it does not need the threshold `T`,
   which only the selection script below applies. It appends one cache line per
   note it actually scores, skipping any pair already cached.
5. Run
   `python3 scripts/select-focused-candidates.py <domain> --min-confidence T` to
   get the deterministic candidate list: cached ratings for the domain with
   already-curated paths filtered out, sorted descending by confidence, and
   walked from the top, stopping at the first sub-threshold entry. Take at most
   `N` paths from its (already-ranked) output — this is a script decision, not
   researcher/supervisor reasoning.
6. Dispatch the domain curator on **only those selected paths**. The curator
   still reads each selected note in full and checkpoints the ledger per note.
7. **Ledger policy (hard):** notes below threshold, near-misses, and notes not
   yet cached remain **unreviewed** — do not append them to the ledger. Only the
   curator ledger-writes, and only after it fully reviews a selected note
   (whether or not it yielded wiki content). A cached low-confidence or deferred
   score never causes a ledger write. A later normal `/curate` (or another
   focused pass) can still see deferred notes.

### Landscape mode (`--landscape`)

A single cross-bundle sweep that tells every domain which fleeting notes might
be worth reading, before any per-domain researcher or curator opens them. See
`docs/landscape.md` for the full mode and cache spec. Unlike every other mode
here, it does not target one (or all) domain's curators at all — it only
populates the shared `landscape/overlap.jsonl` cache that a later `--focused`
gather step may optionally consult.

## Procedure (normal mode)

1. Parse arguments: domain slugs and optional `--limit` / `limit=`. Default
   limit is `15`. Reject unknown slugs. If `--focused` is set, follow **Focused
   mode procedure** instead. If `--landscape` is set, follow **Landscape mode
   procedure** instead (rejecting any domain slug given alongside it).
2. Quick pre-check (**paths vs ledgers only**): for each target domain, list
   Markdown paths under `fleeting/` and compare to path lines in
   `curation/<slug>.txt`. Skip (and say you skipped) any domain with no
   unreviewed paths. Optionally run
   `sh scripts/curation-progress.sh --pending-only` for the same path-only view.
3. Dispatch a curator for each remaining domain **in parallel**, using the
   harness-specific method below. Pass the resolved limit into every curator
   prompt. The layout makes this safe (each curator writes only to its own
   bundle and its own ledger, and treats `fleeting/` as read-only). Remind each
   curator to follow `docs/curation.md` exactly (read every note in full; stop
   after the limit; checkpoint the ledger after each note).
4. When all curators report back, verify the ledgers were updated, and run a
   sanity check with the repo-local `okf` CLI (install via `sh scripts/setup.sh`
   if needed):

   ```sh
   .venv/bin/okf validate --bundle <slug>
   .venv/bin/okf graph --bundle <slug> --broken
   ```

5. Summarise for the user per domain: notes reviewed (and whether the limit
   stopped the run), wiki notes created/extended, anything left pending, and any
   validation findings. Do not auto-dispatch another batch.

## Focused mode procedure

1. Parse: exactly one domain slug, `--focused`, optional `--limit N` (default
   15; reject `all`), optional `--min-confidence T` (default `0.7`).
2. Path-vs-ledger pre-check for that domain only. If nothing is pending, stop.
3. Cache-first candidate gathering: unreviewed paths (per
   `curation/<domain>.txt`) minus paths already cached for this domain (per
   `ratings/<domain>.jsonl`) = the unscored set. Only that set is dispatched to
   the researcher. Do not open fleeting bodies in the supervisor.

   **Optional landscape pre-filter:** if `landscape/overlap.jsonl` has data (a
   prior `/curate --landscape` run), pipe the unscored set through
   `python3 scripts/filter-by-landscape.py <domain>` to drop paths whose
   landscape entry excludes this domain. It is fail-open — any path with no
   landscape entry yet passes through unchanged — so this step never removes a
   candidate this domain would otherwise have seen; it only skips paths a
   landscape sweep already determined do not overlap this domain. Skipping this
   step (no landscape data yet) leaves the gather step exactly as above. See
   `docs/curation.md` (Landscape pre-filter) and `docs/landscape.md`.

4. Dispatch the researcher per **Harness dispatch → Researcher** with the
   unscored path list. It appends one ratings-cache line per note it actually
   scores (skipping any pair already cached) and writes nothing else.
5. Run
   `python3 scripts/select-focused-candidates.py <domain> --min-confidence T`
   (repo root) to get the deterministic candidate list: cached ratings for the
   domain minus already-curated paths, sorted descending by confidence, walked
   from the top and stopped at the first sub-threshold entry — the list is
   sorted, so one sub-threshold hit is sufficient to stop, no need to scan the
   rest. Take at most `N` paths from its (already-ranked) output. If none
   qualify, report that and stop — do not fall back to unscoped curation.
6. Dispatch the domain curator with an explicit candidate list (see focused
   curator prompt below). Curator follows `docs/curation.md` focused-pass rules:
   only those paths, full read, per-note ledger checkpoint.
7. Validate with `okf` as in normal mode. Summarise: paths newly scored this run
   vs reused from cache, selected / deferred by the selection script, curator
   reviewed / created / extended, and that non-selected notes remain unreviewed.

## Landscape mode procedure

1. Parse: `--landscape`, no domain slug, optional `--limit N` (default `40`) or
   `--limit all`. `40` is higher than normal mode's `15` default because this
   pass is cheaper per note — no atomization or wiki writing, just listing
   overlapping bundles — but still bounded by default so a run stays reviewable.
2. Path-only gather: `python3 scripts/list-landscape-unmapped.py` (repo root) —
   fleeting paths with no entry yet in `landscape/overlap.jsonl`. Take at most
   `N` from the top if a numeric limit is set. If nothing is pending, report
   that and stop.
3. Dispatch **one** `fleeting-researcher` run in landscape mode (see Harness
   dispatch → Researcher (landscape mode only)) over that path list. It reads
   every domain charter itself (`.claude/agents/*-curator.md`) and appends one
   `{path, bundles}` line to `landscape/overlap.jsonl` per note it maps,
   immediately after mapping it — an empty `bundles` list is a valid, cached
   result, not a skip.
4. **Never dispatch a second landscape-mode run concurrently over an overlapping
   path set.** Unlike per-domain curator/researcher dispatch, landscape mode
   shares one file across the whole run — see `docs/landscape.md` (Concurrency).
   If more of the backlog remains after this run's limit, a later
   `/curate --landscape` picks it up; do not parallelize by splitting the
   remaining paths across simultaneous dispatches.
5. Report: paths mapped this run, skipped-as-already-mapped (should be zero if
   the gather step worked; a nonzero count is a signal, not an error), and the
   remaining unmapped backlog size.

Landscape mode never curates, never ledger-writes, and never touches
`ratings/<domain>.jsonl`. Its only consumer today is the optional landscape
pre-filter in Focused mode step 3 above (`scripts/filter-by-landscape.py`,
fail-open) — a note with no landscape entry yet is handled by focused mode
exactly as it would be if `--landscape` had never run.

## Harness dispatch

Use exactly one of the following, based on the tools available in this session.
Replace `<LIMIT>` with the resolved limit (`15`, another `N`, or `all` in normal
mode; `40`, another `N`, or `all` in landscape mode). Replace `<DOMAIN>`,
`<UNSCORED_PATHS>`, and `<CANDIDATE_PATHS>` in focused mode, and
`<UNMAPPED_PATHS>` in landscape mode.

### Researcher (focused mode only)

Read `agents/fleeting-researcher.md` and dispatch a subagent with that
charter in **charter-scoring mode** — it writes only the ratings cache, never
ledgers, fleeting notes, wiki bundles, or `landscape/overlap.jsonl`. Prompt:

```text
Score these not-yet-cached fleeting notes for <DOMAIN> against
.claude/agents/<DOMAIN>-curator.md: <UNSCORED_PATHS>. For each note
you open and score, append one line to ratings/<DOMAIN>.jsonl
({"path": ..., "bundle": "<DOMAIN>", "confidence": ...}) immediately
after scoring it — do not batch cache writes. Skip (do not re-open)
any path already cached for <DOMAIN>. Do not write to ledgers,
fleeting notes, or wiki bundles. Report how many notes you scored vs
skipped as already cached.
```

Harness mapping:

- **Claude Code** — Agent tool, name `fleeting-researcher`.
- **Antigravity / Gemini** — `define_subagent` / `invoke_subagent` from
  `agents/fleeting-researcher.md` with the ratings-cache path as its
  only enabled write target.
- **Cursor** — Task tool with `subagent_type: generalPurpose` (or
  `fleeting-researcher` if that type is registered), instructions from the
  researcher file, and an explicit forbid on wiki/ledger/fleeting writes
  (ratings-cache appends only).

### Researcher (landscape mode only)

Read `agents/fleeting-researcher.md` and dispatch a subagent with that
charter in **landscape mode** — it writes only `landscape/overlap.jsonl`, never
ledgers, `ratings/*.jsonl`, fleeting notes, or wiki bundles. Prompt:

```text
Landscape mode: map these not-yet-mapped fleeting notes against every
domain charter under .claude/agents/*-curator.md: <UNMAPPED_PATHS>.
For each note you open and map, append one line to
landscape/overlap.jsonl ({"path": ..., "bundles": [...]}) immediately
after mapping it — do not batch cache writes; an empty bundles list
is a valid, cached result, not a skip. Skip (do not re-open) any
path already present in landscape/overlap.jsonl. Do not write to
ledgers, ratings/*.jsonl, fleeting notes, or wiki bundles. Report how
many notes you mapped vs skipped as already cached.
```

Harness mapping is the same as the charter-scoring researcher above — same
agent, different mode and prompt.

### Claude Code — Agent tool (curator)

Launch the curator agent for each remaining domain via the Agent tool, using
the `<domain-slug>-curator` agent name.

Normal prompt:

```text
Perform a curation pass on the unreviewed fleeting notes for your
domain following docs/curation.md. Review at most <LIMIT> notes (or
the full backlog if <LIMIT> is all). Checkpoint the ledger after each
note. Stop when the limit is reached or the backlog is empty — do not
continue into another batch. Report how many you reviewed and how many
remain pending.
```

Focused prompt:

```text
Perform a focused curation pass for your domain following
docs/curation.md (focused/bootstrap section). Curate ONLY these
selected notes (from scripts/select-focused-candidates.py), in
order: <CANDIDATE_PATHS>. Read each in full; checkpoint the ledger
after each. Do not pull other unreviewed notes. Stop after this
list. Report reviewed vs unused and confirm non-listed notes were
left unreviewed.
```

### Antigravity / Gemini — define_subagent + invoke_subagent

For each remaining domain:

1. Read `.claude/agents/<domain-slug>-curator.md`.
2. Call `define_subagent` with:
   - `name`: `<domain-slug>-curator`
   - `description`: from the curator frontmatter
   - `system_prompt`: the body of the curator file, plus the requirement to
     follow `docs/curation.md` and `docs/wiki-rules.md`
   - `enable_write_tools`: `true`
   - `enable_subagent_tools`: `false`
   - `enable_mcp_tools`: `true`
3. Call `invoke_subagent` with the normal or focused curator prompt from the
   Claude Code section above (same wording).

### Cursor — Task tool (curator)

For each remaining domain, launch a Task subagent with
`subagent_type: <domain-slug>-curator`. Use the same normal or focused curator
prompt as above.

## Rules

- Never curate directly in the main session — always go through the domain's
  curator agent, so the charter and wiki rules are applied.
- **Supervisor non-read / non-filter (hard):** the curate supervisor may only
  list paths under `fleeting/` and compare them to `curation/<slug>.txt` and
  `ratings/<slug>.jsonl`. `scripts/curation-progress.sh` covers the ledger half
  and ratings-cache backlog stats (`MAX_P`, `P>=0.7`) without opening note
  bodies; the ratings-cache unscored-path gather step for `/curate --focused`
  still has no scripted equivalent, so that half is compared by hand. It must
  not open or read fleeting note bodies, and must not drop candidates based on
  title, directory name, source slug, or any other heuristic. Relevance scoring
  belongs only inside the dispatched researcher; candidate selection belongs
  only to `scripts/select-focused-candidates.py`. In focused mode, the
  cache-first gather step and running/forwarding the selection script's output
  are dispatch and deterministic tooling — not supervisor judgment.
- Never curation-shortcut: curators must read every selected note in full. Do
  not allow bulk-adding or skipping files based on path patterns or titles
  without reading.
- Honour `--limit`: curators stop after N reviewed notes with the ledger up to
  date; do not imply or instruct "always continue through the full backlog"
  unless `--limit all` was given (normal mode only).
- Focused mode: never ledger-write for notes that are deferred, not yet cached,
  or not selected by `scripts/select-focused-candidates.py`. A cached
  low-confidence or deferred score never becomes a ledger entry by itself — only
  a curator's full read does that.
- Landscape mode: the supervisor gathers with
  `scripts/list-landscape-unmapped.py` only — same non-read / non-filter posture
  as focused mode's gather step, path comparison only, no note-body reads. Never
  dispatch two landscape-mode researcher runs concurrently over an overlapping
  path set (see `docs/landscape.md`, Concurrency). Landscape mode never gates or
  replaces charter scoring — `scripts/filter-by-landscape.py` is fail-open, so a
  missing or stale landscape entry never hides a candidate from a domain that
  would otherwise have seen it.
- Do not commit or push unless the user asked for that.
