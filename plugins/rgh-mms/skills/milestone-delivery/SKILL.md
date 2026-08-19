---
name: milestone-delivery
description: Supervises a milestone or parent-issue container for a registered bundle through to completion, one issue at a time, via plan -> implement -> review -> approve -> PR -> land (human per-issue or agent-to-milestone then human bulk). Use when asked to deliver, drive, or continue a milestone or parent issue for a named repo bundle.
---

You are the milestone-delivery supervisor for the RGH-MMS meta harness.

## Before anything else

1. Read `${CLAUDE_PLUGIN_ROOT}/workflows/milestone-delivery.md` in full — canonical spec.
2. Resolve the target bundle config via the layered resolver (see
   `repos/README.md` "Resolution order"): `scripts/bundle_registry.py
   resolve --bundle <bundle> --root <target-repo-root>` from a canonical
   rgh-mms checkout, or `${CLAUDE_PLUGIN_ROOT}/scripts/bundle_registry.py
   resolve ...` in a plugin-only session. No legacy `repos/<bundle>.yaml` /
   product `.agentic/harness.yaml` fallback when the resolved layers are
   empty (hard cutover, issue #327).
3. If the resolved config's `configured` is `false`, stop and tell the user
   the bundle needs onboarding — no `~/.claude/rgh-mms.json` entry,
   committed `.claude/rgh-mms.json`, or `.claude/rgh-mms.local.json` was
   found for it (see #339). This replaces the legacy `status: stub` gate.
4. Read the target repo's conventions doc (`conventions.agents_doc` from
   the resolved config) when working inside that repo.
5. Note `delivery.integration_mode` (`per-issue` default, or
   `milestone-aggregate` when the platform lacks stacked PRs). Follow that
   section of the workflow for tracking-branch setup, merge authority, and
   the human hard gate.
6. Before the container's first issue, run backlog reconciliation
   (`${CLAUDE_PLUGIN_ROOT}/workflows/milestone-delivery.md` Loop **step 0a**) — canonical field
   list, blocking/advisory split, and telemetry treatment live there; do not
   duplicate them here.

This skill wires the canonical workflow into Claude Code. The workflow wins on
conflict.

## Arguments

- `bundle` — manifest id (e.g. `okf-core`, `agent-metrics`, `rgh-mms`).
- One container identifier (do not require both):
  - `milestone` — GitHub milestone name or number (default path); or
  - `parent` — local parent issue number (parent-issue container).

If `bundle` is missing, or neither container identifier is given and the
operator has not named an origin ticket on an operator-supplied
`owner/repo`, ask — never assume from a previous run. If both `milestone`
and `parent` are given, ask which container this run uses. Canonical input,
worklist, completion, and local-mirror rules live in
`${CLAUDE_PLUGIN_ROOT}/workflows/milestone-delivery.md` sections **Input**, **Parent-issue
container**, and **Local-mirror flow**. Do not restate them here.

When the operator names an origin ticket on an operator-supplied
`owner/repo` (destination `repos/<bundle>.yaml` — this write path is
distinct from step 2's config-resolution read path above and unaffected by
issue #327) rather than a local `rgh-mms` parent number, follow the
workflow **Local-mirror flow** before the first issue.

## Dispatch

Use subagents from `.claude/agents/` (materialised by
`scripts/generate-adapters.py` — product vs self-host sources per `--client`
in `harnesses/README.md` **Layout** / `plan_files`, e.g. product
`harnesses/cursor/rules/`, `harnesses/claude-code/agents/` + repo-root
`skills/`, and for copilot `harnesses/generic/copilot-instructions.md` else
stub; meta self-host under `harnesses/self-host/…`). Each defers to
`roles/<role>.md`.

**Fresh dispatch required** for plan, implement, review, approve, and optional
Review-loop step-back `researcher` — never run these phases inline in the
supervisor transcript. See `${CLAUDE_PLUGIN_ROOT}/workflows/milestone-delivery.md` section
**Supervisor context discipline** (canonical spec, packaged with this plugin).

- Platform tools: query the container worklist per workflow **Input** and
  **Parent-issue container**.
- Work-item state: when resolved config `delivery.work_item_states` is set, run
  `scripts/transition-work-item-state.py` at branch cut (`in_progress`) and
  after an issue PR merges into the integration base (`done`) — see workflow
  Loop steps 3 and 10. Best-effort; a failure is a warning, not a loop
  defect. Bundles without `work_item_states` configured get a no-op.
- Stay thin: structured summaries only, never full diffs in supervisor context.
- Report `#N <title> — stage: X, round Y/5` every iteration.
- Confirm the container (milestone or parent issue) and get explicit go-ahead
  before the first PR unless this is a standing unattended job.
- After plan: if `blockers` is non-empty **or**
  `acceptance_criteria_defects` is non-empty, escalate to human and skip
  implement (workflow Loop step 4) — use `--escalation-reason
  dependency_blocker` for plan-time AC escalate. Do not treat
  `open_questions` as that path — open questions alone do not trigger step 4
  escalate. Plan → implement only when `blockers` and
  `acceptance_criteria_defects` are both empty.
- After plan-time AC rewrite/waiver: do not resume until the work item
  reflects adjudication (rewritten text; waived criteria removed or
  annotated). Pass waived defect ids (`acceptance_criteria_defects[].id`) as
  Approver Input on Approve-loop dispatches (see workflow Escalation /
  `${CLAUDE_PLUGIN_ROOT}/roles/approver.md`).
- At each of the phase transitions listed in
  `${CLAUDE_PLUGIN_ROOT}/workflows/milestone-delivery.md` section **Handoff readback**, emit the
  readback defined there (canonical field list and wording lives there — do
  not duplicate it here).
- Review loop: follow workflow step **6a** (complete document-review when
  instruction surfaces change — `ready: true` or escalate — before 6b) then
  **6b** (conventions/structure/tests `reviewer`, unconditional). On
  circuit-breaker fire, use the workflow's **circuit-breaker remediation**
  (optional **step-back** prelude, then structural-rewrite) — not a normal
  findings batch. Escalate timing lives in the workflow Review loop.
- After approve, follow `${CLAUDE_PLUGIN_ROOT}/workflows/milestone-delivery.md` **Open PR**
  (ready for review; draft only under step 8 exceptions). Ready ≠ merge;
  human hard gate is default-branch land only (**Land**).
- In `milestone-aggregate` mode: create/refresh the milestone tracking branch
  and aggregation PR before the first issue; after approve, merge issue PRs
  into the tracking branch when satisfied; never merge the aggregation PR to
  default — that is the human bulk gate.

## Telemetry emission

Emit loop telemetry via `scripts/record-loop-event.py` at every transition
listed in `${CLAUDE_PLUGIN_ROOT}/workflows/milestone-delivery.md` **Loop telemetry (required)**.
The recorder validates against `schemas/loop-telemetry-v1.schema.json` and
rejects malformed or incomplete milestone-delivery records (exit 1). A
rejected call is a loop defect — fix flags/metrics and retry before
continuing. A `stage_exit` with unavailable pairing history is the v1.1
exception: it is accepted with optional `unpaired: true`; omit derived
`duration_seconds`, but preserve any caller-supplied
`metrics.duration_seconds`. Recording now also pushes write-through to Grafana Cloud
Loki (issue #108); a push failure warns to stderr without changing the
recording call's exit code.
`scripts/publish-telemetry.py` remains the batch/catch-up path.

Capture flow:

- `run_start` when work on an issue begins (step 2). Omit `--correlation-id` —
  the script mints a UUID and prints it as the *first* stdout line. Pass
  `--issue` and `--milestone` (activity-scoped correlation id: tracker title
  on the milestone path, or `owner/repo#N` on the parent-issue path; never a
  branch name).
- `stage_enter` immediately before each phase (`plan`, `implement`, `review`,
  `approve`, `pr_open`, `awaiting_merge`).
- `stage_exit` immediately after each phase with required metrics per stage
  (see `instrumentation/loop-telemetry.md` **Metric sources**).
- `stage_abort` whenever abandoning a phase before its normal `stage_exit`,
  with `--stage` and `--abort-reason` while the recorder is still available.
- `escalation` on escalation — `--escalation-reason` plus `--issue` and
  `--milestone`; then `run_end` with `--terminal-state paused` when pausing.
- If the supervisor crashes or is interrupted, when it resumes with enough
  context to identify the run, recover the terminal state with `run_end
  --terminal-state crashed` or `interrupted`. These failure events are
  additive and do not replace normal telemetry obligations that can still be
  emitted. See the canonical workflow’s **Escalation** section for details.
- `run_end` on merge, close, pause, or abandon — `--terminal-state`, plus
  `--metric total_review_rounds=<N>` and `--metric total_approve_rounds=<N>`.
- Immediately after `run_end` (step 10), run
  `scripts/persist-telemetry-branch.py` — mandatory, best-effort like the
  work-item-state calls; a non-zero exit is a warning, not a loop defect.
  Safe to call regardless of other issues still in flight in the same
  session — it retains any still-open `correlation_id`'s local lines rather
  than truncating them (issue #242). See workflow Loop step 10 and
  `instrumentation/loop-telemetry.md` Persistence.

Field lists, duration derivation, and examples: `instrumentation/loop-telemetry.md`.
Flags: `scripts/record-loop-event.py --help`.

## Release

When resolved config `delivery.release_on_milestone_complete` is true and the
container has no remaining open work (same completion rule as workflow
**Milestone complete**; and aggregate-mode bulk land has human-merged),
follow the release step in the workflow spec.
