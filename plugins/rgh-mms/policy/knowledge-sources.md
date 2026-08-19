# External knowledge sources

Trial (started 2026-08-09, contract
[`0034_rgh_sme_knowledge_trial`](../.agent-metrics/contracts/0034_rgh_sme_knowledge_trial.md)):
a read-only mount of
[`xchewtoyx/rgh-sme`](https://github.com/xchewtoyx/rgh-sme) — a private
collection of "SME domain knowledge" [Open Knowledge Format (OKF)](https://github.com/xchewtoyx/okf-core)
bundles, curated from reference texts across 20 subject-matter domains.
Distinct from [`docs/agent-context/`](../docs/agent-context) — this repo's
own OKF bundle: agent-context is **read-write, self-curated, harness-portable**
(agents promote concepts into it); rgh-sme is **read-only, externally
curated, SME reference**. Never promote into or edit rgh-sme; it is a mirror,
not a workspace.

**Source:** domain count, per-domain note counts, and the `okf` CLI's
`--config`/project-root resolution behavior are verified directly against
`xchewtoyx/rgh-sme` (`okf-core.toml`, 2026-08-09) and `xchewtoyx/okf-core`
(`src/okf_core/config.py`, same date) — not restated from either repo's own
prose, which undercounts the domain total by one.

## What rgh-sme is

Each domain is a flat folder of atomic, single-concept Markdown notes with
`title`/`description`/`sources` frontmatter and inline links to related
concepts — no index or hub pages by design, per rgh-sme's own
`docs/wiki-rules.md`: "structure emerges from the link graph." It is built
for search-and-traverse retrieval by the `okf` CLI, not for bulk reading.
Compiling a static digest of any bundle would defeat that design and bloat
context for no benefit — always query on demand for the question at hand.

## Trial scope

Three independent trial tracks, each its own contract, sharing the mount
mechanism below:

| Role | Domains | Work scope | Contract |
|---|---|---|---|
| [`roles/implementor.md`](../roles/implementor.md) | `data-engineering`, `data-visualization`, `observability`, `change-engineering` | telemetry and [contract-first-change](../workflows/contract-first-change.md) work | [0034](../.agent-metrics/contracts/0034_rgh_sme_knowledge_trial.md) |
| [`roles/planner.md`](../roles/planner.md) | `requirements-architecture`, `decision-alignment` | classifying `acceptance_criteria_defects`, wording ambiguous `open_questions` | [0035](../.agent-metrics/contracts/0035_planner_requirements_decision_alignment_trial.md) |
| [`roles/reviewer.md`](../roles/reviewer.md) | `evidence-verification`, `software-design` | verifying self-referential/mutation-kill claims, judging structure/complexity findings | [0036](../.agent-metrics/contracts/0036_reviewer_evidence_software_design_trial.md) |

Contract 0035 exists because of a concrete, repeated failure pattern:
imprecise requirements leading to a suboptimal solution and multiple
review/approve passes before acceptance. `roles/stakeholder.md` targets
this same failure mode more directly but is explicitly gated pending an
H2 backlog decision (`docs/backlog/harness-horizons.yaml`) — this trial
grounds the currently-active `planner` role instead, without crossing that
gate; see contract 0035 Regression Risks for the scope boundary between
the two. Contract 0036 exists to widen the diversity of role coverage
rather than a specific reported failure; `distributed-systems` (for
`reviewer`'s Concurrency/TOCTOU checklist) was considered and deferred —
see contract 0036 Proposed Change.

The remaining 12 domains exist in rgh-sme and are cataloged below but not
yet wired into any role — candidates for further expansion once these
trials show value.

<details>
<summary>Full rgh-sme domain catalog</summary>

| Domain slug | Subject area |
|---|---|
| `dimensional-modelling` | Dimensional modelling |
| `reliability-engineering` | Reliability engineering and service-level management |
| `incident-management` | Incident response, on-call and learning-from-failure |
| `automation-engineering` | Automation and operational software engineering |
| `capacity-performance` | Capacity, performance and efficiency engineering |
| `technical-communication` | Expressing complex material clearly for different readers |
| `operational-handover` | Operational, maintenance and handover documentation |
| `infrastructure-as-code` | Declarative infrastructure design, delivery and governance |
| `ci-cd` | Continuous integration, delivery and deployment pipelines |
| `resilience-engineering` | Safety science, human factors and adaptive capacity |
| `distributed-systems` | Replication, consistency, consensus and distribution design |
| `security-engineering` | Threat modelling and secure-design principles |

</details>

## Mounting

Run [`scripts/mount-knowledge.py`](../scripts/mount-knowledge.py) once,
before the first query in a session. It clones (first run) or syncs a shared
checkout at `~/.agentic/knowledge/rgh-sme`, installing a dedicated `okf` venv
at `~/.agentic/knowledge/.venv` alongside it. On success it prints
`mount_path`, `config_path`, and `okf_bin`.

**Protections** — every run makes the checkout match `origin/main` exactly
(`git fetch` + `git reset --hard` + `git clean -fd`), so any local drift
(an agent's stray edit, a half-built cache) is discarded and the mirror
stays current in one step; a freshness marker skips the network round trip
when the last sync was under 15 minutes ago. `pre-commit` and `pre-push`
hooks are installed into the checkout that unconditionally refuse (exit 1),
so even a wayward `git commit` inside the mount cannot succeed.

**Access**: rgh-sme is private. Local sessions need `gh` pre-authenticated
(`gh auth login`), the same pattern as `access.local.tool: gh` in
[`repos/okf-core.yaml`](../repos/okf-core.yaml). Remote/sandboxed sessions
are not wired up for this trial — local self-host only for now.

**If the mount fails** (no `gh` auth, no network, upstream down): skip
domain-knowledge grounding for that session and proceed. It is a
supplementary input, never a blocker.

## Telemetry (what makes this a trial, not just a feature)

Report actual usage so each trial can be settled on evidence rather than
assumption: each role self-reports `knowledge_source_query_count` (and
`knowledge_source_domains` when nonzero) whenever its own "Domain
knowledge (trial)" section
([`roles/implementor.md`](../roles/implementor.md#domain-knowledge-trial),
[`roles/planner.md`](../roles/planner.md#domain-knowledge-trial),
[`roles/reviewer.md`](../roles/reviewer.md#domain-knowledge-trial))
applied to a dispatch — see
[`instrumentation/loop-telemetry.md`](../instrumentation/loop-telemetry.md#knowledge_source_query_count--knowledge_source_domains-trial).
`0` is a valid, expected report, not an omission. Reportable, never a gate
— no review or approve check is keyed on it. Settle criteria (KEEP /
IMPROVE / ROLLBACK) are in each track's own contract, linked in the table
above.

## Query pattern

Full orientation guide: [`xchewtoyx/rgh-sme` `docs/consuming.md`](https://github.com/xchewtoyx/rgh-sme/blob/main/docs/consuming.md)
— the consumer-side counterpart to rgh-sme's own `docs/wiki-rules.md`
(authoring) and `docs/curation.md` (maintenance). It covers bundle
selection, FTS search syntax and vocabulary-miss retries, scanning via
`list-concepts` (with `--with-graph-counts` for PageRank-ranked seeds),
building a linked context pack with `context --seed`, and the
search-and-follow-links reading discipline (cite `sources:`, never read
`fleeting/`, no committed index). Read it before your first query if the
pattern below isn't enough context.

Query the `okf` CLI directly — no `cd` needed, `--config` resolves bundle
paths relative to the config file's own directory, not the caller's cwd:

```bash
<okf_bin> search "<question>" --bundle <domain-slug> --config <config_path>
<okf_bin> context --seed <concept-id> --bundle <domain-slug> --config <config_path>
```

Use `search` to find a concept, then `context --seed <id>` to pull in
linked concepts around it when the graph neighborhood matters. One or two
targeted calls per grounding question is the expected shape — never bulk-list
or read an entire bundle directory, and never write a compiled summary back
into a product repo.

**Known gap**: `--bundle` takes exactly one domain name per call — there is
no fan-out across multiple bundles in one invocation. Pick from the domain
table above rather than guessing; run `<okf_bin> list-bundles --config
<config_path>` if unsure of an exact slug. `xchewtoyx/okf-core` is
self-hosted by the same org that maintains rgh-sme, so a multi-bundle
fan-out is a plausible upstream feature request if the four-domain trial
shows this gap is actually painful in practice — not filed yet.
