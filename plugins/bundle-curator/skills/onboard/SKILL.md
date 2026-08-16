---
name: onboard
description: Distil a source text into fleeting/ literature notes.
argument-hint:
  <path-or-description-of-source-text> [--chapter <locator>] [--limit N|all]
---

# Onboard a source text

Turn a source text into literature notes under `fleeting/`, ready for the domain
curators to process later with `/curate` (or `curate`). Once this run's notes
are written, a post-onboard pass (below) maps and scores them against every
domain charter so that a later `/curate` pass starts from a warm cache instead
of a cold backlog — see Post-onboard: landscape mapping + scoring.

## Session bounds (hard)

- **One source per session.** Process exactly one source text in this
  invocation. Do not open, compare, or distill a second book, article, or
  document in the same run. If the user names several sources, stop and ask
  which one to onboard now; leave the rest for later sessions.
- **One chapter for limited-context / small-model runs.** When the model is
  small, context is tight, or the user passes `--chapter <locator>` (chapter,
  section, or equivalent range), onboard **only that unit** — read it fully,
  write its note(s), then stop. Do not continue into the next chapter in the
  same session. A later `/onboard` on the same `<source-slug>` continues
  numbering.
- For capable models with ample context and no `--chapter` bound, a single
  source may still be onboarded across multiple chapters in one session — but
  never more than one source, and never by skimming.

## Arguments

- Source path or description (required).
- Optional `--chapter <locator>` — scope to one chapter/section (by number or
  title substring match against the chapter map).
- Optional batch limit for large PDF/EPUB chapter-batch mode (pick exactly one
  form):
  - `--limit N` or `limit=N` where `N` is a positive integer (default **`3`**)
  - `--limit all` or `limit=all` to dispatch every remaining chapter in one run

## Modes

### Direct mode (default for small sources)

Use when the source is pasted content, Markdown, plain text, or a short document
the supervisor can read in full without chapter-batch dispatch.

Read the in-scope material in full before writing notes — chunk the reading if
needed, but never skim. Out-of-scope chapters of the same source stay unread
until a later session.

The supervisor writes fleeting notes directly (no subagent dispatch). Once every
note for this run is written, run the post-onboard landscape mapping + scoring
pass (see Post-onboard: landscape mapping + scoring below) over exactly the
paths just written.

### Chapter-batch mode (large PDF/EPUB)

Use when the source is a **PDF or EPUB file path** (or when
`incoming/<source-slug>/chapter-map.json` already exists from a prior dump).

1. Run `scripts/dump-source-chapters.py` to produce per-chapter plain-markdown
   dumps and `incoming/<source-slug>/chapter-map.json`.
2. If the dump reports `mode: no-outline`, first check whether the source's own
   container format exposes structural navigation metadata (e.g. an EPUB's
   `get_toc()` — entry titles and page/anchor positions only, even if entries
   are named essays/letters/sections rather than "Chapter N"). If so, build
   `incoming/<source-slug>/chapter-map.json` directly from that metadata —
   titles and positions only, never prose — grouping entries into sensible
   chapter units along the source's own structural boundaries (e.g. its Part
   divisions), and continue chapter-batch mode as normal. Only if no such
   structural metadata exists at all (a true no-outline case, typically a
   scanned/flat PDF), stop after front-matter extraction and ask the user to
   supply a chapter map, then re-run the dump script with `--chapter-map` before
   continuing.
3. Resume check (**paths only**): list `fleeting/<source-slug>/` and compare
   two-digit prefixes (`NN-`) to chapter numbers in the map. Skip chapters
   already onboarded.
4. Resolve batch scope: pending chapters not yet in `fleeting/`, capped by
   `--limit` (default `3`) or all pending when `--limit all`.
5. If `--chapter <locator>` is set, filter the pending list to that chapter only
   (match chapter number or title substring).
6. Dispatch one **chapter-writer** subagent per chapter in the batch **in
   parallel**.
7. Collect path-only reports; confirm output files exist via directory listing.
   Do not read fleeting note bodies or dump file bodies in the supervisor.
8. Run the post-onboard landscape mapping + scoring pass (see Post-onboard:
   landscape mapping + scoring below) over exactly the paths confirmed in
   step 7.

The supervisor must never open the original PDF/EPUB, page images, or chapter
dump files. Structured metadata from `chapter-map.json` (paths, numbers, titles)
is allowed; prose source text is not.

## Input

The user supplies the source: a file path (PDF, EPUB, Markdown, text), pasted
content, or a pointer to material already in the session. Optional
`--chapter <locator>` scopes the run to one chapter/section.

## Output

Write literature notes into a subfolder per source:
`fleeting/<source-slug>/<nn>-<topic-slug>.md`, where `<source-slug>` is a short
kebab-case identifier for the text (e.g. `mans-search-for-meaning`) and `<nn>`
is a two-digit ordering prefix following the source's own structure (typically
one note per chapter or major section).

