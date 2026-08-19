# Documentation Lenses

Cross-cutting checklists for prose and instruction-file review. Lenses are
short, fixed-output audits — not supervisor skills. Dispatch a `reviewer`
subagent (or a fresh session when the client lacks subagents — see
`clients/compatibility.yaml`) with one lens at a time; aggregate findings
before remediation.

**When to use:** doc-only PRs, policy/workflow edits, `AGENTS.md` / `CLAUDE.md`
changes, and any milestone-delivery review phase that touches instruction files.

## Lens output contract

Every lens run must return:

1. **Lens name** (`style`, `specificity`, or `prompt-engineer`)
2. **Findings** in the lens-specific format below

**Pass:** findings list is empty; final line is exactly:

```text
no issues found
```

**Fail:** one or more findings; **do not** emit `no issues found`.

Do not mix lenses in one dispatch. Run each lens in a fresh reviewer context.

---

## style

**Trigger:** Changed prose in `docs/`, `*.md`, `policy/`, `workflows/`, `roles/`,
or user-facing strings in templates.

**Checklist:**

- Voice is direct and active; avoid passive hedging ("might", "could perhaps",
  "it seems").
- Filler phrases removed ("in order to", "basically", "simply", "just").
- Tense consistent within a section (present for current behavior, past for
  history).
- Parallel structure in lists and headings.
- No marketing tone in governance or technical docs.

**Required output format (pass):**

```markdown
## style lens

no issues found
```

**Required output format (fail):**

```markdown
## style lens

- "<quoted phrase>" → <suggested fix>
- ...
```

---

## specificity

**Trigger:** Claims about behavior, APIs, file layout, CLI flags, workflow
steps, or repo conventions.

**Checklist:**

- Every behavioral claim points to a code path, config key, CLI `--help` output,
  test name, or canonical doc section.
- No aspirational language ("will support", "planned") unless labeled as future
  work in an explicit out-of-scope section.
- Examples use real paths and commands from this repository.
- Cross-repo references name the bundle or manifest id, not vague "the product
  repo".

**Required output format (pass):**

```markdown
## specificity lens

no issues found
```

**Required output format (fail):**

```markdown
## specificity lens

- <file or section>: "<unanchored claim>" → anchor to <path, test, or command>
- ...
```

---

## prompt-engineer

**Trigger:** Edits to instruction surfaces — `AGENTS.md`, `CLAUDE.md`,
`policy/`, `roles/`, `workflows/`, `skills/`, `harnesses/`, and generated
adapter stubs under `.claude/` or `.cursor/`.

**Pre-PR gate:** Before opening a PR that touches the paths above, run this
lens on the full branch diff. **Do not open the PR** until the lens passes or
every finding is resolved. Implementors run the gate after `ci.local_command`
passes and before the supervisor opens the PR.

**Checklist:**

- Instructions are internally consistent (no contradictory rules in the same
  file or across linked policy).
- Scope boundaries explicit (what the role/skill does **not** do).
- Deferral links point to canonical sources (`roles/`, `workflows/`, `policy/`),
  not duplicated prose. Prefer a section anchor over a whole-file link when
  the obligation lives in one section — a whole-file reference binds readers
  to later additions they never reviewed.
- Trigger conditions are actionable ("when X, do Y"), not vague ("be careful").
- No stale references to removed files, roles, or scripts.
- Output shapes match role specs where the file defines agent behavior.

**Required output format (pass):**

```markdown
## prompt-engineer lens

Ready to commit: yes

no issues found
```

**Required output format (fail):**

```markdown
## prompt-engineer lens

1. <file>:<section> — <issue> → <fix>
2. ...

Ready to commit: no
```

---

## Supervisor usage

| Change type | Lenses (order) |
|-------------|----------------|
| Doc-only prose | `style` → `specificity` |
| Instruction / policy files | `style` → `specificity` → `prompt-engineer` (gate) |
| Code + docs | Code review per `review-policy.md`; add lenses for doc paths in diff |

Supervisors run lenses in sequence and aggregate findings before remediation.
See [document-review](../workflows/document-review.md) for the supervisor loop.
See [document-review](../workflows/document-review.md) for the supervisor loop.
