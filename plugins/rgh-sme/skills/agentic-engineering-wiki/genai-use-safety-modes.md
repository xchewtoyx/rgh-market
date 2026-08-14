---
type: concept
title: GenAI Use Safety Modes
description: >
  Rank GenAI collaboration from checking your work up through independent
  complex problem-solving — autonomy rises with risk and oracle demand.
sources:
  - title: Taking Testing Seriously
    resource: "Taking Testing Seriously (Bach & Bolton), ch. 7"
---

Bach & Bolton rank GenAI use by safety:

1. **Check your work** — ask for critique of an answer you already hold (safest).
2. **Assist solving a problem** — draft a strategy or draft code while you stay
   alert.
3. **Independently perform a specific procedure** with verifiable behaviours —
   needs agentic capability; significant risk.
4. **Independently solve a complex problem** — highest risk; weakest oracles.

Map this onto [progressive agent architecture](progressive-agent-architecture.md)
and [human approval gates](human-approval-gates.md): climb the ladder only when
you have offline oracles and blast-radius limits for the new autonomy. Wishful
prompt engineering without a stable evaluation contract leaves modes 3–4
untestable — pair with [genai radical fragility](genai-radical-fragility.md)
and [offline prompt evaluation](offline-prompt-evaluation.md).
