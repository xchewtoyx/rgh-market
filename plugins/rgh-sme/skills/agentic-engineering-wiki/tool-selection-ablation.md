---
type: concept
title: Tool Selection Ablation
description: >
  Empirically size and prune an agent's tool inventory by measuring performance
  with and without each tool and replacing chronically misused ones.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
---

More tools do not automatically mean a better [LLM agent](llm-agent.md).
Inventory design needs experimentation:

- Compare performance across candidate [tool inventories](tool-inventory.md).
- Run ablation: remove a tool and measure the drop; if none, drop it.
- Find tools the agent frequently misuses; if prompting and finetuning cannot
  fix misuse, replace with a simpler tool.
- Plot tool-call distributions to see real usage patterns.

Different tasks and different models prefer different tools — a science QA task
may lean on knowledge retrieval while tabular math does not; GPT-4-class models
may diversify tool choice more than weaker ones. Also evaluate how easily a
framework lets you add tools as needs evolve, and whether frequent tool pairs
should become composite tools or entries in a [skill library](skill-library.md).
