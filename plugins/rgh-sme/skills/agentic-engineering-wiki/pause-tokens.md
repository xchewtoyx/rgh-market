---
type: concept
title: Pause Tokens
description: >
  Fine-tune a model to emit meaningless filler tokens before answering, giving
  it extra timesteps to incorporate context before committing to output.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 8"
---

Pause tokens (Goyal et al., 2023, "Think Before you Speak") fine-tune a model
to use a designated, semantically meaningless "pause" token. Injecting several
of them (e.g. 10) after a question gives the model extra forward-pass
timesteps to more thoroughly incorporate prior-token information into its
internal state before it starts answering, improving output quality —
analogous to a human's "uh"/"um" stalling for time while thinking.

Unlike [chain of thought prompting](chain-of-thought-prompting.md), this buys
extra computation without adding any content to the visible reasoning trace,
and it requires fine-tuning rather than being achievable through prompting
alone. Both techniques attack the same root problem: [autoregressive
generation](autoregressive-generation.md) has no internal monologue by
default, and any way of adding one — words or inert tokens — can improve the
model's chance of getting a hard answer right.
