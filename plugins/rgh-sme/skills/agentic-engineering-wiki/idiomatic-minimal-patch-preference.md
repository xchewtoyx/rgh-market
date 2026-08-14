---
type: concept
title: Idiomatic Minimal Patch Preference
description: >
  Prefer the smallest framework hook that fixes the bug over reimplementing
  larger APIs — agents often localize correctly then over-build the edit.
sources:
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 106–118"
  - title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
    resource: "SWE-bench (Jimenez et al.), pp. 31–45 (Appendix F)"
---

Software-engineering agents frequently **localize the right symbols** yet
submit an **over-specific patch**: reimplement a higher-level API instead of
the one-line framework hook maintainers expect. Example
(`django` readonly password hash label): the agent overrides `label_tag` on the
field (custom HTML, mid-file imports) while the gold fix is
`id_for_label → None` on the **widget** so Django’s label machinery omits
`for` — smaller surface, idiomatic extension point.

The same over-specific-patch pattern recurs across models and languages under
[gold-standard matching](gold-standard-matching.md) qualitative review, and
takes two related shapes:

- **Invented primitive over existing helper.** Claude 2 on a bool-input
  `TypeError` (scikit-learn `HuberRegressor`) adds a hand-rolled
  `_validate_data` that `astype`s booleans to `float64`, instead of routing
  through the framework's existing `check_X_y(..., dtype=[...])` validator
  the gold patch uses — passes both fail-to-pass and pass-to-pass tests, but
  is stylistically and organizationally inconsistent with the codebase.
  Similarly, extending an `isinstance(..., bool)` check with manual
  `== 0 or == 1` branches (matplotlib `sharex`/`sharey`) where the gold patch
  instead folds the cases into an existing `check_in_list` helper **and**
  deletes now-dead related code — the agent's ad hoc branch neither
  generalizes nor cleans up after itself.
- **Generic/popular answer over codebase-specific mechanism.** Claude 2 fixes
  a cyclic-import false positive by adding a bare `TYPE_CHECKING` import
  guard — the common "Stack-Overflow-style" answer to that class of Python
  error — when the gold fix detects the guard via the codebase's own
  `astroid.If` / `is_typing_guard()` dependency-graph machinery. A
  popular general-purpose answer can be *syntactically* the idiomatic-looking
  fix while still being the wrong idiom for *this* codebase; prefer prompts
  and demos that push the agent to search for an existing project-specific
  mechanism before reaching for a generically "correct" pattern it has seen
  often in pretraining.

A third, opposite-looking but related shape is **missing a branch that an
analogous sibling already implements**. Fixing sphinx's `napoleon` extension
to honor a `napoleon_use_param` config flag in one section-parsing function,
the agent edits the right function but hardcodes the True-branch behavior
instead of branching on the config value — while a **sibling function in the
same file** (`_parse_parameters_section`) already implements exactly that
branch for a near-identical section type. The bug was locally correct-looking
(tests without the flag pass) but wrong under the flag's False setting, which
a same-file analogous implementation would have revealed as the expected
shape. Before treating localization as done, search the file (or module) for
a **sibling function handling a structurally similar case** and mirror its
branching, not only its target symbol — an existing parallel implementation
is often a more reliable template than reasoning about the config surface
from scratch. Quantitatively, applied model patches tend to run noticeably
shorter and touch fewer files/functions than gold across the board (SWE-bench
oracle: ~19.6 lines / 1.0 files for applied Claude 2 patches vs ~44.1 lines /
1.2 files for gold on the same instances; gold averages 3.0 functions touched
overall) — models default to the smallest change that makes the target test
pass rather than the structurally complete one, which is this same
missing-branch pattern at scale, not only isolated case studies.

The under-sized-patch tendency above is specific to **prompted** general
models. LoRA-**fine-tuned** code models trained on gold patches show the
opposite asymmetry: patches averaging *longer* than gold, not shorter, with
more hallucinated content, style mismatches, and long-range-dependency errors
as patch length grows. Which direction to expect is a property of how the
model was built, not a universal law — prompted models tend to stop once
tests pass, fine-tuned models tend to over-produce plausible-looking code
toward the training distribution's typical patch length. Size the specific
[offline harness test](per-task-offline-harness-tests.md) checks (diff-size
delta from gold, novel-symbol rate) to the failure direction your model class
actually exhibits rather than assuming under-building is the only risk.

Design implications for the harness:

- [Failure-derived prompt tips](failure-derived-prompt-tips.md): prefer
  existing override hooks (`id_for_*`, empty returns that disable defaults)
  and **already-imported helpers** (`to_native_string` vs decode-then-
  `builtin_str`) before inventing new HTML/render or type-branch paths.
- After localization, prompt a short “what is the smallest API that controls
  this behavior?” thought before
  [guardrailed edit](guardrailed-edit-tool.md).
- Score patches not only on tests but on **diff size / API novelty** in
  [offline harness tests](per-task-offline-harness-tests.md) when gold patches
  exist — overbuild is a dominant unresolved-task mode under
  [compound mistake amplification](compound-mistake-amplification.md). Agent
  patches are often larger than gold partly from leftover
  **reproduction code**; require cleanup before submit under
  [agent episode termination modes](agent-episode-termination-modes.md).

Guardrails still help: lint catching missing imports blocked a bad first edit
and forced a retry — but they do not catch *semantically heavy* correct-syntax
patches. Pair with runtime checks of the reported behavior before `submit`
when the environment allows; submitting without verifying accessibility/`for`
output is a goal-failure under
[agent planning failure modes](agent-planning-failure-modes.md).
