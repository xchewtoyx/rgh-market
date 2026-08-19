# Milestone Delivery Loop

Operating spec for the supervisor that drives one delivery container's
open work items (a GitHub milestone or a parent issue) to merged PRs, one
issue at a time, using the four narrow roles in [roles/](../roles/):
`planner`, `implementor`, `reviewer`, `approver` — plus optional
Review-loop **step-back** via fresh `researcher` under circuit-breaker
remediation.

Platform skills (e.g. `skills/milestone-delivery/`) and portal stubs
must defer to this document — it is the single source of truth.

## Prerequisites

- Bundle config resolved via the layered resolver (see
  `repos/README.md` "Resolution order"): `scripts/bundle_registry.py resolve
  --bundle <bundle> --root <target-repo-root>`. Hard cutover (issue #327):
  no fallback to a legacy `repos/<bundle>.yaml` or product
  `.agentic/harness.yaml` when the resolved layers are empty. The resolved
  config's `configured` flag must be `true` — `false` means the bundle
  needs onboarding (see #339) and this loop does not proceed.
- Target repository available as a local clone (fetch-only — the loop never
  checks out a branch or edits files in that clone's own working tree; see
  Loop step 3) or accessible via platform tools.
- Resolved config `delivery.agent_may_force_push` must be `false` (default).
- **Default-branch merge is always a human hard gate** in both integration
  modes. Agents never merge into the default branch.

## Integration modes

Resolved config `delivery.integration_mode` selects how multi-PR milestones land:

| Mode | When to use | Per-issue PR target | Who merges issue PR | Human hard gate |
|------|-------------|---------------------|---------------------|-----------------|
| `per-issue` (default) | Platforms/tools that support reviewing each PR against default (including stacked-PR workflows) | Default branch | Human | Every issue PR → default |
| `milestone-aggregate` | Platforms that **do not** support stacked PRs (typical Bitbucket DC / Azure DevOps; GitHub without a stacking tool) | Milestone tracking branch | Supervisor, after approve, when satisfied (`delivery.agent_may_merge` must be `true`) | Milestone aggregation PR → default (bulk) |

**Recommendation:** set `integration_mode: milestone-aggregate` in the
bundle's committed `.claude/rgh-mms.json` for `ado`/`bitbucket` targets (see
Prerequisites) — `platform-defaults/ado.json` and
`platform-defaults/bitbucket.json` currently ship `per-issue` as their
baseline default, so this override is required, not automatic. Keep
`per-issue` on GitHub unless the team opts in.

`delivery.agent_may_merge` semantics:

- `per-issue`: must be `false`. Humans merge every issue PR.
- `milestone-aggregate`: must be `true`. Supervisor may merge **only** into the
  milestone tracking branch — never into the default branch.

### Integration base (both modes)

**Integration base means the remote-tracking ref, never a bare local branch
name.** For every diff-producing step (branch cut, `changed-paths`/
`files-touched`, review diff, approve diff), "integration base" resolves to
`origin/<default-branch>` in `per-issue` mode or `origin/<milestone-tracking-branch>`
in `milestone-aggregate` mode — the supervisor must `git fetch` the relevant
remote immediately before that step so the ref is current. This removes the
staleness class where a local branch's stored tip lags behind a sibling
issue's mid-run merge (issue #243); see Loop step 3 and Loop steps 5–7 for
the same wording applied at each diff-producing point. This definition
applies in both `per-issue` and `milestone-aggregate` modes; the
aggregate-only tracking-branch mechanics follow in the next section.

### Milestone tracking branch (aggregate mode)

At the start of a milestone-aggregate run (before the first issue PR):

1. Resolve `delivery.milestone_branch_pattern` (default
   `milestone/{milestone}`). Tokens: `{milestone}` (slugified milestone name or
   number), `{bundle}`, `{parent}` (parent issue number when the run uses the
   parent-issue container). On a parent-issue run, if the resolved pattern
   still contains `{milestone}` or lacks `{parent}`, stop and ask — do not
   emit an empty token.
2. Create the tracking branch from the latest default branch if it does not
   exist; otherwise fast-forward it to default only when it has no unique
   commits yet. Never force-push; never rewrite history that already contains
   merged issue work. Same Isolation rule as Loop step 3: do this via the
   platform API or a direct remote-ref push/fast-forward (or, if a local ref
   is unavoidable, a scratch `git worktree`) — never by checking out the
   tracking branch inside the shared local clone's own working tree.
3. Open or refresh a **milestone aggregation PR**: tracking branch → default
   branch. Title/body identify the container (milestone path: milestone title;
   parent-issue path: `owner/repo#parent`) and list landed issue PRs as they
   merge. Keep this PR open and **ready for review** for the whole run (same
   draft exceptions as [Open PR](#loop-one-issue-end-to-end) step 8) — it is
   the human review surface for the bulk land.
4. Record the tracking branch name and aggregation PR URL in the supervisor's
   short progress state (not full diffs).

Issue branches cut from the **current tip of `origin/<milestone-tracking-branch>`**
(fetch immediately before cutting), not from default. Issue PRs target the
tracking branch. Reviewer and approver diffs are against
`origin/<milestone-tracking-branch>` (the integration base).

## Input

A **bundle** id and one of:

- a **milestone** identifier (name or number) — default path; or
- a **parent issue number** (local tracker) — parent-issue container
  (issue #262 Phase 2); or
- an **origin ticket** on an operator-supplied `owner/repo` (destination
  `repos/<bundle>.yaml`) — follow [Local-mirror flow](#local-mirror-flow)
  once at run start, then continue with the new local parent number.

Resolve the bundle config via the layered resolver first (see
Prerequisites). **Never hard-code or cache a worklist.** Every
iteration re-queries the tracker for currently-open work items.

If none of the three is present, or the supplied identifier does not
resolve, stop and ask — do not guess, fall back to a label list, or assume
from a previous run. If both a milestone identifier and a parent issue
number are supplied, ask which container this run uses — do not silently
prefer one. Do not switch a parent-issue run onto `milestone_query`, or a
milestone run onto sub-issues, without an explicit human instruction.

**Tooling note (GitHub, milestone path):** generic issue listing can omit
`milestone`. Confirm with a milestone-scoped search (resolved config
`delivery.milestone_query`) before concluding a milestone is empty.

**Tooling note (GitHub, parent-issue path):** enumerate via the parent
endpoint — `GET /repos/{owner}/{repo}/issues/{parent}/sub_issues` (resolved
config `delivery.parent_issue_query` when set; token `{parent}`). Sub-issues are
not reachable via `gh search issues` qualifiers (`gh search issues --help`
has no `--parent` flag). Recurse into each child's `sub_issues` when
stories have nested tasks. See
[Parent-issue container](#parent-issue-container).

## Parent-issue container

Additive beside the milestone path. The milestone path remains the default
when the operator gives a milestone identifier and no parent issue number.

| Concern | Parent-issue path | Milestone path (unchanged) |
|---------|-------------------|----------------------------|
| Start | `bundle` + parent issue number | `bundle` + milestone name/number |
| Worklist | Parent-keyed sub-issues (REST above); filter to open | `delivery.milestone_query` |
| Completion | All sub-issues closed (no open descendant after a recursive walk) | Zero open issues on the milestone |
| Telemetry `--milestone` | Repo-qualified ref `{owner}/{repo}#{parent}` (e.g. `xchewtoyx/rgh-mms#310`) | Tracker milestone **title** |
| Branch tokens | `{parent}` required on `milestone_branch_pattern` (stop and ask if the resolved pattern still contains `{milestone}` or lacks `{parent}`); `{parent}` available on `branch_pattern` | `{milestone}`, `{bundle}` as today |

`--milestone` stays required (issue #51). The field is an activity-scoped
correlation id — see
[instrumentation/loop-telemetry.md](../instrumentation/loop-telemetry.md).
`delivery.integration_mode` and `delivery.agent_may_merge` gating do not
change.

## Local-mirror flow

Use when the requested delivery unit is a ticket on an operator-supplied
origin `owner/repo` (the destination product identified by
`repos/<bundle>.yaml`), and the breakdown must stay on this tracker
(`rgh-mms`).

**Zero-change adoption:** never write the local breakdown into the origin
repo's docs, `AGENTS.md`, or other committed product files. The origin
ticket is an interface: read once at start, write once at end.

1. **Create Feature parent (supervisor).** Open a local issue on this
   tracker (`rgh-mms`) with label `type:feature`. Body references the origin
   ticket (URL + title + tracker id) and states that sub-issues here are the
   delivery worklist. Record the new parent number. Do not file that
   structure on the origin `owner/repo`.
2. **Populate sub-issues (planner).** Dispatch `planner` with the origin
   ticket and the new parent number for
   [local-mirror populate](../roles/planner.md#local-mirror-populate). The
   planner creates `type:story` / `type:task` sub-issues under the parent
   (via `gh api -X POST /repos/{owner}/{repo}/issues/{parent}/sub_issues`
   with `sub_issue_id` — same path as
   `scripts/file-github-backlog.py::GitHubClient.add_sub_issue`) and returns
   their numbers. This is a tracker write, not a git write.
3. **Deliver (supervisor).** Deliver against the local parent using
   [Parent-issue container](#parent-issue-container).
4. **Close the origin (end).** When all local sub-issues are closed, post a
   summary comment on the origin ticket (landed PRs / outcome) and close the
   origin ticket. Do not copy the local issue tree into the origin
   `owner/repo`.

## Thinness constraint

The supervisor dispatches roles and reads only their short structured summaries.
It never reads a full diff, full issue thread, or full PR review comment
directly — dispatch `planner`/`reviewer`/`approver`, or optional Review-loop
step-back `researcher`, instead.

## Supervisor context discipline

Every task-level phase — **plan**, **implement**, **review**, and **approve** —
plus optional Review-loop **step-back** `researcher` under circuit-breaker
remediation — must be dispatched to a **fresh subagent** (or a **fresh
session** when the client lacks subagents — see `clients/compatibility.yaml`),
not run inline in the supervisor transcript.

A skill file under `skills/` is insufficient if the supervisor reads full role
outputs, file dumps, or diffs inline. The dispatch boundary is what keeps the
supervisor thin.

**Failure mode:** when planning and implementation run inline and only review is
dispatched, supervisor context grows without bound.

**Source:** `ansible-review-robot/docs/harness/delivery-loops.md` (Supervisor
Context Discipline) — Increment 1 reached ~540K tokens when only review was
dispatched. Fresh dispatch per phase prevents context exhaustion and review
bias.

| Phase | Dispatch | Supervisor reads |
|-------|----------|------------------|
| Plan | Fresh `planner` | Structured plan fields only |
| Implement | Fresh `implementor` | Branch, SHA, worktree path, summary, `ci_evidence`, changed paths (`git diff --name-only`) |
| Review | Fresh `reviewer` | Verdict + findings summary |
| Step-back (optional) | Fresh `researcher` | `summary` / `recommendation` only |
| Approve | Fresh `approver` | Per-criterion pass/fail table |

See also [fresh-context dispatch](../policy/review-policy.md#fresh-context-dispatch)
for review-specific rules.

## Per-issue state

Track and surface on every progress report:

- issue number and title
- current stage (plan / implement / review / approve / pr-open /
  awaiting-merge / merged-to-milestone)
- review round count / cap (e.g. `review 3/5`)
- approve round count / cap (e.g. `approve 1/5`)
- `correlation_id` for loop telemetry (minted by `run_start` when
  `--correlation-id` is omitted; see `scripts/record-loop-event.py`)
- in aggregate mode: tracking branch name and aggregation PR reference

Report format: `#N <title> — stage: review, round 3/5`.

Loop telemetry is **required** — see [Loop telemetry](#loop-telemetry-required)
below and `skills/milestone-delivery/SKILL.md` **Telemetry emission**. A
missing event or a rejected `record-loop-event.py` call (exit non-zero) is a
loop defect: fix the emission and retry before continuing. Field requirements
and metric names: [instrumentation/loop-telemetry.md](../instrumentation/loop-telemetry.md).

## Loop (one issue, end to end)

0. **Run setup (once per run, before the first issue).** Two
   sub-steps, run in order; neither gets a dedicated `stage_enter`/
   `stage_exit` telemetry pair (see **Telemetry treatment** below).
   On a parent-issue run that still needs a local Feature parent, complete
   [Local-mirror flow](#local-mirror-flow) steps 1–2 before 0a (the
   worklist to reconcile is the local sub-issues).
   - **0a. Backlog reconciliation (both integration modes).** Before
     selecting the container's first issue, reconcile its open work items
     against current repo state — backlogs are filed once from YAML and rot
     silently as other work lands (issue #136).
     - **Mechanical checks** — run `scripts/reconcile-backlog.py` against
       each open issue's body text (export via the tracker, one file or
       stdin stream per issue): identifier freshness (a cited contract
       number/filename already taken by a different slug — the #104/`0017`
       case) and cited-path existence (a `path:line` reference where `path`
       no longer exists).
     - **Judgment check (non-blocking, optional)** — for an issue that looks
       already satisfied (e.g. the referenced doc section or file already
       exists), the supervisor **may** dispatch a fresh read-only
       `researcher` to confirm before delivering it; skip when time-boxed.
       This is report-only — it flags a candidate for human closure; it
       never blocks delivery on its own.
     - **Blocking vs. non-blocking split** (`scripts/reconcile-backlog.py`
       and issue #136 use a different, shorter synonym for the non-blocking
       tier — same meaning, worded as "non-blocking" in this file only,
       because a static test guard in `tests/test_record_loop_event.py`
       (issue #51) bans that other, shorter word specifically in this
       file, to keep telemetry emission itself from ever being described as
       optional; see
       `.agent-metrics/contracts/0022_backlog_reconciliation_step.md` for
       full rationale) — identifier collision and missing cited path are
       **blocking** — message the human per [Escalation](#escalation) and
       pause the affected issue before cutting its branch, the same
       response as a hard blocker (conceptually reusing the
       `dependency_blocker` handling from Loop step 4 — no new
       `escalation_reason` enum value — but see Escalation for why this one
       stays an unlogged human message, not a telemetry `escalation`
       event). Line-number drift, an ambiguous bare-filename path citation
       (`ambiguous_path` — matches more than one file under repo root), and
       "AC already satisfied" are **non-blocking** — report to the human
       and continue; they do not stop the container.
   - **0b. Tracking branch and aggregation PR (aggregate mode only).**
     Ensure tracking branch and aggregation PR exist per
     [Milestone tracking branch](#milestone-tracking-branch-aggregate-mode).
   - **Telemetry treatment** — neither sub-step has per-issue context yet —
     0a runs before any issue is selected, and 0b sets up shared
     infrastructure for the whole run.
     `scripts/record-loop-event.py::_validate_milestone_delivery` requires a
     non-null `--issue` for every milestone-delivery event type, including
     `escalation` — a milestone-level check cannot satisfy that without
     misattributing the finding to an arbitrary issue number. This is why
     0b (aggregate-mode tracking-branch setup) has never had a dedicated
     `stage_enter`/`stage_exit` pair, and 0a (reconciliation) follows the
     same precedent rather than adding a new `stage` enum value. Findings
     **may** be folded into `run_start`'s `--metric` fields for
     the container's first issue (e.g. `--metric
     reconciliation_blocking_count=<N>`, `--metric
     reconciliation_nonblocking_count=<N>`) since `metrics` is an open
     `additionalProperties` bag; this is not required.
1. **Query.** Re-fetch open work items for the container: milestone path uses
   the resolved config `delivery.milestone_query` template; parent-issue path uses
   the parent-keyed sub-issue list
   ([Parent-issue container](#parent-issue-container)). If none remain, go to
   [Milestone complete](#milestone-complete).
2. **Select.** Pick exactly one issue (lowest number or tracker default). Work
   end-to-end before touching another. Emit `run_start` with `--issue` and
   `--milestone` set to the activity-scoped correlation id: tracker
   milestone **title** on the milestone path, or `{owner}/{repo}#{parent}`
   on the parent-issue path (never a branch name).
3. **Branch.** Fresh branch per resolved config `delivery.branch_pattern`, cut from
   the **integration base** — the **remote-tracking ref**:
   `origin/<default-branch>` in `per-issue` mode, or
   `origin/<milestone-tracking-branch>` in `milestone-aggregate` mode — never
   a bare local branch name. `git fetch` the relevant remote immediately
   before cutting so that ref is current; a stale local `main` (unfetched
   since a sibling issue merged mid-run) is the exact failure mode this
   wording closes (issue #243).
   - **Isolation (mandatory, no exceptions).** Cut the branch into a fresh
     `git worktree` — `git worktree add <path> <integration-base-ref>` —
     never by checking out the issue branch inside the shared local clone's
     own working tree. "Shared local clone" means any clone another session,
     agent, or the human operator may rely on staying on its default branch
     (e.g. a product repo's single checkout under the operator's normal
     working directory) — that clone is read/fetch-only for this loop: fetch
     into it, then create the worktree from the fetched ref; never
     `git checkout` a different branch there, never edit its files directly.
     Remove the worktree (`git worktree remove <path>`) once the issue
     reaches a terminal state (merged, closed, or abandoned) — see Loop
     step 10.
   - Never reuse a branch or worktree across issues. Never force-push.
   - **Work-item state (best-effort).** When resolved config
     `delivery.work_item_states.in_progress` is set, run
     `scripts/transition-work-item-state.py --bundle <bundle> --work-item
     <issue> --transition in_progress` so the tracker board reflects that
     work has started (e.g. ADO `New` → `Active`) instead of staying frozen
     on its initial state for the whole loop. A non-zero exit is a warning,
     not a loop defect — log it and continue; do not pause the issue or
     escalate over it. Bundles that leave `work_item_states` unset (most
     GitHub bundles) get a no-op here — see
     [Loop telemetry](#loop-telemetry-required) for the (mandatory, separate)
     telemetry emission this does not replace.
4. **Plan.** Emit `stage_enter --stage plan`. Dispatch `planner` in a fresh
   subagent or session. On completion emit `stage_exit --stage plan` with
   `--metric open_questions_count=<N>` (length of planner `open_questions`),
   `--metric verdict=pass` (or `escalate` when escalating below), and
   `--files-touched <path> <path> ...` from the planner's own
   `files_touched` return value (required — see
   [loop-telemetry.md](../instrumentation/loop-telemetry.md#files_touched--changed_paths--scope_divergence-issue-167)).
   When the planner's Output includes `knowledge_source_query_count`
   (trial, contract 0035 — [Domain knowledge (trial)](../roles/planner.md#domain-knowledge-trial)
   applied to this dispatch), pass it through as the same `stage_exit`'s
   `--metric knowledge_source_query_count=<N>` and, if nonzero, `--metric
   knowledge_source_domains=<comma-joined-slugs>`. Likewise pass through
   `--metric knowledge_source_upvote_count=<N>` and, if nonzero, `--metric
   knowledge_source_concept_upvotes=<comma-joined-slugs>` when present.
   Omit whichever the planner's Output omits. (`knowledge_source_notes` is
   not persisted to telemetry — supervisor-context only, per contract
   0035.)
   Non-empty
   `blockers` **or** non-empty `acceptance_criteria_defects` (planner-flagged
   stale, unsatisfiable-as-literal, or scope-conflated acceptance criteria —
   see [planner](../roles/planner.md) Output) → escalate to human, skip implement,
   pause this issue this iteration (same `dependency_blocker` routing for
   both). Emit `escalation` with `--escalation-reason dependency_blocker`
   (reuse for plan-time AC escalate — no new enum) **unless** the human's
   response redirects the goal rather than confirming a blocker or fixable
   AC defect, in which case use `scope_misalignment` instead — see
   [Escalation](#escalation) tagging obligation. Then `run_end` with
   `--terminal-state paused` per [Escalation](#escalation). Do **not** treat
   `open_questions` as this escalate path — open questions alone do not
   trigger step 4 escalate.
5. **Implement.** Emit `stage_enter --stage implement`. Dispatch `implementor`
   in a fresh subagent or session with subtasks. On completion emit
   `stage_exit --stage implement` with `--metric verdict=pass` and
   `--changed-paths <path> <path> ...` from `git diff --name-only` against
   the integration base for the active mode — the **remote-tracking ref**
   (`origin/<default-branch>` in `per-issue` mode, or
   `origin/<milestone-tracking-branch>` in `milestone-aggregate` mode; `git
   fetch` immediately before this diff so the ref is current) — the same
   base the reviewer's diff uses in step 6 — (required; recorder derives
   `scope_divergence`
   from this against the plan's `files_touched` automatically — see
   [loop-telemetry.md](../instrumentation/loop-telemetry.md#files_touched--changed_paths--scope_divergence-issue-167)).
   When the implementor's Output includes `knowledge_source_query_count`
   (trial, contract 0034 — [Domain knowledge (trial)](../roles/implementor.md#domain-knowledge-trial)
   applied to this dispatch), pass it through as the same `stage_exit`'s
   `--metric knowledge_source_query_count=<N>` and, if nonzero, `--metric
   knowledge_source_domains=<comma-joined-slugs>`. Likewise pass through
   `--metric knowledge_source_upvote_count=<N>` and, if nonzero, `--metric
   knowledge_source_concept_upvotes=<comma-joined-slugs>` when present.
   Omit whichever the implementor's Output omits.
6. **Review loop** (cap: 5 rounds):
   - Each round: emit `stage_enter --stage review` before reviewer dispatch;
     on completion emit `stage_exit --stage review` with `--metric
     review_round=<N>`, `--metric verdict=<approve|request_changes>`, and
     `--metric findings_count=<N>`, `--metric batched_findings=<N>` (0 when no
     findings batch this round), and one `--metric category_<tag>=<count>` per
     `fail_reasons` tag present (sum must equal `findings_count`; omit all
     `category_*` when `findings_count` is 0 — see
     [loop-telemetry](../instrumentation/loop-telemetry.md#findings_by_category-wire-shape))
     (and `--metric bug_class_recurrence=0|1`
     when the circuit breaker fires). When the reviewer return includes YAML
     front-matter (see [reviewer structured
     output](../roles/reviewer.md#structured-output-optional)), parse
     `verdict` and `fail_reasons` per [Supervisor
     parsing](../roles/reviewer.md#supervisor-parsing) before routing; carry
     `fail_reasons` in the structured review summary for telemetry handoff
     (#165). When the same front-matter includes
     `knowledge_source_query_count` (trial, contract 0036 —
     [Domain knowledge (trial)](../roles/reviewer.md#domain-knowledge-trial)
     applied to this round), pass it through as this `stage_exit`'s
     `--metric knowledge_source_query_count=<N>` and, if nonzero, `--metric
     knowledge_source_domains=<comma-joined-slugs>`. Likewise pass through
     `--metric knowledge_source_upvote_count=<N>` and, if nonzero, `--metric
     knowledge_source_concept_upvotes=<comma-joined-slugs>` when present.
     Omit whichever the front-matter omits.
   - Diff base is the integration base for the active mode — the
     **remote-tracking ref** (`origin/<default-branch>` in `per-issue` mode,
     or `origin/<milestone-tracking-branch>` in `milestone-aggregate` mode).
     `git fetch` the relevant remote immediately before the diff — matching
     step 5's diff base exactly.
   - Pass implementor `ci_evidence` and scope summary to each reviewer /
     lens dispatch.
   - **6a. Document-review lenses** (conditional): when instruction surfaces
     change (per `documentation-lenses.md` triggers), **complete**
     [document-review](document-review.md) — all lenses pass with
     `ready: true`, or escalate — **before** 6b. Starting lens dispatches
     is not enough; 6b waits on document-review completion.
   - **6b. Conventions / structure / tests** (unconditional): dispatch
     `reviewer` in a **fresh subagent or session** per round — never inline
     in the supervisor transcript
     ([fresh-context dispatch](../policy/review-policy.md#fresh-context-dispatch)).
   - A human PR comment during this loop that redirects the goal (not an
     implementation-level fix request) is a `scope_misalignment` escalation,
     separate from normal verdict routing below — see
     [Escalation](#escalation) tagging obligation.
   - Verdict routing after 6b (condition → action):
     - `approve` → approve loop.
     - `request_changes` without circuit-breaker fire → batch findings;
       dispatch `implementor` once (normal findings batch; see
       [Batching](#batching)).
     - Circuit-breaker fire ("recurrence #2") → **circuit-breaker
       remediation** (not a findings batch), in order:
       1. Optional **step-back** prelude: on first fire the supervisor
          **may** dispatch a fresh read-only `researcher` for mid-review
          structural diagnosis when the recommended structural fix is
          unclear or spans modules; otherwise skip to structural-rewrite.
          Escalate before structural-rewrite when `researcher`
          `recommendation` is `"insufficient evidence"`.
       2. Dispatch `implementor` for an explicitly labeled
          **structural-rewrite**, carrying the recurring bug-class and the
          recommended structural fix (see
          [bug-class circuit breaker](../roles/reviewer.md#bug-class-circuit-breaker)).
     - Escalate before cap when: structural-rewrite remediation fails
       (implementor cannot complete the labeled rewrite, or
       `ci.local_command` exits non-zero after the rewrite attempt); the
       same bug class recurs after remediation (post-rewrite breaker fire);
       or same bug category in the same module continues across rounds
       after a remediation attempt. Do not escalate on first fire alone —
       use remediation (with optional step-back) first.
   - Cap exhausted → escalate with round summaries, pause issue.
7. **Approve loop** (cap: 5 rounds): each round emit `stage_enter --stage
   approve` before dispatch; on completion emit `stage_exit --stage approve`
   with `--metric approve_round=<N>` and `--metric
   verdict=<approve|fail|request_changes>`. Dispatch fresh `approver`
   (subagent or session) each round; same mechanics; failures back to
   `implementor` as one batch. Diff base is the integration base — the
   **remote-tracking ref**. `git fetch` the relevant remote immediately
   before the diff, same as steps 5 and 6. When this issue resumed after
   Loop step 4 plan-time AC escalate, pass the optional **plan-time AC
   adjudication brief** (waived defect ids matching planner
   `acceptance_criteria_defects[].id`, and/or rewrite notes) as Approver
   Input — see [Escalation](#escalation) and
   [approver](../roles/approver.md).
8. **Open PR.** Emit `stage_enter --stage pr_open` before opening the PR; emit
   `stage_exit --stage pr_open` after the PR is open. Title from issue; body
   includes resolved config `pr_body_closes`;
   use target repo PR template if present.
   - `per-issue`: PR targets the default branch.
   - `milestone-aggregate`: PR targets the milestone tracking branch.
   - After approve, open the issue PR **ready for review** (not as a draft).
     Before `stage_enter --stage pr_open`, apply any cheap in-PR fixes named in
     the reviewer summary when verdict was `approve` — see
     [`docs/agent-context/non-blocking-reviewer-note.md`](../docs/agent-context/non-blocking-reviewer-note.md)
     and Handoff readback **approve → PR open** below.
     Do **not** leave it draft waiting for a human to mark it ready.
     Leave draft only when a human explicitly instructs draft, or
     `.agentic/local-policy.md` / product `AGENTS.md` requires draft.
     Ready-for-review is not merge authority: the human hard gate is
     default-branch land only (see Land) — `per-issue`: this PR → default;
     `milestone-aggregate`: aggregation PR → default (supervisor may merge
     issue PRs into the tracking branch).
9. **Land the issue PR:** Emit `stage_enter --stage awaiting_merge` when
   waiting begins.
   - **`per-issue`:** **Wait for human merge — hard gate.** No auto-merge.
     Prefer event-driven PR subscription; if polling, exponential backoff
     (e.g. 1 min → 30 min cap). The PR must already be ready for review
     (step 8); do not treat “still draft” as the human gate.
   - **`milestone-aggregate`:** When the supervisor is satisfied (review and
     approve passed, CI green on the issue PR), **merge the issue PR into the
     milestone tracking branch**. Update the aggregation PR description with
     the landed issue. Do **not** wait for a human at this step. Do **not**
     merge to the default branch. Aggregation PR → default stays the human
     bulk gate; keep that PR ready for review for the whole run (same draft
     exceptions as step 8; see
     [Milestone tracking branch](#milestone-tracking-branch-aggregate-mode)
     §3).
10. **On merge or close.** Emit `stage_exit --stage awaiting_merge`.
    - **Work-item state (best-effort).** On `merged` — the issue PR has
      landed in the default branch (`per-issue` mode) / milestone tracking
      branch (`milestone-aggregate` mode) — when
      resolved config `delivery.work_item_states.done` is set, run
      `scripts/transition-work-item-state.py --bundle <bundle> --work-item
      <issue> --transition done` (e.g. ADO `Active` → `Resolved`). Same
      best-effort handling as step 3: a non-zero exit is a warning, log and
      continue. Skip this call on `closed` (issue closed without merging —
      nothing was accepted). In `milestone-aggregate` mode this call happens
      once per issue PR landing in the tracking branch; it does not wait for
      the aggregation PR's final human-gated merge to the default branch
      (see [Milestone complete](#milestone-complete)).
    - Remove the issue's worktree (`git worktree remove <path>`, using the
      worktree path the implementor returned per
      [roles/implementor.md](../roles/implementor.md#output) Output) per
      Loop step 3 Isolation — the shared local clone was never checked out
      to the issue branch, so no branch switch is needed there. Discard
      working detail for this issue. Record `run_end` via
      `scripts/record-loop-event.py --terminal-state merged` or
      `--terminal-state closed` with `--metric total_review_rounds=<N>` and
      `--metric total_approve_rounds=<N>` (`total_duration_seconds` and
      `human_wait_seconds` are derived by the recorder — see
      [instrumentation/loop-telemetry.md](../instrumentation/loop-telemetry.md)).
    - **Persist telemetry (best-effort).** Immediately after `run_end`, run
      `scripts/persist-telemetry-branch.py` so this issue's recorded events
      move off the local, gitignored `.agent-metrics/loop-events.jsonl` onto
      the durable `telemetry` branch without depending on a human remembering
      to invoke it — this is a mandatory Loop step, not optional tooling.
      Same best-effort handling as the work-item-state calls above: a
      non-zero exit is a warning, not a loop defect — log it and continue; do
      not pause the issue or escalate over it. Safe to call at any issue's
      `run_end` regardless of whether other issues are still in flight in the
      same session — it retains, not truncates, the local lines of any
      `correlation_id` that isn't terminal yet (issue #242), so it never
      breaks a concurrently open issue's later `stage_exit`/`run_end` calls.
      See [instrumentation/loop-telemetry.md](../instrumentation/loop-telemetry.md)
      Persistence for what the script does and its own (unchanged)
      fail-loudly behavior when run directly.
    - Return to step 1 and re-query from scratch.

## Loop telemetry (required)

Every per-issue loop step above that names an emit action is **mandatory**.
`scripts/record-loop-event.py` validates records against
`schemas/loop-telemetry-v1.schema.json` and rejects incomplete
milestone-delivery payloads (exit 1, nothing appended). Each successfully
recorded event also pushes write-through to Grafana Cloud Loki immediately
(issue #108): a push failure warns to stderr and never fails the recording
call or changes its exit code. `scripts/publish-telemetry.py` remains the
batch/catch-up path — for backfilling a session run with the push disabled
(`--no-push` or `telemetry.grafana_cloud.loki.push_enabled: false`), or a
bundle with no Loki configuration at all — and still owns the Mimir rollup
gauges.

| When | Event | Required context |
|------|-------|------------------|
| After Select (step 2) | `run_start` | `--issue`, `--milestone` (activity-scoped correlation id: tracker title or `owner/repo#N`) |
| Before each phase | `stage_enter` | `--correlation-id`, `--stage`, `--issue`, `--milestone` |
| After each phase | `stage_exit` | `--correlation-id`, `--stage`, `--issue`, `--milestone`, required metrics per stage (see instrumentation doc) |
| On abandoning a stage | `stage_abort` | `--correlation-id`, `--stage`, `--abort-reason`, `--issue`, `--milestone` |
| On escalation | `escalation` | `--correlation-id`, `--escalation-reason`, `--issue`, `--milestone` |
| On terminal | `run_end` | `--correlation-id`, `--issue`, `--milestone`, `--terminal-state`, `--metric total_review_rounds=<N>`, `--metric total_approve_rounds=<N>` |

When pairing evidence is available, `duration_seconds` on `stage_exit` is
derived by `scripts/record-loop-event.py` from the matching local or
already-available telemetry-branch `stage_enter` timestamp when the caller
does not supply `metrics.duration_seconds` — do not estimate. If no pairing
evidence is available, the recorder accepts the exit with the optional
top-level `unpaired: true` marker and omits only the derived duration; a
caller-supplied `metrics.duration_seconds` is preserved and included in
`total_duration_seconds`. The recorder never fabricates a duration.
`milestone` is an activity-scoped correlation id: the GitHub milestone
title from the tracker query on the milestone path, or `{owner}/{repo}#{parent}`
on the parent-issue path — never a branch name.

## Handoff readback

At the transitions in the table below, the supervisor states a one-line
readback of what the prior phase produced before dispatching the next phase.
This is **confirm-and-proceed, not a negotiation gate**: state it and move on
unless a role's output or a human message signals a blocker. For
**plan → implement**, proceed only when `blockers` is empty **and**
`acceptance_criteria_defects` is empty; otherwise escalate per Loop step 4
and skip implement.

The readback restates what the supervisor already holds from the prior role's
return (see [roles/](../roles/)) — it requires no role to emit a new output
field. It is narration only: it never determines whether a gate fires. Gate
triggers stay where they are defined — Loop step 4 (non-empty `blockers` /
`acceptance_criteria_defects` before implement); `policy/documentation-lenses.md`
for lens triggers, enforced by `roles/implementor.md` step 6 (`prompt-engineer`
Pre-PR) and Loop step 6a (complete document-review) / 6b (conventions review),
which evaluate the actual branch diff.

Sources are what the supervisor already reads per
[Supervisor context discipline](#supervisor-context-discipline), plus the
branch's changed-path list against the **integration base** — the
**remote-tracking ref** (`origin/<default-branch>` in `per-issue` mode, or
`origin/<milestone-tracking-branch>` in `milestone-aggregate` mode).
`git fetch` the relevant remote immediately before the diff.

| Transition | Readback | Source |
|------------|----------|--------|
| plan → implement | `ordered_subtasks` count, `blockers`, `acceptance_criteria_defects`, `contract_required` | `planner` return |
| implement → review | changed paths, instruction-surfaces flag, gates run, `ci_evidence` | `implementor` return, plus `git diff --name-only` against the remote-tracking integration base |
| plan → implement (recorded) | `files_touched` (issue #167) — this is not just narrated in the readback above, it is **persisted**: Loop step 4's `stage_exit --files-touched` records the planner's prediction to telemetry, not only held in supervisor context for the readback | `planner` return, emitted via `record-loop-event.py` |
| implement → review (recorded) | `changed_paths` (issue #167) — the same changed-path list this readback already narrates above is **also persisted**: Loop step 5's `stage_exit --changed-paths` records it to telemetry, so `scope_divergence` against the plan's `files_touched` can be derived (see [loop-telemetry.md](../instrumentation/loop-telemetry.md#files_touched--changed_paths--scope_divergence-issue-167)) | same `git diff --name-only` against the remote-tracking integration base as the row above, emitted via `record-loop-event.py` |
| review → implement (findings) | `request_changes` verdict, finding count, `fail_reasons` when front-matter present | `reviewer` return |
| review → implement (breaker remediation) | circuit-breaker fire, bug-class, structural-rewrite label | supervisor brief to `implementor` (fire + class from `reviewer` return; structural-rewrite label assigned by supervisor — not a reviewer Output field) |
| review → step-back | circuit-breaker fire, step-back role (`researcher`) | supervisor (from `reviewer` fire) |
| step-back → implement (structural-rewrite) | researcher `summary` / `recommendation`, supervisor-held structural-rewrite label from breaker | `researcher` return + supervisor brief |
| review → approve | `approve` verdict | `reviewer` return |
| approve → implement | failed-criteria count, failed-criteria names | `approver` per-criterion table |
| approve → PR open | all-criteria-pass confirmation; actionable non-blocking reviewer notes applied or explicitly deferred | `approver` per-criterion table; reviewer summary for cheap in-PR alignments per [`docs/agent-context/non-blocking-reviewer-note.md`](../docs/agent-context/non-blocking-reviewer-note.md) |

A changed-path list is not diff content — the
[Thinness constraint](#thinness-constraint) forbids reading full diffs, not
path lists.

## Batching

Collect multiple review findings into a single `implementor` dispatch rather
than one dispatch per comment. Circuit-breaker remediation is **not** a
findings batch — see Review loop structural-rewrite / step-back routing.

## Escalation

If a phase is abandoned before its normal `stage_exit`, emit
`stage_abort --stage <stage> --abort-reason <controlled-value>` while the
recorder is still available. If the supervisor itself crashes or is
interrupted, the recovery path must use the
[loop-event recorder](../scripts/record-loop-event.py) to emit
`run_end --terminal-state crashed` or `interrupted` when it resumes with enough
context to identify the run; the [recorder tests](../tests/test_record_loop_event.py)
cover the failure-event path. These failure events are additive evidence: they
do not replace the normal
`stage_enter`/`stage_exit` or `run_start`/`run_end` obligations when those can
still be emitted.

Message the human with: issue number, round counts, recurring pattern or
blocker, recommendation. For plan-time AC defects (Loop step 4), include the
`acceptance_criteria_defects` entries (each with stable `id`) so the human
can rewrite or waive by that id before implement resumes. Pause that issue;
continue others if in flight. Emit `escalation` via `scripts/record-loop-event.py
--escalation-reason <reason>` (`round_cap`, `bug_class_recurrence`,
`dependency_blocker`, `thin_supervisor_violation`, or `scope_misalignment` —
see [instrumentation/loop-telemetry.md](../instrumentation/loop-telemetry.md)
Event types → `escalation`). Plan-time AC escalate defaults to reusing
`dependency_blocker` (same path as non-empty `blockers`; no new enum) —
**unless** the tagging obligation below applies, in which case use
`scope_misalignment` instead. Then record `run_end` with
`--terminal-state paused` before moving on.

**Tagging obligation: `scope_misalignment`.** Ask the question — not just
at Loop step 4, but at every human touchpoint below — whenever a human
response redirects the *goal* ("this isn't what I asked for") rather than
answering a factual blocker or requesting a fix within the existing
approach; see
[loop-telemetry.md Escalation](../instrumentation/loop-telemetry.md#escalation)
for the full definition and worked distinction from `dependency_blocker`.
This is the readiness-gate signal for #84 (stakeholder-alignment role vs.
gating on `open_questions_count`) — it is only useful if actually tagged
when it fires, at all three points:

- **Loop step 4** — the human's response to a `blockers` /
  `acceptance_criteria_defects` escalation reveals the plan targeted the
  wrong problem, not merely an unresolved dependency or a fixable AC. Use
  `--escalation-reason scope_misalignment` here instead of
  `dependency_blocker`.
- **Review loop (step 6)** — a human PR comment during review reveals the
  delivered work solved the wrong problem, not just that it needs
  convention/structure/test fixes. Emit `escalation` with
  `--escalation-reason scope_misalignment`; this is separate from, and
  does not replace, the normal findings-batch routing for
  implementation-level feedback.
- **Post-merge feedback** — even after `run_end` has already fired for
  this issue, a human comment (PR conversation, follow-up issue, or
  direct feedback) that reveals the merged work targeted the wrong
  problem still gets tagged: emit `escalation --escalation-reason
  scope_misalignment --correlation-id <original correlation_id>
  --issue <issue> --milestone <milestone>` against the **original**
  `correlation_id` for that issue — do not skip this because the run is
  technically closed; it is the latest and most expensive place to catch
  this failure mode, and `record-loop-event.py` accepts an escalation
  against a correlation_id whose `run_end` has already been recorded (no
  separate `run_start`/`run_end` pair, no new terminal state — just the
  one `escalation` event).
Backlog-reconciliation blocking findings (Loop step 0a) reuse
`dependency_blocker` too, but stay **unlogged** — no `escalation` event, no
`run_start`/`run_end` pair — because no issue has been selected yet at that
point (see Loop step 0a Telemetry treatment); the human message still names
the affected issue and cited reference. Record
`abandoned` only when a human explicitly instructs the supervisor to drop a
paused issue without merging, closing, or resuming. After human
rewrite/waiver: do **not** resume implement until the work item reflects
adjudication — rewritten criteria in place, and/or waived criteria
**removed** or **annotated** as waived (cite defect `id`). Hold waived
defect ids matching `acceptance_criteria_defects[].id` (and rewrite notes if
any) for Approve-loop Approver Input. The
[approver](../roles/approver.md) verifies adjudicated criteria and must not
re-fail the same plan-time defect.

## Milestone complete

When the container has no remaining open work — milestone path: zero open
issues on the milestone; parent-issue path: all sub-issues closed
(recursive; no open descendant):

### Aggregate mode — human bulk gate

1. Confirm every intended issue PR is merged into the tracking branch and the
   aggregation PR is up to date (description lists landed issues; CI on the
   aggregation PR is green or explicitly waived by the human).
2. **Wait for human merge of the aggregation PR into the default branch —
   hard gate.** This is the final human gate for the container. Agents must
   not merge it.
3. After human merge, delete or leave the tracking branch per repo convention;
   do not force-delete protected refs.
4. If `delivery.release_on_milestone_complete` is true, continue to
   [Release step](#release-step); otherwise report the container closed and
   ask about the next container.

### Per-issue mode

If `delivery.release_on_milestone_complete` is true, go to
[Release step](#release-step); otherwise report done.

## Release step

When `delivery.release_on_milestone_complete` is true and the container has
no remaining open work (same rule as [Milestone complete](#milestone-complete):
milestone path — zero open issues on the milestone; parent-issue path — all
sub-issues closed) and, in aggregate mode, the aggregation PR has been
human-merged:

1. Dispatch `implementor` to bump version and roll changelog per target repo
   conventions.
2. Open release PR targeting the default branch; wait for human merge (same
   default-branch hard gate).
3. Report the container closed and ask about the next container.

## Do not

- Check out an issue branch or otherwise edit files directly inside a shared
  local clone's own working tree — always cut a fresh `git worktree` from
  the fetched integration base (Loop step 3 Isolation).
- Force-push, or merge **into the default branch**.
- Skip the human hard gate for default-branch lands (per-issue PRs in
  `per-issue` mode, or the aggregation PR in `milestone-aggregate` mode).
- Leave a delivery PR as draft except under the Open PR draft exception
  (step 8).
- In `milestone-aggregate` mode, merge an issue PR before review and approve
  both pass, or merge an issue PR directly to the default branch.
- In `per-issue` mode, set `agent_may_merge: true` or auto-merge issue PRs.
- Batch multiple issues on one issue branch/PR.
- Fabricate merge status.
