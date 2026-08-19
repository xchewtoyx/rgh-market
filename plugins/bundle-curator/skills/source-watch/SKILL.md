---
name: source-watch
description: >-
  Discover candidate research publications for onboarding via core-learning
  citation snowball (Signal A) plus thin B/C corroboration; queue survivors in
  suggested-sources (never auto-onboard).
argument-hint: "--focused <domain-slug> [--limit N] [--min-cores K]"
---

# Source watch

Find **not-yet-onboarded** publications that look like shared ground rules for a
domain — stable, vendor-neutral, multiply attested — and queue them in
`docs/suggested-sources.md` for a later human `/onboard`.

Full procedure: `docs/source-watch.md`. Follow it; do not invent a web crawl or
auto-onboard.

## Domains

Any slug from `python3 scripts/domains.py`. Reject unknown slugs. Unlike
`/curate`, there is no all-domains mode and no default slug — `--focused
<domain-slug>` is required, since silently picking one domain out of a
consuming repo's set would be arbitrary.

## Arguments

- Required `--focused <domain-slug>`.
- Optional `--limit N` — max survivors to queue (default **10**).
- Optional `--min-cores K` — minimum distinct citing cores for Signal A (default
  **2**).
- Optional `--min-charter-fit T` — minimum researcher charter_fit (default
  **0.7**).

## Procedure

1. Run setup if needed (`sh scripts/run-setup.sh`). Missing `okf` is non-fatal.
2. Read `docs/source-watch.md` in full.
3. Resolve the focused domain; read its curator charter path only
   (`.claude/agents/<slug>-curator.md`) for the researcher prompt — do not
   pre-filter candidates yourself from the charter.
4. **Seed paths (deterministic, path metadata only):**

   ```sh
   python3 scripts/list-source-watch-seeds.py <domain-slug>
   ```

   Use the script's listed `seed_paths`. Do **not** open fleeting note bodies in
   the supervisor.

5. Dispatch **source-watch-researcher** with: domain slug, charter path, seed
   path list, and instruction to append only to `watch/<domain-slug>.jsonl`. See
   Harness dispatch below.
6. After the researcher returns, select survivors:

   ```sh
   python3 scripts/select-watch-candidates.py <domain-slug> \
     --min-cores <K> --min-charter-fit <T> --limit <N>
   ```

7. **Thin Signal B/C pass** (supervisor): for each selected title, note citation
   mass (OpenAlex / Semantic Scholar / Scholar) and whether a **non-author**
   vendor or OSS harness adopted the named pattern. Mark `unchecked` when
   evidence is thin. Apply anti-signals from `docs/source-watch.md`; drop
   failures.
8. Keep only **A ∧ (B ∨ C)**. Prefer A∧C over A∧B when ordering the queue
   writeback.
9. Update `docs/suggested-sources.md`: remove any queued entry that is now
   onboarded under `fleeting/`; append or refresh a **Research watch candidates
   (`<domain>`)** section with the survivors and signal bullets.
10. Summarise: seeds dispatched, cache lines added (from researcher report),
    selected titles, B/C outcomes, files written. Suggest `/onboard` only as a
    later human step — do not run it.

## Harness dispatch — source-watch-researcher

Read `agents/source-watch-researcher.md`. Prompt:

```text
Source-watch for domain-slug <DOMAIN_SLUG>.
Read charter at .claude/agents/<DOMAIN_SLUG>-curator.md.
Read only these seed fleeting paths (full text):
<SEED_PATHS>
Append candidate observations to watch/<DOMAIN_SLUG>.jsonl per
source-watch-researcher.md and docs/source-watch.md.
Skip works already under fleeting/. Checkpoint per candidate.
Return counts only — no full note text.
```

Harness mapping:

- **Claude Code** — Agent tool, name `source-watch-researcher`.
- **Antigravity / Gemini** — `define_subagent` / `invoke_subagent` from
  `agents/source-watch-researcher.md` with write tools enabled for
  `watch/` only.
- **Cursor** — Task tool with `subagent_type: generalPurpose` (or
  `source-watch-researcher` if registered), instructions from the researcher
  file.

## Finish

Report only:

- focused domain and limits used
- seed path count
- researcher cache append count
- selected candidates (title + core count + charter_fit)
- B/C disposition per survivor
- whether `docs/suggested-sources.md` was updated

Do not onboard. Do not curate. Do not edit domain bundles or `fleeting/`.
