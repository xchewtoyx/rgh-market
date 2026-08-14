# rgh-market

Claude Code plugin marketplace for [`rgh-sme`](https://github.com/xchewtoyx/rgh-sme)
and [`rgh-pre`](https://github.com/xchewtoyx/rgh-pre) — Zettelkasten-style Agent
Plugins wiki bundles. The catalog is
[`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json); the
plugin archives themselves are hosted on Cloudsmith
(`chewcorp-kl2f/xchewtoyx`, raw format), which both plugin repos already
publish to on every version bump.

## Install

```shell
/plugin marketplace add xchewtoyx/rgh-market
/plugin install rgh-sme@rgh-plugins
/plugin install rgh-pre@rgh-plugins
```

## How it's wired

- Each `plugins[]` entry in `marketplace.json` uses an
  [`archive` source](https://code.claude.com/docs/en/plugin-marketplaces#zip-archives):
  an HTTPS URL to the versioned zip on Cloudsmith, pinned with a `sha256`
  digest. Claude Code downloads and verifies the archive directly — no git
  clone of the plugin repos needed.
- Cloudsmith's raw-package downloads and packages API are both public for
  anonymous reads on this repo (only *pushing* new packages needs the
  `CLOUDSMITH_API_KEY` that `rgh-sme`/`rgh-pre`'s CI holds), so no secrets are
  needed here.
- `rgh-sme` and `rgh-pre` pack their `plugin.json` (Agent Plugins 1.0.0
  schema, not Claude Code's own `.claude-plugin/plugin.json`) at the archive
  root alongside `skills/`. Every entry here sets `"strict": false` so Claude
  Code ignores that foreign manifest and falls back to its default
  `skills/*/SKILL.md` scan, which the existing package layout already
  satisfies — no changes needed to either plugin repo's build/pack/publish
  pipeline.

## Keeping it current

`scripts/sync_marketplace.py` queries the Cloudsmith packages API for the
newest package matching each entry's name (parsed from its existing
Cloudsmith URL — no separate config file) and rewrites `version`,
`source.url`, and `source.sha256` in place when a newer one has been
published. [`.github/workflows/sync-marketplace.yml`](.github/workflows/sync-marketplace.yml)
runs it on a schedule (and via manual dispatch) and commits the result when
it changes.

```shell
python3 scripts/sync_marketplace.py          # rewrite marketplace.json in place
python3 scripts/sync_marketplace.py --check  # exit 1 if it would change
```

Adding a plugin from the same Cloudsmith repo: add a new entry to
`plugins[]` pointing at any existing version of its package (any valid
`archive` source with a `dl.cloudsmith.io/public/...` URL); the next sync
run picks up its latest version automatically.

## Tests

```shell
pip install -r requirements-dev.txt
pytest tests/ -v
```
