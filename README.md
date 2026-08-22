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

### Claude Code

```shell
/plugin marketplace add xchewtoyx/rgh-market
/plugin install rgh-sme@rgh-plugins
/plugin install rgh-pre@rgh-plugins
/plugin install bundle-curator@rgh-plugins
/plugin install rgh-mms@rgh-plugins
```

### Cursor (desktop, CLI, team marketplace)

Cursor does not read `.claude-plugin/marketplace.json`. The Cursor catalog is
[`.cursor-plugin/marketplace.json`](.cursor-plugin/marketplace.json), generated
from the Claude catalog so the two cannot drift. Each vendored plugin also
carries a thin `.cursor-plugin/plugin.json` sidecar — Cursor Team Marketplace
resolution looks for that file — without replacing the Agent Plugins
`plugin.json` Cloudsmith already ships.

**Team / Enterprise** (best for org-wide desktop + Cloud Agents when a plugin
is marked Required): Dashboard → Plugins → Add Marketplace → Import from Repo
→ `https://github.com/xchewtoyx/rgh-market`. Then set each plugin to Default
On or Required.

**CLI / desktop user marketplace:**

```shell
agent plugin marketplace add https://github.com/xchewtoyx/rgh-market
```

Then install from `/plugin` or Customize. Local smoke-test without a
marketplace import:

```shell
python3 scripts/install_cursor_plugins.py --all
```

That copies each plugin to `~/.cursor/plugins/local/<name>/`.

### Cursor Cloud Agents

Cloud Agents boot a fresh VM. They do **not** see plugins you installed on a
laptop, and `.cursor/environment.json` has no `plugins` field. They *do* load:

- skills committed at `.cursor/skills/` (or `.agents/skills/`) in the cloned repo
- skills written to the VM's `~/.cursor/skills/` by the environment `install` script
- Team Marketplace plugins marked **Required**
- local plugin trees under `~/.cursor/plugins/local/<name>/`

The installer targets those last two paths. On a **personal or team Cloud
Agent environment**, add this to the environment install script (Dashboard →
Cloud Agents → environment, or `.cursor/environment.json` `install` in a
consuming repo):

```shell
curl -fsSL https://raw.githubusercontent.com/xchewtoyx/rgh-market/main/scripts/install_cursor_plugins.py | python3 - --all
```

Subset:

```shell
curl -fsSL https://raw.githubusercontent.com/xchewtoyx/rgh-market/main/scripts/install_cursor_plugins.py | python3 - rgh-sme rgh-pre
```

`python3 - --all` is required when piping: stdin is the script, so flags go
after `-`. The script fetches [`.cursor-plugin/catalog.json`](.cursor-plugin/catalog.json)
(plugin names, Cloudsmith archive URL + sha256, skill inventory) and, for
vendored plugins, downloads the same verified zip this repo already mirrors.
`bundle-curator` has no Cloudsmith package — it is extracted from the GitHub
tarball instead.

To pin plugins into **one consuming repo** (so every Cloud Agent on that repo
gets them without an environment install):

```shell
python3 scripts/install_cursor_plugins.py --project --skills-only rgh-sme
git add .cursor/skills && git commit
```

`--list` prints the catalog. `--plugins-only` / `--skills-only` skip one of
the two destinations. Default destinations are `~/.cursor/plugins/local` and
`~/.cursor/skills/<plugin>/<skill>/` (plugin-prefixed so `wiki-router` from
`rgh-sme` and `rgh-pre` do not overwrite each other).

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
- Cursor catalogs are generated, not hand-edited:
  `scripts/cursor_catalog.py` reads `.claude-plugin/marketplace.json` plus
  each plugin's layout/stamp and writes `.cursor-plugin/marketplace.json`
  (Team Marketplace / `agent plugin marketplace add`),
  `.cursor-plugin/catalog.json` (Cloud Agent installer), and
  `plugins/<name>/.cursor-plugin/plugin.json` (Cursor sidecar).
  `scripts/sync_marketplace.py` runs that step after every vendor update.
  `scripts/cursor_catalog.py --check` (and the Python-tests workflow) fail
  if the committed Cursor files are stale.

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
python3 scripts/sync_marketplace.py          # vendor the latest packages and refresh Cursor catalogs
python3 scripts/sync_marketplace.py --check  # exit 1 if anything would change
python3 scripts/cursor_catalog.py            # regenerate Cursor catalogs only
python3 scripts/cursor_catalog.py --check    # exit 1 if Cursor catalogs are stale
```

Adding a plugin from the same Cloudsmith repo: create
`plugins/<name>/.cloudsmith-source.json` with `{"owner", "repo", "name"}`,
add a matching entry to `.claude-plugin/marketplace.json`'s `plugins[]` with
`"source": "./plugins/<name>"`, and the next sync run vendors it, keeps its
version current, and regenerates the Cursor catalogs. Do not edit
`.cursor-plugin/` by hand.

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
python3 scripts/cursor_catalog.py --check
pytest tests/ plugins/bundle-curator/tests/ -v
```
