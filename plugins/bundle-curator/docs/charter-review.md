# Charter review procedure

How to propose a rare update to a domain curator charter under
`.claude/agents/<domain-slug>-curator.md`. This is a deliberate, uncommon
workflow — not part of routine `/onboard` or `/curate`.

Charter edits reframe what counts as in-scope for a bundle. They may invalidate
prior curation framing, so they require human review and must never be applied
silently by an agent.

Primary evidence is **authoritative source literature** (via full reads of
matched `fleeting/` notes for the bundle's top-cited sources), not a tour of
already-synthesised wiki notes. The bundle is only a secondary drift check —
sampling it alone is circular, because those notes were filtered through the
current charter.

## When to run this

Run `/charter-review <domain-slug>` only when evidence from the live corpus
suggests the charter is wrong or too vague, for example:

- Curators repeatedly skip dense material that clearly belongs, or repeatedly
  ingest material that belongs to a neighbour.
- Bundle notes cluster around themes the charter never names.
- Boundary lines with adjacent domains are fuzzy, duplicated, or contradicted by
  what each bundle actually holds.
- A new source stream keeps forcing awkward "whose is this?" decisions.

Do **not** run it for polish, style tweaks, or after every curation batch.
Initial charters are starting points; leave them alone until the bundle and
ledger give a concrete reason to realign.

## Roles

| Role               | Who                        | Job                                                                                                   |
| ------------------ | -------------------------- | ----------------------------------------------------------------------------------------------------- |
| Supervisor         | skill session              | Rank citations, dispatch researcher, read neighbour charters, light bundle drift check, emit proposal |
| Charter researcher | `charter-researcher` agent | Full-read selected fleeting source groups; propose literature-grounded In scope themes                |

The supervisor must not substitute a wiki-title skim for the researcher's source
reading.

## Inputs

For exactly one `domain-slug`:

1. Current charter: `.claude/agents/<domain-slug>-curator.md`
2. Citation ranking + fleeting path groups from
   `python3 scripts/bundle-cited-sources.py <domain-slug>`
3. Neighbouring domain charters named in the current Boundaries section
4. Light bundle drift sample (titles + a few boundary-adjacent notes) —
   secondary only
5. Optional: a small sample of ledgered fleeting paths when drafting reopen
   candidates after a widen/realign verdict

## Procedure

### 1. Rank authoritative sources

From the repo root:

```sh
python3 scripts/bundle-cited-sources.py <domain-slug> --top 5
```

The script reads bundle `sources:` / `resource:` frontmatter only (not fleeting
bodies), maps titles to `fleeting/` dirs or `-part*.md` groups, and prints
`dispatch_paths` per source:

- **`full-group`** — small groups (≤15 notes) or loose part-files: every matched
  fleeting path
- **`cited-chapters`** — large multi-domain folders: only chapters cited in this
  bundle's `resource:` locators (e.g. `ch. 14`)

Select sources for the researcher (default):

- The top **3** cited sources that have a fleeting match, or fewer if the bundle
  has fewer matched sources.
- Pass each source's **`dispatch_paths`** list (not necessarily the entire
  folder).
- Optionally add **one** extra fleeting source group that looks dense for this
  domain but is thin or missing in citations (supervisor notes why — citation
  rank can under-weight newly onboarded material).
- Optionally widen a `cited-chapters` source with a few extra paths if the
  primary source reading later suggests a gap — record the rationale. Do not
  silently drop paths from `dispatch_paths`.

If the top-cited source has `fleeting_match: NONE`, try a manual map; if still
none, drop it and take the next matched source. Record gaps.

`cited-chapters` narrowing is evidence-based (what this bundle already grounded
in), not a title-guess filter. Rank-1 / `full-group` sources still get a
complete read of their matched fleeting notes — that is what breaks circular
wiki sampling.

### 2. Dispatch the charter researcher (read-only)

Read `agents/charter-researcher.md` and dispatch a read-only subagent
with that charter. Pass:

- `domain-slug` and path to the current curator charter
- The selected source list (title, cites, `dispatch_mode`, `dispatch_paths`)
- Neighbour slugs from the current Boundaries section

Prompt shape:

> For `<DOMAIN>`, fully read every fleeting note in these `dispatch_paths` for
> the authoritative sources: `<SOURCE_GROUPS>`. Current charter:
> `.claude/agents/<DOMAIN>-curator.md`. Neighbours named in Boundaries:
> `<NEIGHBOURS>`. Return the report sections required by charter-researcher.md.
> Do not write to charters, ledgers, fleeting notes, or wiki bundles.

Harness mapping:

- **Claude Code** — Agent tool, name `charter-researcher`.
- **Antigravity / Gemini** — `define_subagent` / `invoke_subagent` from
  `agents/charter-researcher.md` with write tools disabled.
