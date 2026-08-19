# Research Loop

Lightweight read-only workflow for exploration before committing to
implementation.

## When to use

- Design decisions with multiple viable approaches.
- Upstream spec or dependency investigation.
- Planner reports `open_questions` that need evidence.
- "Spike" issues explicitly scoped as research-only.

## Input

- Bundle id and research question (from issue or user).
- Optional scope boundaries and time box.

## Loop

1. Resolve the target bundle config for constraint context via the layered
   resolver (`scripts/bundle_registry.py resolve --bundle <bundle> --root
   <target-repo-root>` — see `repos/README.md` "Resolution order"; no
   legacy `repos/<bundle>.yaml` fallback, issue #327).
2. Dispatch `researcher` with the question and scope.
3. Return structured brief to human or `planner` for follow-on implementation.
4. **Do not** open a PR or edit files unless the user explicitly expands scope.

## Output handling

- If `recommendation` is clear and user approves → hand off to
  [milestone-delivery](milestone-delivery.md) or a single-issue implement path.
- If `open_questions` remain → escalate to human before coding.
- Store brief in issue comment or linked doc per target repo practice.

## Supervisor thinness

Supervisor reads only the researcher's structured brief — not raw search dumps.
