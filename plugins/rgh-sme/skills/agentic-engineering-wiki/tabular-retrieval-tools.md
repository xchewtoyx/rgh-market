---
type: concept
title: Tabular Retrieval Tools
description: >
  Answer structured-data questions via text-to-SQL, execution, and generation —
  treating schema selection and SQL runners as agent tools.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
---

Tabular questions ("units of Fruity Fedora sold in the last 7 days") are not
solved by dumping table text into context. The workflow is: (1) text-to-SQL from
query plus schema, (2) SQL execution, (3) natural-language generation from the
result. If many schemas cannot fit in context, first predict which tables to use.

This is the bridge from classic [RAG](retrieval-augmented-generation.md) into
the agentic pattern: retrievers and SQL executors are tools in the
[tool inventory](tool-inventory.md). Write-capable SQL raises
[indirect prompt injection](indirect-prompt-injection.md) and
[human approval gates](human-approval-gates.md) concerns — treat generated SQL
like any other write action under
[agent system-level defenses](agent-system-level-defenses.md).