- **Cursor** — Task tool with `subagent_type: generalPurpose` (or
  `charter-researcher` if registered), instructions from the researcher file,
  explicit forbid on wiki/ledger/fleeting/charter writes.

Do not pre-filter the path list by title. Do not skip the researcher and "just
sample the bundle" unless every selected source lacks fleeting material — and
then say the review is degraded.

### 3. Neighbour Boundaries + light bundle drift (supervisor)

After the researcher returns:

1. Read each neighbouring charter named in Boundaries (and any neighbour the
   researcher newly implicated). Note reciprocal ownership claims.
2. Light drift check only: list bundle concept titles (via
   `.venv/bin/okf list-concepts --bundle <slug>` if available, else `*.md`
   basenames) and open a few boundary-adjacent or orphan-looking notes (about
   5–8). Use this to spot mis-ingest under the old frame — not as the primary
   basis for In scope.
3. Draft Boundaries so literature-grounded In scope stays partitioned against
   neighbours. Multi-domain books must not expand this charter into a
   neighbour's ownership. Call out paired neighbour charter tweaks; do not apply
   them here.

### 4. Emit the proposal (required output)

Produce a review report for a human. Do **not** edit
`.claude/agents/<domain-slug>-curator.md` (or any neighbour charter) unless a
human has explicitly approved the proposal in a later turn.

#### Verdict

One of:

- **Hold** — charter still matches the authoritative sources + partition
- **Clarify** — same ownership, sharper In scope / Boundaries wording
- **Realign** — material moves in or out of scope, or a boundary with a
  neighbour should move

State evidence bullets that cite the researcher reading (source titles) and only
secondarily the drift sample.

#### Proposed charter patch

If Clarify or Realign, show a unified diff (or before/after) limited to the
Charter section — primarily In scope and Boundaries. Keep agent frontmatter,
role preamble, and Procedure stub unless factually wrong.

Proposed wording should:

- prefer the researcher's literature-grounded In scope themes, compressed into
  curator-rubric bullets,
- keep neighbour Boundaries reciprocal where a move touches another domain,
- stay short enough to score fleeting notes against.

#### Impact notes

| Change type                       | Likely impact                                                                                                              |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Narrower In scope                 | Some existing wiki notes may be out of place; some ledgered fleeting notes may have been over-ingested under the old frame |
| Wider In scope                    | Some already-ledgered fleeting notes may deserve a second look; pending backlog may newly qualify                          |
| Boundary move to/from a neighbour | Both domains' charters and bundles may need coordinated follow-up                                                          |
| Clarify only (no ownership move)  | Usually no ledger revisit; curators just score more consistently                                                           |

Name concrete paths when evidence supports it. Prefer "likely revisit" over
certainty.

Ledgers record **reviewed**, not used vs unused (`docs/curation.md`). Do not
invent a reviewed-not-used bit. Reopen candidates come from re-reading sampled
ledgered fleeting notes against the _proposed_ charter, not from ledger
metadata.

#### Re-curation / ledger guidance

Say explicitly whether applying the patch warrants further work:

- **No revisit** — wording clarify only; leave ledgers and notes alone.
- **Selective wiki audit** — list or describe wiki notes to re-read for
  mis-scope. Moving notes across bundles is a human-directed follow-up, not part
  of this skill.
- **Ledger reopen candidates** — if scope widened (or a boundary moved material
  in), list specific ledgered fleeting paths from a small sample that the
  _proposed_ charter would now treat as in-scope enough to re-curate, and that a
  human may want removed from `curation/<domain-slug>.txt` so a later `/curate`
  sees them again. If the sample does not surface any, say so. Do not edit the
  ledger.
- **Neighbour pass** — if a boundary moved, recommend
  `/charter-review <neighbour>` and/or a focused `/curate` after charters are
  updated.
- **Re-ingest warning** — charter realignment can invalidate prior framing;
  large moves may imply re-curating from fleeting sources rather than only
  patching wiki prose.

Never auto-remove ledger lines, never auto-move wiki notes, and never treat the
proposal as applied.

## After human approval

Only when a human explicitly asks to apply an agreed patch:

1. Edit `.claude/agents/<domain-slug>-curator.md` to match the approved Charter
   text (and any approved neighbour charter edits, preferably in the same change
   set).
2. Leave ledgers and wiki notes untouched unless the human also asks for a
   specific audit or reopen list to be carried out.
3. Summarise what was applied vs what remains as follow-up (`/curate`, selective
   note moves, neighbour review).

## Rules

- Rare by design — refuse to invent churn when the verdict is Hold.
- Source-led: researcher full-reads of top-cited fleeting groups are mandatory
  primary evidence; bundle sampling is secondary drift only.
- Proposal only in the review pass: no silent charter edits.
- One domain per invocation; neighbour changes are recommendations or paired
  human-approved edits, not drive-by rewrites.
- Do not start `/curate` or edit wiki notes as part of the review itself.
- Keep lines short in any markdown you write; match existing charter style.
