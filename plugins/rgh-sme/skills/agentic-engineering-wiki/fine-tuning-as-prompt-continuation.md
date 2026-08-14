---
type: concept
title: Fine-Tuning as Prompt Continuation
description: >
  Treat fine-tuning as baking static instructions and few-shots into weights so
  prompts shrink — LoRA for format and priors, full FT for new domains.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 7"
---

When [prompt engineering](prompt-engineering.md) alone is not enough, further
training on task-specific documents can teach the model to mimic the target
format and domain — usually trading some generic ability for much better
performance on anticipated document types. Training docs must be factually
correct, carry only the background you want learned, and match the expected
form. Whether you can gather such examples (hand-write, contractors,
synthesize, or collect accepted/liked user outcomes) is the go/no-go factor.

**Approaches by how much they rewrite the model:**

| Approach | Typical learnable change | Doc scale |
| --- | --- | --- |
| Full fine-tune / continued pretrain | New facts or whole domains | Tens of thousands |
| Parameter-efficient (e.g. LoRA) | Format, style, which existing skills to expect | Hundreds–thousands |
| Soft prompting | A continuous “prompt state” that elicits target outputs | Hundreds |

LoRA freezes most weights and trains a small low-rank diff — shareable across
VMs, multi-diff on one base, hours-to-days to train — but limited in how much
genuinely *new* behaviour it can add. Use it to shift domain priors and output
conventions (what to attend to, how to interpret the prompt, expected
completion shape). Full fine-tuning can carve genuinely new grooves; soft
prompting skips wordcraft and searches for a model state that produces
example outputs (availability depends on the framework).

Both full FT and LoRA usually let you **drop static prompt context and
few-shots** — those lessons live in parameters more effectively than being
re-presented every call. In that sense fine-tuning is a continuation of
prompting by other means: move durable instructions into weights, keep
instance-specific content in the prompt. Prefer **loss masking** so training
updates only the solution span, not the problem/prompt span you never want
reproduced. After any fine-tune, re-check the
[Little Red Riding Hood principle](little-red-riding-hood-principle.md) so
prompts stay on the fine-tuned path rather than the overgrown pretraining one.
When the harness only needs a specialist for some steps, combine with
[model selection criteria](llm-model-selection-criteria.md) and a
[model router](model-router.md) instead of fine-tuning the whole stack.

**Agent example (SWE-Llama):** Off-the-shelf long-context CodeLlama failed to
follow repository-edit instructions; LoRA on attention sublayers with
issue+file→gold-patch pairs (disjoint repos from eval, drop >30k-token
sequences) produced specialized editors meant for consumer hardware. Treat
that as PE continuation for a fixed edit format — still pair with
[codebase retrieval for agents](codebase-retrieval-for-agents.md) because
fine-tuning does not remove the need to select which files enter the prompt.