In chapter-batch mode, `nn` comes from the chapter map (pre-assigned to each
chapter-writer so parallel writes cannot collide).

Each note starts with this frontmatter:

```yaml
---
type: fleeting
title: "Meaning Through Suffering"
source:
  title: "Man's Search for Meaning"
  authors: "Viktor E. Frankl"
  locator: "Part One"
captured: 2026-08-05
---
```

- `type: fleeting` — always, exactly.
- `source.locator` — the chapter/section/page range the note covers, precise
  enough for a curator to cite it in a wiki note's `sources:` field.
- `captured` — today's date (formatted as YYYY-MM-DD).
- Do NOT add a `curated` field or any per-domain tracking — curation state lives
  in `curation/*.txt` ledgers, not in the notes.

## What a fleeting note contains

These are literature notes, not wiki notes. The curators will only ever see
these notes, not the original text, so density and fidelity matter:

- Capture the claims, definitions, techniques, arguments, numbers, and worked
  examples the text actually makes — faithfully, in condensed form.
- Preserve the author's terminology and any memorable framing.
- Note explicit locators (chapter, section) for significant claims so they can
  be traced later.
- Do NOT atomize, do NOT add wiki links, do NOT impose the wiki's structure —
  that is the curators' job. A fleeting note may freely span many concepts.
- Stay **destination-agnostic**: do not map material onto domain bundles,
  suggest which wikis should consume it, or compare it to existing wiki or
  fleeting notes. One source only — no cross-source synthesis and no
  "disagreements with the knowledge base." (This governs how you _write_ a note.
  The separate post-onboard pass below maps finished notes to bundles after the
  fact, by dispatching `fleeting-researcher` — it never feeds back into how a
  note is written, including any note written afterward in the same or a later
  session.)

## Rules

- Treat `fleeting/` as append-only: never modify or delete notes from previously
  onboarded sources.
- If the same source is onboarded again (e.g. more chapters), reuse its existing
  `<source-slug>` folder and continue the numbering.
- Do not write anything into the domain bundle folders or curation ledgers
  (`curation/<domain>.txt`) — note-writing stops at `fleeting/`. The
  post-onboard pass below additionally writes cache lines to
  `landscape/overlap.jsonl` and `ratings/<domain>.jsonl` (the same two files
  `/curate --landscape` and `/curate --focused` write) — nothing else, and never
  a domain bundle or a ledger.
- Do not read domain bundle notes, curation ledgers, or other sources' fleeting
  notes for comparison during onboard. Listing `fleeting/<source-slug>/` to
  continue numbering is fine.
- **Chapter-batch supervisor discipline (hard):** do not read dump file bodies,
  fleeting note bodies, or the original PDF/EPUB. Dispatch chapter-writers and
  verify outputs by path listing only.
- The post-onboard pass is dispatch and deterministic tooling, not supervisor
  reasoning: the onboard supervisor itself never opens a fleeting note body to
  decide its bundles or score it — that judgment belongs to the dispatched
  `fleeting-researcher`, exactly as in `/curate` (see docs/landscape.md,
  docs/curation.md).

## Procedure (chapter-batch mode)

1. Parse arguments: source path, optional `--chapter`, optional `--limit`
   (default `3`). Reject unknown flags.
2. Run setup if needed (`sh scripts/run-setup.sh`).
3. Dump chapters:

   ```sh
   .venv/bin/python3 scripts/dump-source-chapters.py <SOURCE> [--slug <source-slug>]
   ```

   Read only the script's stdout summary and
   `incoming/<source-slug>/chapter-map.json` metadata (not dump file bodies).

4. Load chapter map. Extract per chapter: `number`, `title`, `dump_path`, and
   derive `nn` as `f"{number:02d}"`.
5. Resume: list `fleeting/<source-slug>/` (paths only). A chapter is done if any
   file matches `^<nn>-` or `^<nn>[a-z]?-`.
6. Build pending chapter list. Apply `--chapter` filter if set. Cap by `--limit`
   unless `all`.
7. Infer or ask for `source.title` and `source.authors` if not obvious from the
   filename or user input (metadata only — do not read dump bodies).
8. Dispatch chapter-writers in parallel (see Harness dispatch). Pass each writer
   its dump path, `nn`, chapter metadata, and source frontmatter fields.
9. Collect path-only reports. List `fleeting/<source-slug>/` to confirm new
   files exist.
10. Run the post-onboard landscape mapping + scoring pass (see Post-onboard:
    landscape mapping + scoring below) over exactly the paths confirmed in
    step 9.
11. Summarise: chapters processed, note paths written, chapters remaining,
    whether another `/onboard` invocation is needed, plus the post-onboard
    pass's own report (bundles identified, domains scored).

## Harness dispatch — chapter-writer

