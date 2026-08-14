---
type: concept
title: Advice Conversation Document
description: >
  Frame a prompt as a conversation where one party asks for help and the
  other provides it, the document type ChatML itself is built around.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 6"
---

A prompt plus its completion together form a document, and per the
[Little Red Riding Hood principle](little-red-riding-hood-principle.md) the
best document type to write is one the model has plausibly seen many of in
training. The advice conversation — one person asking for help, another
providing it — is one such archetype: the model plays the advisor, and the
application or user plays the asker.

It is the natural fit for chat models (OpenAI built ChatML around advice
conversations specifically because they judged them the most universally
useful and easiest to implement), but it's useful for completion models too.
Advantages:

- **Natural interaction** — people already think in conversational terms; you
  can pose a question and take the model's continuation as the answer.
- **Multiround interactions** — complex interactions continue the same prompt
  with new question/answer turns, with your own application logic interleaved
  between queries.
- **Real-world integration** — the conversational shape suits multiround
  processes and integrating real-world tools, with either chat or completion
  models, via [function calling](function-calling.md).

Using this structure with a chat model gets you RLHF-driven instruction
compliance for free; using it with a completion model lets you sidestep
unhelpful RLHF traits (particular stylistic habits, content policing) while
still getting the conversational shape. Completion models writing this
archetype need an explicit
[transcript format](transcript-format-selection.md) chosen, since nothing
enforces one automatically the way a chat API's template does.
