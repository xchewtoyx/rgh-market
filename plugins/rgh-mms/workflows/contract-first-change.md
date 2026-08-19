# Contract-First Change Loop

Golden path for load-bearing harness or behavior changes, distilled from
`agent-metrics`. Requires the resolved bundle config's `contracts.enabled:
true` — via the layered resolver (`scripts/bundle_registry.py resolve
--bundle <bundle> --root <target-repo-root>`; no legacy
`repos/<bundle>.yaml` fallback, issue #327).

Combines falsifiable prediction with implementation and settlement.

## When to use

- Harness, API, or schema changes that affect agent behavior or evidence.
- Skip for pure docs or trivial refactors (per target repo conventions).

## Roles

| Phase | Role | Action |
|-------|------|--------|
| 1 | planner (or human) | Confirm change needs a contract |
| 2 | implementor | Scaffold contract via manifest `contracts.cli` |
| 3 | implementor | Implement change + tests + docs |
| 4 | reviewer | Review diff + contract presence |
| 5 | approver | Verify acceptance criteria (optional) |
| 6 | implementor | `settle` contract with verdict and evidence |

## Contract scaffold

Use the target repo's contract CLI (e.g. `agent-metrics contract "Title"`).
Name contracts under manifest `contracts.directory` using one of two
filename schemes (issue #250):

- **Legacy — `NNNN_slug.md`.** A zero-padded, 4-digit sequential id. This
  scheme is **frozen**: it covers the existing files only
  (`0001`-`0045` in this repo's own registry). Do not scaffold a new
  contract with a sequential legacy id — the id is allocated by each
  author reading the current registry and picking the next unused number,
  which two branches working concurrently can pick identically without
  either author knowing; the only defense is CI's duplicate-id lint
  catching the collision after the fact, at merge time (see issue #250 and
  contract `0045_remote_tracking_integration_base.md`, which names this
  exact race as this issue's failure mode).
- **Issue-keyed — `i<issue-number>_slug.md`.** The `i` marker plus the
  GitHub issue number that scaffolds the contract, not zero-padded
  (`i9`, `i212`, `i9999` are all valid as-is). **This is the standard for
  all new contracts going forward**, including multi-issue contracts,
  which use the scaffolding issue's own number. GitHub issue numbers are
  centrally allocated and unique by construction, so two branches
  independently scaffolding a contract for two different issues cannot
  produce the same filename prefix — the collision class the legacy scheme
  can only detect, this scheme cannot produce at all.

Both schemes share the same required content:

- Observed failure evidence
- Inferred root cause
- Proposed change
- Predicted fixes and regression risks
- Verification plan
- Instrumentation: litmus question or waiver (issue #214)
- Settle criteria (KEEP / IMPROVE / ROLLBACK)

The Instrumentation entry answers which existing event/field evidences the
change working in production loops post-merge, or the addition this
contract introduces for that purpose, or an explicit "not observable in
loop telemetry because ..." waiver. It's enforced by the
contracts-registry lint (`scripts/validate-contracts-registry.py`):
for the legacy scheme, only at/above its id threshold; for the issue-keyed
scheme, unconditionally for every contract (issue #250) — the scheme did
not exist before Instrumentation became mandatory, so there is no
pre-existing-contract class to exempt.

## Loop

1. **Predict.** Scaffold contract before load-bearing edits.
2. **Implement.** Follow [implementor](../roles/implementor.md) spec; run
   `ci.local_command`.
3. **Review.** Reviewer confirms contract exists for behavioral changes,
   checks target `review_checklist` process gates, and confirms the
   Instrumentation section is present and substantive (names a real
   event/field, addition, or waiver reason, not a placeholder) — for the
   legacy scheme, only at or above the lint's Instrumentation-enforcement
   id threshold; for the issue-keyed scheme, always (issue #250).
4. **Approve.** If work item has acceptance criteria, run approver.
5. **Settle.** Record outcome: `settle <id> --verdict KEEP|IMPROVE|ROLLBACK
   --evidence "..."`.

## Health snapshot (optional)

Repos using `agent-metrics` may append structural health after CI:

```bash
agent-metrics health --append --bundle <bundle> .
```

## Supervisor thinness

Same as milestone-delivery: supervisors consume summaries, not full diffs.
