# bundle-curator

Harness-agnostic curation tooling extracted from [`rgh-pre`](https://github.com/xchewtoyx/rgh-pre)
and [`rgh-sme`](https://github.com/xchewtoyx/rgh-sme): the skills, shared
agents, and scripts an OKF wiki repo uses to turn raw "fleeting" literature
notes into curated, linked wiki bundles. This is **not** the consumer-facing
wiki content plugin (see `../rgh-pre` and `../rgh-sme` in this marketplace) —
it ships no wiki notes and answers no retrieval questions. It is the
maintainer-side tooling that *produces* that content.

**Authoring model:** unlike `../rgh-pre` and `../rgh-sme`, which are vendored
from Cloudsmith by `scripts/sync_marketplace.py`, this plugin is **mastered
directly in this repo** — edit `plugins/bundle-curator/` here and bump
`plugin.json`'s `version`. There is no `.cloudsmith-source.json` stamp, so
`scripts/sync_marketplace.py` prints a warning and leaves this directory
untouched every run (it only syncs plugins that carry that stamp). Once `rgh-pre`/`rgh-sme` (and any future domain-wiki repo) actually
depend on this plugin instead of carrying their own copy of this tooling,
mastering may move upstream to one of those repos, or to a dedicated repo of
its own — this repo is the starting point, not necessarily the permanent home.

## What a consuming repo must supply

This plugin is domain-agnostic — `scripts/domains.py` reads the current
domain-slug list from the consuming repo's `okf-core.toml`, never a hardcoded
table. Beyond that config, a repo that installs this plugin still needs, in
its own tree (none of this ships here):

- `okf-core.toml` — the domain-bundle declarations `scripts/domains.py` reads.
- `.claude/agents/<slug>-curator.md` per domain — the curator charter (In
  scope / Boundaries) and curation persona. Domain-specific by nature; not
  something a shared plugin can supply.
- `fleeting/`, `curation/<slug>.txt`, `ratings/<slug>.jsonl`,
  `landscape/overlap.jsonl`, `watch/<slug>.jsonl`, and the domain bundle
  directories themselves — all repo-local curation state these skills read
  and append to.
- The `okf` CLI (install path: `.venv/bin/okf`, see `scripts/setup.sh` in
  `rgh-pre`/`rgh-sme` for the current install recipe) for validation and
  search during curation.
- `pymupdf` (see `requirements.txt` here) if `scripts/dump-source-chapters.py`
  will be used for PDF/EPUB onboarding.

## Layout

- `skills/` — `onboard`, `curate`, `progress`, `charter-review`, `catch-up`,
  `score-catchup`, `source-watch`. Each `SKILL.md` is the full harness-facing
  procedure.
- `agents/` — the domain-agnostic agents skills dispatch to:
  `fleeting-researcher` (charter-scoring and landscape-mapping modes),
  `charter-researcher`, `chapter-writer`, `source-watch-researcher`. Per-domain
  `<slug>-curator` agents are not here — they're consuming-repo content.
- `scripts/` — deterministic selection/reporting tooling the skills shell out
  to (candidate selection, progress reporting, chapter dumping, etc.). Pure
  Python 3, cwd-relative (they locate the repo root by walking up for
  `okf-core.toml`), so they work unmodified from wherever a harness installs
  this plugin.
- `docs/` — the detailed procedures (`curation.md`, `landscape.md`,
  `charter-review.md`, `wiki-rules.md`, `source-watch.md`) the skills point to
  rather than restate.
- `tests/` — pytest coverage for `scripts/`, ported alongside the scripts so
  this repo's own `pytest tests/ -v` (via `requirements-dev.txt` plus this
  directory's `requirements.txt`) still exercises them.

## Provenance

Ported from `rgh-pre` (canonical source for everything except `source-watch`,
which only `rgh-sme` has today) as of the repos' `main` at extraction time.
Two real drifts between the two repos' copies were resolved in favour of
`rgh-pre`'s newer version: a `fleeting/`-scan bug fix (stray top-level files
under `fleeting/` are no longer treated as source notes) and consistent
`P>=0.7` (at-or-above) confidence-threshold semantics, matching what the
selection scripts actually gate on. `source-watch`'s implicit
`agentic-engineering` default was replaced with a required `--focused
<domain-slug>` argument, since a hardcoded default domain has no meaning
across multiple consuming repos with different domain sets.
