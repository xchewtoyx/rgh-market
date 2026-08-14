---
type: concept
title: Prompt Conversion Criteria
description: >
  Four conditions a prompt must satisfy at once to turn a user's problem into
  a completion that actually solves it.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 4"
---

Converting the user's problem into the model domain is the crux of
[prompt engineering](prompt-engineering.md): craft a prompt whose completion
addresses the user's problem, satisfying four criteria simultaneously.

1. **Resemble training-set content** — the
   [Little Red Riding Hood principle](little-red-riding-hood-principle.md):
   the prompt should closely resemble a document type the model has plausibly
   seen before.
2. **Include all relevant information** — sometimes the user's raw input
   suffices; sometimes the application must pull in preferences, calendars,
   availability, news, or other external data. The two challenges are finding
   *all* possibly relevant content and finding the *best* of it — over-
   saturating the prompt with loosely relevant material distracts the model
   and degrades completions, the same problem the
   [Chekhov's gun retrieval fallacy](chekhovs-gun-retrieval-fallacy.md) names
   for retrieval specifically. Content must also be arranged into a
   well-formatted, logical document, not just dumped in.
3. **Lead the model to a solution, not elaboration** — the prompt must
   condition the model to actually address the problem rather than merely
   restate or elaborate on it. This is trickier for completion models, which
   need an explicit signal to switch from problem-poser to problem-solver; it
   is largely solved for chat models, which are fine-tuned to produce a
   helpful assistant reply automatically.
4. **Ensure the model reaches a stopping point** — see
   [completion stop-condition design](completion-stop-condition-design.md) for
   how this is engineered, particularly for completion models where nothing in
   the API tells the model a turn has ended.

Chat APIs largely satisfy criteria 1, 3, and 4 automatically, because the
chat template resembles fine-tuning data, the model is conditioned to be
helpful, and it stops at the end of its own message. The prompt engineer
remains fully responsible for criterion 2 regardless of model type, and still
needs to shape the system message, transcript, and tool definitions so the
model can reach a genuinely successful stopping point under criteria 3 and 4.
