---
type: concept
title: Multimodal Prompt Framing
description: >
  Treat images and video in a prompt the same way as any other context —
  include only what's relevant, introduce their role in text, and favor
  familiar visual motifs over novel ones.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 11"
  - title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
    resource: "SWE-bench (Jimenez et al.), pp. 1–15 (§5); pp. 31–45 (Appendix F)"
---

Multimodal models process an image by converting it into embedding vectors of
the same dimensionality as text-token embeddings, with positional information
imbued into the image vectors to preserve spatial relationships; the combined
image-and-text vector sequence then runs through the same transformer used
for text. Video is commonly handled by sampling individual frames as images.
Because the image ends up feeding the same underlying completion process as
text, the existing prompt-engineering principles for text apply to images
essentially unchanged, not as a separate discipline:

- **Include only images relevant to the conversation.** An irrelevant image
  distracts the model from the task the same way irrelevant text does — see
  [prompt element importance](prompt-element-importance.md) for the general
  principle of trimming to what actually helps.
- **Frame images with text that introduces their role**, the same way a
  [prompt introduction](prompt-introduction.md) sets the model up to interpret
  everything that follows through the right lens — an unintroduced image
  forces the model to guess why it's there before it can use it correctly.
- **Use patterns and motifs present in training data** rather than inventing
  a novel visual format: don't design a bespoke diagram convention when a
  common one already exists on the internet and in the model's training data.
  This is the [Little Red Riding Hood principle](little-red-riding-hood-principle.md)
  applied to images instead of text — a chart in a familiar style is easier
  for the model to read correctly than an unusual one, for the same reason a
  familiar document type is easier to complete correctly than a novel one.

**Harness gap to watch for**: real-world issue trackers routinely embed the
only evidence of a visual bug as an image (a plot showing slight bar overlap
under a log axis) with no equivalent textual description. A code-agent ACI
built as a text-only pipeline silently drops that evidence rather than
degrading gracefully — the agent still attempts a patch, guided only by
whatever it can infer from surrounding text, and fails not from reasoning
error but from an input modality the harness never captured. When the task
domain's issues can carry images (bug reports, UI specs, design diagrams,
user screenshots), route them through a vision-capable model or an
image-to-text preprocessing step in the
[agent-computer interface](agent-computer-interface.md) rather than assuming
a coding agent only ever needs text. This is not a rare edge case in
visually-oriented domains: on SWE-bench, plotting-library repositories run
far above the corpus baseline for image-bearing issues (32% of matplotlib and
10% of seaborn instances embed an image in the issue text vs ~2% overall) —
audit per-repository or per-domain image rates before deciding a text-only
ACI is good enough for the whole task distribution, rather than assuming the
corpus-wide average applies everywhere.
