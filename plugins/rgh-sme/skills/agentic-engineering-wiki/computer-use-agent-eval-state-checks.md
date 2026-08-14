---
type: concept
title: Computer-Use Agent Eval State Checks
description: >
  Verify a computer-use agent by inspecting real backend and application
  state after the fact, not the on-screen confirmation alone, and account for
  its DOM-versus-screenshot interaction trade-off.
sources:
  - title: "Demystifying evals for AI agents"
    resource: "Demystifying evals for AI agents (Anthropic), How to evaluate AI agents"
---

Computer-use agents interact through the same interface a human would —
screenshots, mouse clicks, keyboard input, scrolling — rather than through
APIs or code execution, which is what lets them operate any GUI application
from a design tool to legacy enterprise software with no dedicated
integration. Evaluating one requires actually running it in a real or
sandboxed environment and checking whether the intended outcome happened —
grading on the visible UI response alone is not enough, because a UI can show
a success confirmation without the underlying action having actually taken
effect. This is the same
[outcome vs. transcript](agent-eval-outcome-vs-transcript.md) distinction that
applies to agent evals generally, specialized to the visible surface a
computer-use agent narrates through. Two named benchmarks anchor increasing scope: browser-based task
evaluation using URL and page-state checks for navigation plus backend state
verification for tasks that modify data (confirming an order was actually
placed in the backend, not just that a confirmation page rendered); and
full operating-system control evaluation, whose scripts inspect whatever
artifacts the task actually touched — file system state, application configs,
database contents, UI element properties — after the agent finishes.

**The DOM-versus-screenshot trade-off is itself something to evaluate.**
Browser-use agents can interact via the page's DOM (fast, but token-heavy for
large pages) or via screenshots (slower, but token-efficient for pages whose
full DOM would be expensive to extract). Which is more efficient depends on
the task: extracting readable text from a well-structured page favors DOM
access, while a visually dense page favors a screenshot instead of dumping its
entire DOM. Because getting this choice right materially affects both
latency and accuracy, it's worth building a dedicated eval that checks whether
the agent picked the *right* interaction mode for the page it was on, not only
whether it eventually completed the task — a slow-but-correct completion via
the wrong mode is a real regression a pure task-success metric would miss.
