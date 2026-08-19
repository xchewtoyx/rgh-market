# Review Policy

How coding agents review changes — distinct from runtime review agents shipped
as product code.

## Reviewer scope

The `reviewer` role checks:

- Conventions doc (`AGENTS.md`) compliance
- Product `local-policy.md` and review checklist
- Harness `policy/` where referenced by profile
- Tests, docs, complexity, concurrency and change-safety surfaces

The `reviewer` does **not** judge acceptance criteria — that is `approver`.

For claims a diff makes about its own coverage, completeness, or effect, see
the **Self-referential claims verification** section in
[roles/reviewer.md](../roles/reviewer.md#self-referential-claims-verification)
— canonical, not restated here. Reported test mutation-kill claims are
verified under the same duty — see the nested **Mutation kill-claim
verification** subsection at
[roles/reviewer.md](../roles/reviewer.md#mutation-kill-claim-verification).

## Documentation lenses

For prose and instruction-file changes, dispatch `reviewer` with lenses from
[documentation-lenses.md](documentation-lenses.md):

- **style** and **specificity** for doc paths in the diff
- **prompt-engineer** as a **pre-PR gate** when the diff touches instruction
  surfaces listed in the `prompt-engineer` trigger there (canonical path list —
  do not duplicate)

Run each lens in a fresh reviewer context (fresh subagent when supported;
otherwise a fresh session per `clients/compatibility.yaml`). Aggregate findings
before sending work back to implementor. See
[document-review](../workflows/document-review.md).

## Fresh-context dispatch

Portable rationale:
[`docs/agent-context/fresh-context-dispatch.md`](../docs/agent-context/fresh-context-dispatch.md).
Harness enforcement below.

Reviews must run in a **fresh subagent or session** when **implementation**
context would bias the outcome. The diff, scope summary, and checklists are
required inputs — they do not by themselves invalidate a review.

**Invalidates review (implementation context):**

- Same chat/session as the implementor dispatch
- Parent agent that planned or implemented the change
- Reviewer who already saw debugging history, design exploration, or rejected
  approaches from the implementation session

**Required reviewer inputs:**

- Work item **scope summary** and out-of-scope boundaries (from issue or planner;
  include acceptance criteria text for context — **do not** pass/fail AC; that is
  `approver`)
- Changed paths and diff reference (PR or branch)
- CI gate evidence: command name, exit code, and log path or URL from implementor
  (reviewer may re-run `ci.local_command` when evidence is missing)
- Applicable checklists: `AGENTS.md`, `review-policy.md`, and profile `policy/`
  files from `profiles/<profile>.yaml` when harness policy applies

**Forbidden reviewer inputs:**

- Implementation-session debugging transcripts
- Design rationale the implementor explored but did not ship
- "Trust me, I already fixed it" without diff evidence

Dispatch a new `reviewer` in a fresh subagent when the client supports it;
otherwise start a **fresh session** (see `clients/compatibility.yaml`).
Milestone-delivery and document-review supervisors must not run review inline —
see [milestone-delivery](../workflows/milestone-delivery.md) and
[document-review](../workflows/document-review.md).

## Approver scope

The `approver` role verifies each acceptance criterion independently with
evidence (command output, test name, observable behavior).

## Bug-class circuit breaker

On second finding in the same category within one diff, recommend a structural
fix instead of symptom patches. Milestone-delivery routes the fire to
circuit-breaker remediation (optional step-back prelude via `researcher`, then
structural-rewrite), not a normal findings batch — see
[milestone-delivery](../workflows/milestone-delivery.md) Review loop.

## Concurrency

Check-then-act surfaces declared in `.agentic/harness.yaml` or product manifest
are correctness bugs when racy, not nits.

## Change safety

Diffs touching migration, serialized-format, or config surfaces, or deleting
or renaming externally-consumed names, are checked against the
[Change-safety checklist](../roles/reviewer.md#change-safety-checklist) —
unacknowledged rollback and rollout-compatibility hazards are correctness
findings, not nits.

## Batching

Multiple review findings dispatch to implementor once per round, not per
comment. Circuit-breaker remediation is **not** a findings batch — see
[milestone-delivery](../workflows/milestone-delivery.md) Batching and Review
loop.

## Human review

Agent approve loops do not replace human PR review and merge. Humans merge.
