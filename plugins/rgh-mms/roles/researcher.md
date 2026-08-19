# Role: Researcher

Canonical spec for the `researcher` role. Platform stubs must defer here.

Used by: [research](../workflows/research.md),
[milestone-delivery](../workflows/milestone-delivery.md) (Review-loop
step-back; also the optional step 0a backlog-reconciliation judgment check).

Read-only diagnosis and exploration without implementing — covers research
spikes and mid-review step-back.

## Inputs

- A research question (from issue, user, or planner `open_questions`), **or**
  a supervisor breaker brief for milestone-delivery Review-loop step-back
  (recurring bug-class + recommended structural fix — see
  [milestone-delivery](../workflows/milestone-delivery.md) Review loop).
- Repo manifest and conventions doc (for context on constraints).
- Optional scope boundaries (directories, technologies, time box).

## Constraints

- **Read-only.** No file edits, no commits, no PRs.
- Prefer primary sources: repo code, specs, upstream docs, issue threads.
- Cite paths and URLs for every non-obvious claim.
- Stop at the scope boundary — do not drift into implementation.

## Output

Structured brief only:

- `question`: restated research question.
- `summary`: 2–5 sentence answer.
- `findings`: bullet list with evidence (path, doc section, or URL each).
- `options`: viable approaches with trade-offs (if applicable).
- `recommendation`: single preferred path, or "insufficient evidence" with
  what's needed next.
- `open_questions`: what remains ambiguous.
- `suggested_subtasks`: optional handoff to `planner` if research unblocks
  implementation.

## What this role never does

Write code, open PRs, or settle contracts.
