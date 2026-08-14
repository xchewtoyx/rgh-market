---
type: concept
title: Answer Cleansing
description: >
  Deterministically parse the model’s free-form extraction into a canonical
  answer type — number, choice letter, yes/no, or stripped free text.
sources:
  - title: "Large Language Models are Zero-Shot Reasoners"
    resource: "Large Language Models are Zero-Shot Reasoners (Kojima et al.), Appendix A.6"
---

After [two-stage reasoning–answer extraction](two-stage-reasoning-answer-extraction.md),
do not trust raw completion text as the scored answer. **Answer cleansing**
maps the extraction turn to a typed value:

- **Number** — strip commas; first regex match of an optional-signed decimal.
- **Multiple choice** — first token in {A…E} (or the task’s letter set).
- **Yes/No** — lower-case, strip punctuation; first token in {yes, no}.
- **Free text** — strip quotes, newlines, trailing dots/spaces.

Keep cleansing in the harness, not in the prompt, so metric computation stays
reproducible under [offline prompt evaluation](offline-prompt-evaluation.md).
Pair format-specific extraction cues (“arabic numerals”, “among A through E”)
with matching cleansers; mismatch is a common false-negative source when
comparing [zero-shot chain of thought](zero-shot-chain-of-thought.md) to
baselines.
