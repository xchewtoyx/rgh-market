---
type: concept
title: Fine-Tuning Decision
description: >
  Decide whether to fine-tune based on whether you can gather enough correct,
  well-formatted, on-domain training examples — not on model quality alone.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 7"
  - title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
    resource: "SWE-bench (Jimenez et al.), pp. 1–15 (§5)"
---

Building or training a model from scratch is rarely warranted, but taking an
existing model and training it further on task-specific data — fine-tuning —
may be, once
[prompt engineering](prompt-engineering.md) alone isn't enough. Initial model
training is reading and mimicking a huge number of documents; fine-tuning
presents new documents and trains the model to mimic those specifically,
usually at some cost to generic-document ability, in exchange for much better
performance on the document types you actually care about.

Training documents need to be factually correct, use only the background
information you actually want the model to learn, and follow the exact format
expected downstream — bad training data teaches the model to reproduce the
badness. Sources for such documents: create them yourself, hire contractors,
synthesize them, or — if the application already has users — collect them
from success signals (accepted suggestions, likes) or from a prior,
human-performed version of the task now being automated. Whether you can
actually gather examples like this at sufficient volume and quality is the
key factor in deciding whether fine-tuning is worth attempting at all; a
promising [model selection](model-selection-tradeoffs.md) case that can't
supply good training data isn't ready for fine-tuning yet, no matter how
much it might help in principle.

**Match training-time and inference-time context distribution.** Fine-tuning
teaches a model what to expect in its input, not only what to produce — a
model fine-tuned to edit code given a curated, always-relevant context (every
file it sees should be edited) can perform much worse at inference time when
the real retrieval pipeline hands it noisier, partially-irrelevant context
where most retrieved files should be left untouched (SWE-Llama, fine-tuned
under oracle-only context, drops sharply under realistic BM25 retrieval
relative to prompted general models trained on more heterogeneous data). If
the deployed [ACI](agent-computer-interface.md) or retrieval pipeline can hand
the model imperfect or partially off-target context, the fine-tuning set
needs the same noise profile, not only clean positive examples.

**Loss masking** — some fine-tuning frameworks let you train only on the
portion of a document that addresses the problem (the solution), not the
portion where the problem itself is stated, since you're not actually
interested in the model's ability to reproduce the prompt half of the
document. This keeps training focused on the behavior you actually want
learned. See [fine-tuning approach comparison](fine-tuning-approach-comparison.md)
for how to choose among the different ways to fine-tune once the decision is
made.
