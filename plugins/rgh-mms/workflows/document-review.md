# Document Review Loop

Operating spec for the supervisor that runs documentation lenses on a doc-only
diff — prose and instruction files without behavior changes.

Platform skills (e.g. `skills/document-review/`) must defer to this document.

## When to use

- Doc-only PRs whose changed paths match lens triggers in
  [policy/documentation-lenses.md](../policy/documentation-lenses.md)
  (do not re-list trigger paths here).
- Meta harness policy edits (this repo).

## When not to use

- Behavior changes → use [milestone-delivery](milestone-delivery.md) or
  [contract-first-change](contract-first-change.md) with full reviewer + approver.
  When a milestone diff also touches instruction surfaces, complete
  document-review as milestone-delivery Review loop **6a** (`ready: true` or
  escalate) before conventions review **6b** (see
  `workflows/milestone-delivery.md`).
- Large multi-file doc regenerations → use [documentation](documentation.md)
  for routine edits; a dedicated regeneration workflow is P2 backlog.

## Prerequisites

- [policy/documentation-lenses.md](../policy/documentation-lenses.md) on the
  pinned harness version.
- A diff or branch to review (PR, local branch vs default).
- When `bundle` is set, resolve its config via the layered resolver
  (`scripts/bundle_registry.py resolve --bundle <bundle> --root
  <target-repo-root>` — see `repos/README.md` "Resolution order"; no
  legacy `repos/<bundle>.yaml` fallback, issue #327) and pass
  `conventions.agents_doc` (and `conventions.review_checklist` when
  present) from the resolved config to every lens dispatch.

## Thinness constraint

The supervisor dispatches one lens per fresh `reviewer` subagent (or fresh
session when subagents are unavailable) and reads only structured lens summaries.
Never run lenses inline in the supervisor transcript.

## Loop

1. **Identify scope.** List changed prose paths in the diff per
   `documentation-lenses.md` triggers.
2. **Style lens.** Dispatch `reviewer` with the `style` lens. Collect findings.
3. **Specificity lens.** Fresh dispatch with the `specificity` lens.
4. **Prompt-engineer gate.** If any instruction-surface path changed, fresh
   dispatch with the `prompt-engineer` lens. Block until findings are empty
   (`no issues found` on pass).
5. **Remediate (if needed).** Batch findings; dispatch `implementor` once.
6. **Re-run failed lenses.** After remediation, repeat steps 2–4 for any lens
   that failed — fresh dispatch each time — until all pass or escalate.
7. **Report.** Return supervisor output (below).

## Output

Supervisor returns:

- `lenses_run`: list of lens names executed (including re-runs)
- `findings`: aggregated actionable items (empty if all passed)
- `ready`: boolean — true only when every lens's findings list is empty

Derive `ready` from empty findings, not from parsing `no issues found` when
findings are present.

## Do not

- Inline lens checklists in the supervisor context.
- Skip `prompt-engineer` when instruction files changed.
- Report `ready: true` without re-running lenses after remediation.
- Expand scope into code fixes without explicit user approval.
