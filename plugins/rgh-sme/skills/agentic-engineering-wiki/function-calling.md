---
type: concept
title: Function Calling
description: >
  Model-provider-native tool use — declare a tool inventory, let the model
  emit structured calls, execute them in the harness, and feed results back.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 8"
  - title: "MemGPT: Towards LLMs as Operating Systems"
    resource: "MemGPT (Packer et al.), §2.3"
  - title: "Toolformer: Language Models Can Teach Themselves to Use Tools"
    resource: "Toolformer (Schick et al.), pp. 1–17"
---

Function calling is model-provider-native tool use for an
[LLM agent](llm-agent.md) — mechanically a fine-tuned chat model plus
API-level syntactic sugar, detailed in
[tool definition internal representation](tool-definition-internal-representation.md).
The pattern:

1. Declare a [tool inventory](tool-inventory.md) — name, parameters,
   documentation ([tool definition design](tool-definition-design.md)).
2. Specify which tools are allowed for the query (`required`, `none`, or
   `auto`).
3. When the model finishes with tool calls, the harness invokes the real
   functions and feeds outputs back for the next model turn.

A typical harness loop: send messages plus tool schemas; append the assistant
message; if it contains tool calls, execute each and append `role: tool`
results; repeat until the model returns user-facing prose. That inner loop is
one while-loop from a full conversational agent under
[conversational agent context](conversational-agent-context.md). Validate
arguments before execution and feed runtime errors back as observations so the
model can recover — [function-call chaining](function-call-chaining.md) then
lets multi-step tool work continue in the same user turn when the model
requests another heartbeat.

Under the hood, tool calling is still chat-template completion plus
fine-tuning — syntactic sugar at the API, not a separate execution engine.
Providers may render tools as TypeScript-like signatures in the system message
(richer types, named JSON arguments) and use special roles/tokens for call and
response turns. Token-by-token, the model chains small decisions: whether to
call a tool, which tool, which argument, what value.

APIs may guarantee that only *valid* function names are generated, but they do
not guarantee correct parameter *values*. Always log the parameters used per
call and inspect them — wrong values are a leading
[planning failure mode](agent-planning-failure-modes.md), including
[argument hallucination](argument-hallucination.md), where the model invents a
plausible value for an argument no one supplied. Clear tool docs
([tool definition design](tool-definition-design.md)),
simpler function surfaces, stronger models, and plan-specific finetuning all
reduce invalid or wrong calls.

Both the action sequence and the parameters are model-generated and therefore
hallucination-prone. Prefer [plan-validate-execute](plan-validate-execute.md)
over blind execution when stakes are high. Never rely on prompt text alone to
block dangerous tools — intercept at the application layer with
[human approval gates](human-approval-gates.md).

An alternate lineage inserts tools as
[inline API call interruption](inline-api-call-interruption.md) inside a single
decode stream and may train timing via
[self-supervised tool annotation](self-supervised-tool-annotation.md) rather
than chat-style tool messages. Choose the interface your model was actually
trained for; mixing shapes without finetuning or strong few-shot scaffolding
invites format drift under [action format enforcement](action-format-enforcement.md).
