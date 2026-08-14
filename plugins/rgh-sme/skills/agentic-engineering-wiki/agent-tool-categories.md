---
type: concept
title: Agent Tool Categories
description: >
  Agent tools fall into knowledge augmentation, capability extension, and write
  actions, with risk rising sharply for tools that mutate the environment.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 4"
  - title: "Toolformer: Language Models Can Teach Themselves to Use Tools"
    resource: "Toolformer (Schick et al.), pp. 1–17"
---

Tools in an agent's [tool inventory](tool-inventory.md) group into three
practical categories:

**Knowledge augmentation** expands what the agent knows: retrievers, SQL
executors, people search, inventory APIs, email readers, and web browsing.
These construct [context](context-engineering.md) from private or public data.
Web browsing fights training-cutoff staleness but exposes the agent to
unreliable or harmful content, so API choice matters.

**Capability extension** patches model weaknesses more cheaply than training
them away: calculators, calendars, converters, translators, and especially code
interpreters that return execution results and errors. Tools can also make a
unimodal model effectively multimodal (image generation, OCR, transcription,
charting via code). Scaling alone does not fix up-to-date knowledge,
precise math, low-resource languages, or time awareness —
[Toolformer-style tool use](toolformer-tool-use.md) is one way to teach the
model *when* those APIs help without task-specific wiring. Schick et al.’s
canonical five: QA (Atlas), calculator (+−*/), BM25 Wikipedia search,
NLLB→English MT, and a zero-arg calendar — all text I/O with a few demos.

**Write actions** change data sources rather than only reading them: mutating
tables, sending email, initiating transfers. They unlock full workflow
automation, but blast radius scales with autonomy — models are probabilistic
and often wrong, so do not book travel or merge PRs merely because the user
mentioned wanting to. Treat write access like production credentials for a
junior operator — trust must be earned through sandboxing,
[human approval gates](human-approval-gates.md), and security measures, not
assumed because the model is capable.
