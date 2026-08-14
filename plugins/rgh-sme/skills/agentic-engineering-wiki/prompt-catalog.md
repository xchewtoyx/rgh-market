---
type: concept
title: Prompt Catalog
description: >
  Version prompts independently of application code with metadata so shared
  prompts can be pinned, searched, and evolved without silent force-updates.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 5"
---

Separate prompts from code (for example a `prompts` module) for reusability,
independent testing, readability, and SME collaboration. As prompt count grows,
attach metadata: model, created date, application, creator, endpoint, sampling
parameters, input/output schemas. Dedicated `.prompt` formats (Dotprompt and
similar) package YAML frontmatter with the prompt body.

Git-versioning prompts only beside app code force-updates every consumer on
change. A separate **prompt catalog** versions each prompt independently,
supports search, and can track which applications depend on which version —
notifying owners on updates. This is the maintenance surface for
[prompt engineering](prompt-engineering.md) and
[system prompt architecture](system-prompt-architecture.md) as models and
requirements change.
