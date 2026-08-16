---
name: charter-review
description: >-
  Propose a rare domain charter realignment from top-cited sources (researcher
  full-reads fleeting notes; no silent edits).
argument-hint: <domain-slug> [--top N]
---

# Charter review (rare)

Propose clearer In scope / Boundaries wording for one domain curator charter,
grounded in a full reading of the bundle's most authoritative onboarded sources.
**Do not apply the patch** unless a human explicitly approves it in a later
turn.

Full procedure: `docs/charter-review.md`. Follow it exactly; do not shorten away
the researcher dispatch, no-silent-edit, or re-curation guidance.

## Domains

Same slugs as `/curate` — get them with `python3 scripts/domains.py`.
Charter path: `.claude/agents/<slug>-curator.md`.

## Arguments

- Exactly one `domain-slug` from `python3 scripts/domains.py`. Reject unknown
  slugs or a missing slug.
- Optional `--top N` (default **5** for the ranking script; researcher still
  receives the top **3** matched sources unless the user asks for a different
  researcher set).

## Procedure

1. Run setup if needed (`sh scripts/run-setup.sh`). Missing `okf` or a failed
   setup is non-fatal for this skill.
2. Read `docs/charter-review.md` in full.
3. Rank citations (frontmatter only — do not open fleeting bodies yet):

   ```sh
   python3 scripts/bundle-cited-sources.py <domain-slug> --top <N>
   ```

4. Choose authoritative source groups per the runbook (default: top 3 with
   fleeting matches; optional one under-cited add). Pass each source's
   `dispatch_paths` from the script (`full-group` or `cited-chapters`).
5. Dispatch the **charter-researcher** read-only (see Harness dispatch). Do not
   skip this step in favour of sampling wiki notes.
6. After the researcher returns: read neighbour charters, do the light bundle
   drift check, draft Boundaries that keep the partition honest.
7. Emit the required report sections:
   - **Verdict** — Hold / Clarify / Realign, with source-grounded bullets
   - **Proposed charter patch** — unified diff or before/after (omit if Hold)
   - **Impact notes** — likely wiki / ledger / neighbour consequences
   - **Re-curation / ledger guidance** — whether revisit is warranted, with
     concrete paths when possible
8. Stop. Do not edit the charter, ledgers, fleeting notes, or wiki bundles. Do
   not dispatch `/curate`. Invite the human to approve, revise, or discard the
   proposal.

## Harness dispatch — charter researcher

Read `agents/charter-researcher.md` and dispatch a **read-only**
subagent with that charter. Prompt:

```text
For <DOMAIN>, fully read every fleeting note in these dispatch_paths for
the authoritative sources: <SOURCE_GROUPS>. Current charter:
.claude/agents/<DOMAIN>-curator.md. Neighbours named in Boundaries:
<NEIGHBOURS>. Return the report sections required by
charter-researcher.md. Do not write to charters, ledgers, fleeting
notes, or wiki bundles.
```

- **Claude Code** — Agent tool, name `charter-researcher`.
- **Antigravity / Gemini** — `define_subagent` / `invoke_subagent` from
  `agents/charter-researcher.md` with write tools disabled.
- **Cursor** — Task tool with `subagent_type: generalPurpose` (or
  `charter-researcher` if that type is registered), instructions from the
  researcher file, and an explicit forbid on charter/wiki/ledger/ fleeting
  writes.

## Applying an approved patch

Only if the user explicitly asks to apply a reviewed proposal (same session or a
follow-up): edit the approved charter file(s) to match, leave ledgers/wikis
alone unless they also request a listed follow-up, and summarise applied vs
remaining work. Still follow `docs/charter-review.md` → After human approval.

## Rules

- Rare workflow — prefer **Hold** when evidence is thin.
- Source-led: researcher full-reads are primary; bundle sampling is secondary
  drift only.
- Review pass is read-only against charters and corpus state.
- Output is a proposal + impact notes, never a silent charter edit.
- One domain per run; neighbour charter edits need explicit approval.
- Do not invent ledger reopen lists. Ledgers have no used/unused flag; only
  propose reopen paths you re-read and that the proposed charter newly
  justifies.
