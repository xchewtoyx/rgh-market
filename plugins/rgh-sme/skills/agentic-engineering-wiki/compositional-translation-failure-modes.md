---
type: concept
title: Compositional Translation Failure Modes
description: >
  Under least-to-most on compositional commands, failures split into bad
  decompositions versus translation bugs — modifiers, conjunction order, copies.
sources:
  - title: "Least-to-Most Prompting Enables Complex Reasoning in Language Models"
    resource: "Least-to-Most Prompting (Zhou et al.), pp. 31–45 (§8)"
---

On SCAN-style compositional instructions,
[least-to-most prompting](least-to-most-prompting.md) fails in either
**command decomposition** or **command translation**. Stronger models often
eliminate decomposition and copy errors while residual mistakes concentrate on
a few semantic operators — audit those operators first when engineering
[compositional mapping exemplars](compositional-mapping-exemplars.md).

**Decomposition failures:** skipping required intermediates (e.g. omitting the
bare “around X” step before “around X twice”) so later `*`/`+` factors are
wrong even if leaf mappings look plausible. Teach
[domain-specific decomposition prompts](domain-specific-decomposition-prompts.md)
to expand nesting explicitly: conjunctions → ordered subcommands; “around”
introduces an intermediate; “after” keeps both sides’ subproblems.

**Translation failure types** (from Zhou et al. Table 15):

- Incorrect **twice/thrice** — especially after “around” (apply `* n` to the
  already-`* 4` form as `* 4 * n`, not a single wrong constant) or after
  “opposite” (group the whole opposite form before repeating).
- **“After” as “and”** — both sides translate correctly but concatenate in the
  wrong order; treat sequencing as a first-class exemplar, not only
  conjunction.
- Incorrect **left/right** — drop the turn or invent atomic actions
  (“LOOK LEFT”) that break later composition.
- **Copy errors** — mangling parentheses or intermediate expressions when
  combining already-correct sub-translations.

Contrast
[decomposition-before-composition failures](decomposition-before-composition-failures.md)
on DROP (wrong facts/operators vs bad sub-answers): here the composition
algebra itself is the fragile stage. **CoT vs L2M on the same SCAN items:**
CoT often corrupts around/opposite/twice/thrice grouping in one continuous
generation; L2M’s decomposition ladder is frequently intact while residual
bugs concentrate on thrice×around (`* 8` vs `* 4 * 3`) and “after” order at
the final concat. Use these buckets in
[offline prompt evaluation](offline-prompt-evaluation.md) — sample failures,
tag decompose vs translate subtypes, and add targeted mapping demos rather than
only more CoT length.
