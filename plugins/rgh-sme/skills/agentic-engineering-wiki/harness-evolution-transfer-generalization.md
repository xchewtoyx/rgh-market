---
type: concept
title: Harness Evolution Transfer and Generalization
description: >
  Freeze an evolved harness and move it to an unseen benchmark or a different
  base model without further evolution — the result separates general
  engineering experience from benchmark-specific tuning.
sources:
  - title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
    resource: "Agentic Harness Engineering (Lin, Liu, Pan, et al.), §4.3"
---

Any [harness evolution outer loop](harness-evolution-outer-loop.md) that
optimizes against one benchmark risks producing a harness that only works
*there* — edits shaped around that benchmark's specific tasks rather than
durable engineering practice. The diagnostic is transfer: freeze the evolved
harness exactly as evolution left it, apply zero further edits, and move it
to (a) a different task surface and (b) different base models than the one
evolution ran on.

**Cross-benchmark transfer.** A harness evolved on one long-horizon terminal
benchmark, moved unchanged to a repository-scale patch-resolution benchmark,
can post the highest aggregate success among the compared methods *while also
using fewer tokens than its own unevolved seed* — evidence the evolved
components (tools, middleware, memory) encode reusable engineering behavior
rather than per-call re-derivation. Contrast this with prompt-only
self-evolution baselines (a distilled natural-language playbook, or a
trajectory-feedback method that reinforces successful tool sequences): both
can *regress below their own unevolved seed* on the new benchmark while
spending 11–29% more tokens than that seed, because the text they inject was
distilled from the original benchmark's traces and rides every prompt
regardless of whether it's still relevant — a cost with no corresponding
benefit once the task surface has changed. This is the transfer-side evidence
for why [component-level harness ablation](component-level-harness-ablation.md)
locates the gain outside the prompt: what lives in tools and middleware
transfers; what lives only in prompt text does not travel as cleanly.

**Cross-model transfer.** Moving the same frozen harness across several
alternate base models (holding the harness fixed, swapping only the model)
can produce positive gains across every model tried — evidence the harness
isn't specific to one provider's idioms. But gain magnitude tracks *how far
the alternate model sits from the operating point evolution was tuned
against*, not raw model capability: models further from that operating point
lean more heavily on the coordination patterns the harness encodes, while a
model close to the original operating point can re-derive the same
coordination cheaply from its own prompt-following ability, leaving less
headroom for a fixed harness to add.

**The honest caveat.** Evolution's step budget and per-task timeout are
themselves fitted to whatever base model evolution ran against — so
cross-model transfer numbers *conflate* harness portability with that
operating-point coupling. A harness re-evaluated at a different reasoning
tier of the *same* model family can show a non-monotone gain profile purely
from budget mismatch, not from the harness itself working worse. Report
transfer numbers with this caveat rather than reading gain magnitude as a pure
harness-quality signal.
