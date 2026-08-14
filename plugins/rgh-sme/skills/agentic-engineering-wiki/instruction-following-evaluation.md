---
type: concept
title: Instruction-Following Evaluation
description: >
  Measure whether the model obeys your stated constraints — format, length,
  vocabulary, style, content limits — separately from domain skill or prose
  quality, and build custom suites for the instructions your product actually
  uses.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 4"
---

The **instruction-following** bucket of
[application evaluation criteria](application-evaluation-criteria.md) asks:
given *your* instructions, does the model comply — independent of whether
those instructions are good? A model can have domain skill (sentiment
analysis) and still fail the product contract by emitting `HAPPY`/`ANGRY`
instead of the required `NEGATIVE`/`POSITIVE`/`NEUTRAL` labels. Stronger
models generally follow instructions better, but that is not a substitute
for measuring the constraints you actually ship.

This axis is essential for
[structured output generation](structured-output-generation.md) (JSON,
regex-shaped fields) and for less obvious product rules (restrict vocabulary
to what a child can read; ban phrases like "As a language model"). It is
hard to cleanly separate from domain or generation capability: failure to
write a constrained verse form may be missing domain knowledge *or*
misreading the instruction. Evaluation is also confounded by instruction
quality itself — a low score can mean a bad model or a bad prompt — so pair
failures with
[explicit instruction design](explicit-instruction-design.md) review before
blaming the model.

Two public suites are useful templates for custom harness evals:

- **Format-verifiable instructions (IFEval-style)** — automatically checkable
  constraints: keyword inclusion/frequency, forbidden words, response
  language, paragraph/word/sentence counts, bullet/title/placeholder
  markers, JSON format, choose-from options. Score = fraction of
  instructions followed. Prefer these wherever a code-based
  [grader](agent-grader-types.md) can replace a judge.
- **Broader constraint checklists (INFOBench-style)** — content limits
  ("discuss only climate change"), linguistic guidelines ("Victorian
  English"), style rules ("respectful tone"). These need a yes/no criteria
  checklist per instruction; the model succeeds only if *all* criteria
  pass, with aggregate score = criteria met / criteria total. Model-based
  graders work here when calibrated; they can beat crowd annotators while
  still trailing experts.

**Curate your own suite** for the instructions your product actually
emits — YAML schemas, banned phrases, length caps, persona rules — rather
than relying only on public format benchmarks that may never exercise your
failure modes.

**Roleplay** is a common instruction type (user-facing personas and
roleplay-as-prompting). Automating it is hard; evaluate on two axes —
*style* (does voice match the persona) and *knowledge* (does it stay inside
what the persona would know, including "negative knowledge" checks so a
game NPC cannot leak spoilers). Use similarity scores, model judges, or
trained reward models as needed, but keep roleplay failures labeled as
instruction-following rather than domain ignorance when the missing
knowledge was deliberately out of scope.
