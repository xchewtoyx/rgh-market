# Source watch

Repeatable discovery of **candidate publications** for onboarding — biased
toward stable, vendor-neutral, shared ground rules of a domain's practice — not
arXiv novelty or vendor press-release papers.

Used by `/source-watch`. Writes only to the per-domain watch cache
(`watch/<domain>.jsonl`) and, after a thin Signal B/C pass, to
`docs/suggested-sources.md`. Never onboards, never curates, never edits
`fleeting/` or domain bundles.

## When to run

- Quarterly for research-heavy domains.
- Optionally paired with `/charter-review` on the same domain.
- There is no default focused domain — always pass `--focused <domain-slug>`
  explicitly.

## Ranking signals

Promote candidates that show **cross-source convergence**:

| Signal                             | Meaning                                                               | Collection                                                                                       |
| ---------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **A. Core-learning citation**      | Cited by ≥2 independent onboarded sources (different author groups)   | Snowball from Related Work / survey-style fleeting notes of top-cited cores; diff vs `fleeting/` |
| **B. Citation mass**               | Durable academic attention                                            | OpenAlex / Semantic Scholar; prefer ≥12 months old or survey uptake                              |
| **C. Independent vendor adoption** | Idea appears in a **non-author** product/framework as a named pattern | Docs/OSS harnesses that cite the paper; **exclude** when vendor ≈ author/lab                     |

Promotion rule for the suggested-sources queue: **A ∧ (B ∨ C)**, with A
strongest. Signal A is what the researcher persists; B and C are a thin
supervisor pass over the selected shortlist (manual OK in v1).

## Hard anti-signals

- Single-model SOTA / leaderboard papers with no transferable design claim
- Framework cookbooks (LangChain / LlamaIndex-shaped) — same bias as
  `docs/suggested-sources.md`
- Vendor whitepapers where the vendor is author **and** the only adopter
- Prompt tricks tied to one model family
- Renames of patterns already in the bundle (`okf search` / existing concepts)

## Roles

| Role             | Who                             | Duties                                                                                                |
| ---------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Supervisor       | skill session                   | Path-only seed listing, dispatch researcher, run selection script, thin B/C, update suggested-sources |
| Watch researcher | `source-watch-researcher` agent | Full-read seed fleeting notes; extract not-yet-onboarded citations; append watch-cache lines          |

The supervisor must not read fleeting note bodies. Seed path selection is
`scripts/list-source-watch-seeds.py`. Candidate selection after the researcher
returns is `scripts/select-watch-candidates.py` — deterministic, not supervisor
reasoning.

## Watch cache

Append-only JSONL at `watch/<domain-slug>.jsonl`. One object per candidate
observation (researcher may append multiple lines for the same title from
different seed notes; selection collapses by normalized title):

```json
{
  "title": "Voyager: An Open-Ended Embodied Agent with Large Language Models",
  "authors": "Wang et al.",
  "year": 2023,
  "bundle": "agentic-engineering",
  "citing_core": "ai-engineering",
  "citing_path": "fleeting/ai-engineering/07b-agents.md",
  "charter_fit": 0.85,
  "arxiv_id": "2305.16291",
  "notes": "skill library / curriculum lifelong learning for agents"
}
```

- `citing_core` — fleeting source-slug (or book folder) that cited this work.
- `charter_fit` — `0.0`–`1.0` applicability to the domain In scope / Boundaries.
- Do not invent scores without reading the citing note.

## Selection

```sh
python3 scripts/select-watch-candidates.py <domain-slug> \
  --min-cores 2 --min-charter-fit 0.7 --limit 10
```

1. Load `watch/<domain>.jsonl`.
2. Drop titles that already match an onboarded `fleeting/` source slug/title.
3. Group by normalized title; collect distinct `citing_core` values.
4. Keep groups with `len(cores) >= --min-cores` and max
   `charter_fit >= --min-charter-fit`.
5. Sort by core count desc, then charter_fit desc; print top `--limit`.

## Suggested-sources writeback

For each selected survivor, after a thin B/C pass, append (or refresh) an entry
under a **Research watch candidates** section in `docs/suggested-sources.md`:

- Title / authors / year / optional arXiv id
- Benefits: domain slug
- Signal A: listing citing cores
- Signal B / C: short evidence or `unchecked`
- Onboard priority hint: prefer high A∧C, then high A∧B

Never call `/onboard` from this skill. Human acquires the PDF, then onboard →
curate as usual.

## Non-goals (v1)

- Automated B/C scraping pipelines
- Auto-onboarding or auto-curation
- Multi-domain fan-out beyond the focused slug
