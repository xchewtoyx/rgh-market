# rgh-market

Claude Code plugin marketplace for [`rgh-sme`](https://github.com/xchewtoyx/rgh-sme)
and [`rgh-pre`](https://github.com/xchewtoyx/rgh-pre) — Zettelkasten-style Agent
Plugins wiki bundles — plus [`bundle-curator`](plugins/bundle-curator), the
harness-agnostic curation tooling those two repos (and future OKF wiki repos)
share. The catalog is
[`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json). Cloudsmith
(`chewcorp-kl2f/xchewtoyx`, raw format) is the artifact store the `rgh-sme` and
`rgh-pre` plugin repos already publish to on every version bump; this repo
vendors the newest package from there into `plugins/<name>/` so Claude Code can
install straight from git. `bundle-curator` is different — see
[Mastering `bundle-curator`](#mastering-bundle-curator) below.

## Install

```shell
/plugin marketplace add xchewtoyx/rgh-market
/plugin install rgh-sme@rgh-plugins
/plugin install rgh-pre@rgh-plugins
/plugin install bundle-curator@rgh-plugins
```

## How it's wired

- **Cloudsmith is the artifact store, git is the install path.** Claude
  Code's `archive` plugin source (an HTTPS zip + `sha256`) is what a direct
  Cloudsmith reference would use, but the stable CLI (verified against
  2.1.223) doesn't support it yet — only `github`, `url` (git), and
  `git-subdir` sources install today. So each `marketplace.json` entry
  instead points at a `./plugins/<name>` [relative path](https://code.claude.com/docs/en/plugin-marketplaces#relative-paths)
  *inside this repo*, and `plugins/<name>/` is a vendored, verified copy of
  the newest Cloudsmith package — install works on every Claude Code
  version, not just ones with archive support.
- Cloudsmith's raw-package downloads and packages API are both public for
  anonymous reads on this repo (only *pushing* new packages needs the
  `CLOUDSMITH_API_KEY` that `rgh-sme`/`rgh-pre`'s CI holds), so no secrets
  are needed here either.
- `rgh-sme` and `rgh-pre` pack their `plugin.json` (Agent Plugins 1.0.0
  schema, not Claude Code's own `.claude-plugin/plugin.json`) at the package
  root alongside `skills/`. Every entry here sets `"strict": false` so
  Claude Code ignores that foreign manifest and falls back to its default
  `skills/*/SKILL.md` scan, which the vendored layout already satisfies —
  no changes needed to either plugin repo's build/pack/publish pipeline.
- Each `plugins/<name>/.cloudsmith-source.json` stamp records where that
  directory is vendored from (Cloudsmith owner/repo/package name) and what
  was last synced (version, `sha256`, source URL, timestamp) — the audit
  trail for "what's actually in git right now."

## Keeping it current

`scripts/sync_marketplace.py` walks `plugins/*/`, reads each
`.cloudsmith-source.json` stamp, queries the Cloudsmith packages API for the
newest package with that name, and — only if its `sha256` differs from what's
stamped — downloads it, re-verifies the checksum against what the API
reported, and extracts it over the vendored directory (clearing stale files
first, so removed files don't linger). It then updates that plugin's
`version` in `marketplace.json`.
[`.github/workflows/sync-marketplace.yml`](.github/workflows/sync-marketplace.yml)
runs it on a schedule (and via manual dispatch) and commits the result when
it changes.

```shell
python3 scripts/sync_marketplace.py          # vendor the latest packages in place
python3 scripts/sync_marketplace.py --check  # exit 1 if anything would change
```

Adding a plugin from the same Cloudsmith repo: create
`plugins/<name>/.cloudsmith-source.json` with `{"owner", "repo", "name"}`,
add a matching entry to `marketplace.json`'s `plugins[]` with
`"source": "./plugins/<name>"`, and the next sync run vendors it and keeps
its version current.

**Trade-off:** this repo carries a full copy of each plugin's package
(~6 MB for `rgh-sme`, ~1.6 MB for `rgh-pre` today) instead of just a
pointer, and that copy — plus git history — grows with every release. That's
the price of installing on Claude Code versions without `archive` support;
once that's broadly available, entries can switch back to a direct
Cloudsmith `archive` source and `plugins/` can go away.

## Mastering `bundle-curator`

`plugins/bundle-curator/` is not vendored — it has no `.cloudsmith-source.json`
stamp, so `scripts/sync_marketplace.py` leaves it alone (a stderr warning, no
write) on every run. It was extracted directly from `rgh-pre`'s and
`rgh-sme`'s `.claude/skills/`, `.claude/agents/`, and `scripts/` — the
maintainer-side tooling that curates fleeting notes into wiki bundles, as
opposed to the consumer-facing wiki content the `rgh-sme`/`rgh-pre` entries
ship. Edit it in place here and bump `plugin.json`'s `version` by hand; see
[`plugins/bundle-curator/README.md`](plugins/bundle-curator/README.md) for
what it expects a consuming repo to supply (`okf-core.toml`, per-domain
curator charters, curation state) and its provenance. `rgh-pre` and `rgh-sme`
still carry their own copies of this tooling for now — neither depends on this
plugin yet.

## Tests

```shell
pip install -r requirements-dev.txt -r plugins/bundle-curator/requirements.txt
pytest tests/ plugins/bundle-curator/tests/ -v
```