Read `agents/chapter-writer.md` and dispatch one subagent per chapter in
the batch. Prompt:

```text
Onboard chapter <CHAPTER_NUMBER> for source-slug <SOURCE_SLUG>.
Read only dump_path: <DUMP_PATH>.
Use pre-assigned nn prefix: <NN>.
Chapter title: <CHAPTER_TITLE>.
Source frontmatter: title="<SOURCE_TITLE>", authors="<AUTHORS>",
locator="ch. <CHAPTER_NUMBER>", captured=<TODAY>.
Write fleeting notes under fleeting/<SOURCE_SLUG>/ following
chapter-writer.md and the onboard skill content rules. Return paths
and one-line summaries only — never full note text.
```

Harness mapping:

- **Claude Code** — Agent tool, name `chapter-writer` (one invocation per
  chapter; parallel when the harness allows).
- **Antigravity / Gemini** — `define_subagent` / `invoke_subagent` from
  `agents/chapter-writer.md` with write tools enabled for `fleeting/`
  only.
- **Cursor** — Task tool with `subagent_type: chapter-writer` (or
  `generalPurpose` with chapter-writer charter if the type is not registered),
  one task per chapter in parallel.

The post-onboard pass below dispatches `fleeting-researcher` the same way
`/curate --landscape` and `/curate --focused` do — see
`skills/curate/SKILL.md` (Harness dispatch → Researcher) for the exact
prompts and harness mapping for both modes; this skill does not repeat them.

## Post-onboard: landscape mapping + scoring

Runs once, after every note this run is going to write has been written (direct
mode) or the batch's chapter-writers have all returned (chapter-batch mode) —
over exactly this run's new paths, never the wider `fleeting/` backlog. It
writes only `landscape/overlap.jsonl` and `ratings/<domain>.jsonl` —
`fleeting-researcher`'s two cache targets (see `docs/landscape.md` and
`docs/curation.md`) — never `curation/<domain>.txt`, a domain bundle, or
`fleeting/` itself, and it never curates anything. The point is that a later
`/curate` (normal or `--focused`) starts from a warm cache across every domain
this run's notes actually touched, instead of a cold backlog it has to discover
from scratch.

1. **Path-only input**: use exactly the paths this run wrote — already known
   from the note-writing step (direct mode) or the chapter-writers' path-only
   reports (chapter-batch mode). Do not re-derive the input with
   `scripts/list-landscape-unmapped.py`; that would also sweep in any historical
   backlog other sessions left unmapped, which belongs to a separate
   `/curate --landscape` run, not this one.
2. Dispatch **one** `fleeting-researcher` run in **landscape mode** (see
   `agents/fleeting-researcher.md`) over exactly those paths. It reads
   every domain charter itself and appends one `{path, bundles}` line per note
   to `landscape/overlap.jsonl`, immediately after mapping each note.
3. Run `python3 scripts/list-bundles-for-paths.py` (repo root), feeding the same
   path list on stdin, to get the deterministic union of bundles this run's
   notes overlap — this is tooling, not supervisor judgment.
4. For each identified bundle, **in parallel**: run
   `python3 scripts/filter-by-landscape.py <bundle>` (same path list on stdin)
   to get that bundle's subset of this run's paths, then dispatch a
   `fleeting-researcher` run in **charter-scoring mode** over that subset — the
   same dispatch `/curate --focused` uses (see `docs/curation.md`, Ratings
   cache), just triggered here instead of from a later `/curate` invocation.
   Each appends to its own `ratings/<bundle>.jsonl`.
5. If step 3 finds no bundle at all, skip step 4 and say so in Finish — it means
   landscape mode judged none of these notes overlap any existing charter
   closely enough to be worth a scoring pass yet. The notes are still fully
   onboarded; a normal (non-`--focused`) `/curate` pass will still see them.

**Never lets a failure here undo onboarding's success.** The fleeting notes are
already durably written before this pass starts. If a landscape or scoring
dispatch fails partway through, report it in Finish and move on — do not retry
in a loop, and do not report the run as failed. A later `/curate --landscape`
(for the mapping) or `/curate --focused` (for the scoring) can always pick up
whatever this pass did not finish.

## Finish

Report only:

- which source was onboarded (and the chapter/section scope, if bounded)
- how many notes were written and their paths
- whether more of the same source remains for a later session
- the post-onboard pass's own results: bundles identified, how many domains got
  a scoring dispatch, and any dispatch that failed and was left for a later
  `/curate` run

In chapter-batch mode, also report chapters dispatched vs remaining and suggest
the next `/onboard` invocation when batch-limited.

Suggest running `/curate` or `curate` as a later step when ready — it now has a
warm ratings cache to start from, courtesy of the post-onboard pass above. The
**note-writing** rule above stays unchanged: do not require naming relevant
domains, scoring destination fit, or comparing the new notes to the existing
wikis while a note is being written.
