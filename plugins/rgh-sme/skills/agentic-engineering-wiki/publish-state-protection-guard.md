---
type: concept
title: Publish-State Protection Guard
description: >
  Once an agent's own end-state check passes, intercept later destructive
  commands against that verified output at the tool level so a "tidy up" pass
  cannot erase what was just proven correct.
sources:
  - title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
    resource: "Agentic Harness Engineering (Lin, Liu, Pan, et al.), App. C.1–C.2"
---

A recurring long-horizon agent failure looks nothing like getting the task
wrong: the agent produces a correct deliverable, runs a self-check that
confirms it, and then destroys its own success on the way out — a sweeping
cleanup command, a "leave a clean repo for grading" reset, deleting scratch
files that turn out to include the actual output. A prompt rule telling the
agent not to do this ("don't destroy verified state") helps but is not
sufficient on its own: it is advisory, and an agent under time or context
pressure can simply forget it — see
[harness component-level selection](harness-component-level-selection.md) for
why an advisory fix is the wrong strength for an enforcement problem.

The **publish-state protection guard** closes the gap at the tool level
instead of the prompt level. Installed inside the shell/execution tool itself:

1. After a successful evaluator-style final check, parse the acceptance
   command for the file paths and roots it referenced, and record those as
   **protected**.
2. Intercept later commands that would delete a protected output or reset a
   protected root **before execution**, returning a targeted error that names
   the at-risk protected target instead of silently letting the command
   through.
3. Allow an explicit override token (e.g. `ALLOW_POST_SUCCESS_RESET`) to
   downgrade the block to a warning — forcing the agent to consciously
   re-attach the token and, ideally, revalidate before submitting again,
   rather than making protected-state destruction impossible outright.

Extending what counts as "protected" matters as much as the initial guard:
script entrypoints and other files a final check explicitly references need
the same protection as the output files themselves, or an agent can route
around the guard by re-running or rewriting the *generator* of a verified
output rather than the output file directly. And the override token itself
needs a ceiling — a guard that can be fully bypassed by attaching one token
string is only a speed bump; escalating live, already-verified deliverables
and roots to a **hard block** that the override token cannot downgrade closes
that residual loophole, while non-critical protected state can still allow
the override-and-revalidate path.

This is a general ACI guardrail pattern for any long-horizon agent with write
access to its own output: verified state is a promise, and only an
execution-time intercept — not a prompt reminder — can make breaking that
promise something the harness prevents rather than something it merely
discourages.
