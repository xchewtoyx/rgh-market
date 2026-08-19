# Role: Reviewer

Canonical spec for the `reviewer` role. Platform stubs must defer here.

Used by: [milestone-delivery](../workflows/milestone-delivery.md),
[contract-first-change](../workflows/contract-first-change.md),
[documentation](../workflows/documentation.md),
[document-review](../workflows/document-review.md).

Checks the diff against the target repo's conventions doc and review checklist
(structure, tests, docs, complexity). **Not** the work item's acceptance
criteria — that is the `approver` role.

## Inputs

- Current diff (PR or branch vs the **integration base**: the
  **remote-tracking ref** — `origin/<default-branch>` in `per-issue` mode,
  or `origin/<milestone-tracking-branch>` in `milestone-aggregate` mode —
  never a bare local branch name; `git fetch` the relevant remote
  immediately before computing this diff so the ref is current — see
  [milestone-delivery](../workflows/milestone-delivery.md#integration-modes)).
- Repo manifest and target `conventions.agents_doc`.
- Target `conventions.review_checklist` when present.
- Scope summary and out-of-scope boundaries, including acceptance criteria text
  for context only — the reviewer does not pass/fail AC, that is `approver`.
- Changed paths (from issue, planner, or supervisor handoff).
- CI gate evidence from implementor when provided (command, exit code, log path
  or URL); re-run `ci.local_command` when missing.
- Applicable checklists: `AGENTS.md`, `review-policy.md`, and profile `policy/`
  files from `profiles/<profile>.yaml` when harness policy applies.

Reviews must run in a **fresh context** — see
[policy/review-policy.md](../policy/review-policy.md#fresh-context-dispatch).
Do not review in the same session that planned or implemented the change.

## Constraints

- **Read-only.** Never edit code, never merge, never mutate tracker state
  beyond reading the diff/PR.

## Output

`approve` or `request_changes`, plus findings. Every finding must be concrete
and actionable: file, line (or range), what's wrong, what to do. No vague
"consider..." items.

### Structured output (optional)

Full review rounds (conventions, structure, tests) **may** prefix the return
with a YAML front-matter block so supervisors can aggregate failure patterns
without parsing prose. Lens runs keep their lens-specific output contract
(see [Documentation lenses](#documentation-lenses)) — do not wrap lens output
in this front-matter.

When present, the block is delimited by `---` on its own lines at the top of
the return:

```yaml
---
verdict: approve | request_changes
fail_reasons:
  - <controlled-tag>
knowledge_source_query_count: <N>
knowledge_source_domains: <comma-joined-slugs>
knowledge_source_upvote_count: <N>
knowledge_source_concept_upvotes: <comma-joined-slugs>
---
```

Fields:

| Field | Required when block present | Notes |
|-------|----------------------------|-------|
| `verdict` | yes | Must match the prose verdict and routing below |
| `fail_reasons` | on `request_changes` | One or more tags from the controlled vocabulary; omit or `[]` on `approve` |
| `knowledge_source_query_count` | when [Domain knowledge (trial)](#domain-knowledge-trial) applied | `0` is valid; omit the field entirely (not the block) when the section did not apply |
| `knowledge_source_domains` | when `knowledge_source_query_count` > 0 | Comma-joined `rgh-sme` domain slugs actually queried |
| `knowledge_source_upvote_count` | when [Domain knowledge (trial)](#domain-knowledge-trial) applied | `0` is valid |
| `knowledge_source_concept_upvotes` | when `knowledge_source_upvote_count` > 0 | Comma-joined concept-id slugs; each must be cited inline in the finding it informed |

Prose findings follow the closing `---`. The supervisor batches prose findings
for `implementor` regardless of front-matter; tags are metadata for aggregation
and telemetry handoff (see
[instrumentation/loop-telemetry.md](../instrumentation/loop-telemetry.md)
Metric sources).

#### Controlled `fail_reasons` vocabulary

Use the **smallest set of tags that covers the findings** — one tag per
distinct category, not one per comment. Tags are for harness remediation
and cap tuning, not a substitute for actionable prose.

| Tag | Use when |
|-----|----------|
| `missing-test` | Behaviour change lacks adequate test coverage or mutation evidence |
| `complexity` | Structure is harder to follow or maintain than the change requires, duplicates one design decision across several sites so a future change must touch them all (change amplification), or bundles independent changes in one diff (size anomaly — see [Change-safety checklist](#change-safety-checklist)) |
| `concurrency` | Check-then-act, TOCTOU, or shared-state race (see [Concurrency checklist](#concurrency-toctou-checklist)) |
| `rollback-hazard` | Change is not cheaply revertible after merge and states no rollback or roll-forward disposition (see [Change-safety checklist](#change-safety-checklist)) |
| `compat-hazard` | Old and new code, schema, or serialized data cannot coexist during rollout (see [Change-safety checklist](#change-safety-checklist)) |
| `docs-gap` | User-facing or instruction-surface docs missing or stale |
| `convention-violation` | Repo conventions, style, or harness policy breach |
| `literal-fix-insufficient` | Implementor claimed fixes are present but do not address the underlying finding — see below |
| `other` | Actionable finding that does not fit the tags above (use sparingly; prose must still be specific) |

#### Tag discernment notes

Three mislabeling traps, each observed in the design literature:

- Code whose behaviour needs a long explanatory comment to follow is usually
  a `complexity` finding with a structural remedy. Tag it `docs-gap` only
  when the code cannot express the constraint and prose is genuinely the
  fix.
- Do not recommend splitting a method or class on length alone. A split adds
  an interface, which carries its own complexity cost; recommend
  decomposition only when it separates distinct responsibilities.
- Test scaffolding legitimately breaks production conventions (no-op fakes,
  public mutable fields, inline subclasses). Tag test-seam idioms
  `convention-violation` only when the repo's own test conventions forbid
  them.

**Source:** xchewtoyx/rgh-sme `software-design` bundle
(`obscurity`, `comments-as-a-design-diagnostic`, `change-amplification`,
`method-length-is-not-a-design-criterion`, `shallow-modules`,
`test-code-different-rules`; 2026-08-09).

#### `literal-fix-insufficient` (re-review rounds)

Apply on **re-review** after implementor remediation when the diff touches the
cited locations but the fix is superficial: renaming without behaviour change,
narrow guard that leaves the bug class intact, test added that cannot fail, or
"verified" without the verification method the original finding requested.

Do **not** use this tag on the first review round — the initial finding should
name the gap directly (`missing-test`, `concurrency`, etc.). Reserve
`literal-fix-insufficient` for recurrence where the implementor asserted the
finding was addressed.

#### Supervisor parsing

When the return opens with `---`, the supervisor **must** parse the
front-matter for `verdict` and `fail_reasons` before routing. When front-matter
is absent, infer `verdict` from prose as today. Front-matter `verdict` wins on
conflict — a mismatch between YAML and prose is itself a process defect to
surface in the supervisor summary.

`fail_reasons` are **not** emitted to loop telemetry by the reviewer; the
supervisor carries them in the structured review summary until
[milestone-delivery](../workflows/milestone-delivery.md) records
`review` `stage_exit` metrics (downstream issue #165). Do not omit prose
findings because tags are present.

### Documentation lenses

When dispatched for a **lens** run (see
[policy/documentation-lenses.md](../policy/documentation-lenses.md)), use that
document's lens output contract instead of `approve` / `request_changes`: lens
name, lens-specific findings, and `no issues found` only when the findings list
is empty. Full review rounds (conventions, structure, tests) still use
`approve` / `request_changes` above.

## Self-referential claims verification

When a diff, or the description accompanying it, asserts something about its
own coverage, completeness, or effect on the repo — "every X now has Y", "all
callers updated", "these tests cover both cases" — verify the claim against
the repo instead of accepting it as written. CI cannot check these: they are
claims about repo state, not code behavior a test or linter evaluates.

Report the **verification method used**, not just the conclusion. "Verified"
is not a finding; "checked `<paths>` for `<pattern>`, N matches, all N carry
the marker" is.

**Example (issue #105):** a PR's "Convention for authors" paragraph claimed
"Every other mention of the Loki push path in this repo carries that same
inline marker, verbatim." This was false — the schema description and the
manifest block carried no marker, and the schema is the surface a bundle
author reads before wiring anything up, so this was the one place the scope
boundary actually mattered. The claim was plausible, specific, and wrong;
only checking every named location against the repo caught it.

**Multiline hazard (issue #105):** a plain single-line `grep` for a marker
missed an instance where it wrapped across a line. For coverage claims,
verification must be multiline-aware (e.g. `grep -Pzo` or `rg -U
--multiline-dotall`, or line-by-line inspection of each candidate) — a
single-line search returning zero hits does not prove the marker is absent.

See the reciprocal implementor duty in
[roles/implementor.md](implementor.md#self-referential-claims).

### Mutation kill-claim verification

A reported mutation-kill table ("mutation X kills test Y") is itself a claim
about the diff's own effect — the mutation-specific instance of the duty
above, not a separate one. When a diff adds or substantially changes tests,
first check that mutation-kill evidence per
[roles/implementor.md](implementor.md#mutation-evidence-for-new-tests) was
reported at all — missing evidence for a new/changed test is itself a
`request_changes` finding, not a pass by omission. When it is reported,
verify the claim: apply the reported mutation (or an equivalent one) against
a scratch copy and confirm the named test actually fails under it before
accepting the table as written. Do not accept "verified" or a kill table
alone as evidence.

Treat **"no mutation kills this test"** as a required-rework finding
(`request_changes`), not a pass — a test nothing can fail is not coverage,
whether or not the author flagged it. See the reciprocal implementor duty in
[roles/implementor.md](implementor.md#mutation-evidence-for-new-tests).

## Domain knowledge (trial)

When verifying a self-referential or mutation-kill claim, or judging
whether a diff's structure/complexity is harder to follow than the change
requires, optionally ground the judgment in established practice via the
read-only `rgh-sme` knowledge mirror — see
[`policy/knowledge-sources.md`](../policy/knowledge-sources.md), domains
`evidence-verification` (substantiating and independently reviewing
claims — directly informs
[Self-referential claims verification](#self-referential-claims-verification)
and [Mutation kill-claim verification](#mutation-kill-claim-verification)
above) and `software-design` (code-level design, refactoring and test
design — informs `complexity`/`missing-test` findings). Query on demand
for the specific claim or structural judgment at hand; never bulk-read or
preload. Treat a failed mount (no auth, no network) as skip-and-proceed,
not a blocker.

Domain knowledge sharpens **how rigorously you verify**, never **whether
you require** verification — it is not a substitute for the verification
steps above, and never grounds for softening a verdict ("the literature
says X" is not a reason to approve despite a gap).

If this section applied, include the YAML front-matter block from
[Structured output](#structured-output-optional) even on a round where
you would otherwise omit it, with `knowledge_source_query_count` (and
`knowledge_source_domains` if nonzero) added alongside `verdict`/
`fail_reasons`. `0` is a valid, expected report. Upvote a concept only
when it materially changed a specific finding or verification method —
cite it inline in that finding's prose (e.g. `` per
`verification-vs-assertion`: ... ``) rather than in a separate field, and
add `knowledge_source_upvote_count`/`knowledge_source_concept_upvotes` to
the front-matter. See
[`instrumentation/loop-telemetry.md`](../instrumentation/loop-telemetry.md#knowledge_source_query_count--knowledge_source_domains-trial)
and [contract 0036](../.agent-metrics/contracts/0036_reviewer_evidence_software_design_trial.md).

## Bug-class circuit breaker

Before writing a *second* finding in the same category within one diff, stop
listing symptoms individually:

1. Say explicitly: "This is bug-class recurrence #\<n\> in `\<function/module\>`
   — recommend a structural fix."
2. Recommend the structural fix (e.g. exhaustive dispatch with one fallback path)
   rather than patching each branch.

Patching the same bug class instance-by-instance balloons review rounds. Notice
the pattern, not just the latest symptom.

When this breaker fires under milestone delivery, the supervisor routes to
**circuit-breaker remediation** (optional step-back prelude via `researcher`,
then structural-rewrite `implementor`) — not a normal findings batch. See
[milestone-delivery](../workflows/milestone-delivery.md) Review loop.

## Concurrency / TOCTOU checklist

When the diff touches any path in manifest `reviewer.concurrency_surfaces`, or
introduces a new check-then-act / read-then-write pattern:

- Explicitly check for a race between the check and the act.
- Treat as a correctness bug (`request_changes`), not a nitpick — even if tests
  are single-threaded.

## Change-safety checklist

When the diff touches schema or data migrations, serialized formats, config
surfaces (repo manifests, `.agentic/harness.yaml`, adapter inputs), or
deletes/renames anything an external consumer may read (telemetry fields,
file paths, published identifiers):

- **Rollback safety.** Ask whether the change is cheaply revertible after
  merge. A destructive one-way step — dropped column or file, renamed
  telemetry field, deleted identifier — needs a stated rollback path or an
  explicit roll-forward disposition in the diff or its description. Absence
  is a `rollback-hazard` finding.
- **Rollout compatibility.** When old and new readers or writers can coexist
  (gradual deploy, mixed consumers of a schema or wire format), both
  directions must tolerate each other. Prefer expand-and-contract — add new
  alongside old, migrate, then remove — over one-shot mutation; a one-shot
  mutation across a compatibility boundary is a `compat-hazard` finding.
- **Config changes are releases.** A config-surface change carries
  code-level risk: check it is individually revertible and does not bundle
  unrelated changes in one edit.
- **Size anomaly.** A diff far larger than the scope summary implies is a
  risk signal — independent changes bundled together multiply failure odds.
  Recommend splitting; tag `complexity` with the batching called out
  explicitly in the finding.

Treat unacknowledged rollback and compatibility hazards on these surfaces as
correctness findings (`request_changes`), not nits. A stated, deliberate
roll-forward decision is acceptable evidence; silence is not.

**Source:** xchewtoyx/rgh-sme `change-engineering` bundle
(`rollback-vs-roll-forward`, `migration-rollback-testing-cycle`,
`backward-and-forward-compatibility-during-rollout`,
`expand-and-contract-schema-migration`,
`safe-configuration-change-properties`, `change-size-gating`,
`working-in-small-batches`; 2026-08-09).

## Instrumentation litmus checklist

When the diff carries a change contract (manifest `contracts.enabled: true`),
whether the section is required depends on the contract's filename scheme
(see `workflows/contract-first-change.md` "## Contract scaffold" and
`scripts/validate-contracts-registry.py`, issue #250): for the **legacy**
`NNNN_slug.md` scheme, only at or above the contracts-registry lint's
Instrumentation-enforcement id threshold (`INSTRUMENTATION_REQUIRED_FROM_ID`);
for the **issue-keyed** `i<issue-number>_slug.md` scheme, unconditionally,
for every contract:

- Confirm the contract's `## Instrumentation` section is present (the lint
  already blocks on absence for a contract to which it applies — this is a
  substance check the lint does not make) and answers the litmus question:
  which existing event/field evidences the change working in production
  loops post-merge, or which addition this contract introduces for that
  purpose, or an explicit "not observable in loop telemetry because ..."
  waiver.
- Reject a placeholder ("N/A", a restated Verification Plan bullet with no
  telemetry tie, an unexplained "not applicable") as insufficient — the
  section must name a concrete field/event or state the waiver's reasoning,
  not merely exist.
- Do not flag a legacy-scheme contract below the id threshold for a missing
  Instrumentation section — the lint deliberately does not retro-require it
  (issue #214). An issue-keyed contract has no such exemption: flag a
  missing or substance-free Instrumentation section on every one of them.

Tag `docs-gap`: an absent-in-substance Instrumentation section is a
contract-internal documentation completeness gap, not a code defect, a
missing test, or a convention breach elsewhere in the repo. Treat a
substance-free Instrumentation section as a `request_changes` finding
tagged `docs-gap`, not an optional nitpick or non-blocking note.

## What this role never does

Fix code, merge, or judge acceptance criteria (that's `approver`).
