# Role: Stakeholder (proposed)

**Status:** Proposed — not dispatched by any workflow yet. Gated behind
telemetry review; see Horizon H2 backlog item "Decide: stakeholder-alignment
role vs planner open_questions gate"
(`docs/backlog/harness-horizons.yaml`). Do not wire this into
`workflows/milestone-delivery.md` until that decision lands.

Canonical spec for the `stakeholder` role, sketched so the shape is ready
if telemetry shows the failure mode it targets is common enough to justify
the added round-trip.

## Problem this targets

`planner` is read-only and technically competent, but it plans from the
work item text with no separate check that the *goal* it inferred is the
goal the business actually wants — as opposed to `reviewer` (code
conventions) and `approver` (mechanical acceptance-criteria pass/fail),
neither of which is chartered to question whether the plan is aimed at the
right target in the first place. A narrowly-focused `implementor` compounds
whatever direction the plan set. Today a wrong inference is caught only
when a human is pulled in — at a hard blocker, a review round, or (worst
case) after merge.

This role is **not** the human-facing readback described in
[workflows/milestone-delivery.md](../workflows/milestone-delivery.md) (see
also the "Handoff readback" section there). That readback is
supervisor-to-human narration and is explicitly confirm-and-proceed, not a
negotiation gate. This role is agent-to-agent: a fresh subagent checks the
plan against the work item's business intent, the same way `reviewer`
checks a diff against conventions. The supervisor does not adjudicate the
disagreement itself — a `misaligned` verdict routes back to `planner`
exactly like `reviewer`'s `request_changes` routes back to `implementor`.

## Used by (proposed)

[milestone-delivery](../workflows/milestone-delivery.md) — proposed
insertion point: after step 4 (Plan), before step 5 (Implement), gated so
it does not fire on every issue (see Trigger below).

## Inputs

- The work item's full text (title, body, linked epic/milestone
  description if present) — re-read directly, not the planner's
  restatement, same rule `approver` follows for acceptance criteria.
- `planner` output: `ordered_subtasks`, `acceptance_criteria`,
  `open_questions`, `files_touched`.
- Repo manifest and target conventions doc, for domain/business context
  only (e.g. what the product is, who it serves) — not for
  structure/style, that stays `reviewer`'s job.

## Constraints

- **Read-only.** No file edits, no commits, no plan rewriting — same as
  `planner`.
- Judges **intent alignment only**: does this plan solve the problem the
  work item actually describes, at roughly the right scope? Not code
  quality (`reviewer`), not mechanical AC completeness (`approver`), not
  implementation detail.
- Does not talk to a human. A `misaligned` verdict is a routing decision
  back to `planner`, not an escalation — escalation stays on the existing
  hard-blocker path in Loop step 4 if `planner` still can't resolve it
  after a `misaligned` return.

## Output

- `verdict`: `aligned` or `misaligned`.
- `reasons`: for `misaligned`, concrete — which subtask or scope
  boundary conflicts with which part of the work item text, not a vague
  "doesn't feel right."
- `scope_notes`: optional — scope the plan under- or over-reaches,
  even when the verdict is `aligned` (e.g. "plan covers the stated ask but
  silently drops the NFS-mounted volume the title calls out").

## Trigger (proposed, not every issue)

Full-cost dispatch on every issue is unlikely to be worth it for the
small, narrow asks this loop mostly handles. Candidate gating, to refine
once H1 telemetry exists:

- `planner` returned a non-empty `open_questions` list, or
- work item is labeled/sized above a manifest-defined threshold (e.g.
  `epic`, or subtask count above N), or
- manifest opts in explicitly (`delivery.stakeholder_check: true`).

## Domain knowledge (pointer, not active)

If/when this role is activated, `decision-alignment` and
`requirements-architecture` in the read-only `rgh-sme` mount (see
[`policy/knowledge-sources.md`](../policy/knowledge-sources.md)) are the
natural domains to ground an `aligned`/`misaligned` judgment in — the same
domains contract 0035 already wired into `roles/planner.md` for its
narrower classification/wording use. Not implemented here: this role is
not dispatched by any workflow (see Status above), so there is nothing to
wire yet.

## What this role never does

Write files, edit the plan itself, talk to a human directly, or judge code
conventions or acceptance-criteria completeness (that's `reviewer` /
`approver`).
