---
type: concept
title: Human–Model Demo Interface Parity
description: >
  Collect demonstrations through the same action/observation surface the model
  will use, exposing only deliberate exceptions such as memory summaries.
sources:
  - title: "WebGPT: Browser-assisted question-answering with human feedback"
    resource: "WebGPT (Nakano et al.), Appendix C.1"
---

When humans produce trajectories for imitation or preference labels, give them
the **same information and actions** as the deployed agent ACI — otherwise
demos encode affordances the model never sees. WebGPT’s GUI rule: labelers
share the model’s view, with explicit exceptions (past-action summary shown to
the model only because it has no memory; multi-step scrolls merged for humans
while the model issues repeated single scrolls).

Parity keeps demonstration data aligned with
[lm-oriented web observations](lm-oriented-web-observations.md) and the live
[agent-computer interface](agent-computer-interface.md). Document every
exception in the harness config under
[configurable ACI harness](configurable-aci-harness.md) so training and eval
do not silently diverge. This is collection-time ACI design, not the RLHF
reward-model pipeline itself.
