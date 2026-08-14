---
type: concept
title: Configurable ACI Harness
description: >
  Specify an agent-computer interface as config — prompt templates, command
  files, parsers, history processors, and stateful environment variables.
sources:
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 16–30"
---

A configurable ACI harness separates the multi-turn LM wrapper from a
declarative interface definition so you can iterate
[ACI design principles](aci-design-principles.md) without rewriting the agent
loop. Typical configuration categories:

1. **Prompt templates** — system, instance, next-step (with/without output),
   format-error, and optional demonstration layers of an
   [agent episode prompt stack](agent-episode-prompt-stack.md).
2. **Command files** — bash/Python functions whose signature, docstring, and
   arguments inject into prompts; effects via stdout; globals for stateful UI
   (`CURRENT_FILE`, `WINDOW_SIZE`, …).
3. **Control flow** — `parse_function` for
   [action format enforcement](action-format-enforcement.md); history
   processors that build the literal LM context each turn (for example
   [collapsed observations](collapsed-observations.md)).
4. **Environment variables** — initial shell/ACI state the commands mutate.

Pair with a sandboxed environment module (containerized execution) and episode
logging of trajectories plus final artifacts. Treat the config as the versioned
harness artifact under [harness drift awareness](harness-drift-awareness.md):
changing templates or command docs is an interface change, not a silent prompt
tweak. Prefer this shape when experimenting with new commands, I/O formats, or
context managers atop a fixed [agent-computer interface](agent-computer-interface.md)
abstraction.
