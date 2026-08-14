---
type: concept
title: Runbook and Checklist Design
description: Designing operational checklists and runbooks that can be executed accurately under stress without causing cognitive overload.
sources:
  - title: "The Checklist Manifesto: How to Get Things Right"
    resource: "The Checklist Manifesto (Gawande), ch. 6"
---

When documenting operational procedures (such as runbooks and playbooks) meant to be followed correctly under pressure or by an unfamiliar operator, the design of the document must account for human cognitive limits under stress. This note covers how to format and structure that content; for what content a playbook needs to contain in the first place (technical steps plus the business judgment of when to invoke it, who to notify, and what to verify), see [Playbook Required Content Elements](playbook-required-content-elements.md).

## Failure Modes Checklists Guard Against

Checklists exist to counter two distinct ways experienced operators fail at routine tasks under complexity:

- **Memory and attention degradation**: Focus and recall fail under pressure, noise, or fatigue — especially dangerous in all-or-none processes, where omitting a single step invalidates the entire procedure.
- **Complacency and step-skipping**: Operators intentionally bypass a step because "it rarely matters" or "has never failed before," exposing the system to rare but severe tail-risk failures.

Design every checklist item to guard against one of these two modes specifically, rather than as a generic reminder — see [Checklist Compliance Precondition Audit](checklist-compliance-precondition-audit.md) for a third, non-cognitive reason compliance can fail even when the checklist itself is well designed.

## Execution Modes

Checklists and runbooks should be explicitly designed for one of two execution modes:

- **DO-CONFIRM**: Operators perform tasks from memory and experience independently, then pause at a designated threshold to verify that all critical steps were completed. This is ideal for routine, highly practiced workflows.
- **READ-DO**: Operators execute steps sequentially as they read them from the list, acting like a recipe. This is appropriate for rare, complex, or high-risk workflows where deviation is dangerous.

## Design Rules for Reliability

To ensure high compliance and reduce errors, checklists must adhere to strict ergonomics:

1. **Focus on "Killer Items"**: Target **5 to 9 items** per checklist or pause point (the limit of working memory). Do not attempt to document every single trivial detail. Instead, focus exclusively on the critical safety steps that are easily forgotten under pressure and would cause system failure if omitted.
2. **Strict Time Limits**: A checklist execution window or pause point should take no more than **60 to 90 seconds** to complete. If a checklist is too long, operators will shortcut it or miss checks due to distraction.
3. **Visual Ergonomics**: Keep the layout clean, uncluttered, and on a single page if possible. Use a clear sans-serif font and mixed upper/lowercase text for readability under poor lighting or high stress.
4. **Mandatory Staging/Simulation Testing**: The first draft of any checklist or runbook will fail. Every procedure must undergo iterative empirical testing in staging, disaster simulation exercises, or dry runs prior to being deployed as a standard operational asset. This validates the procedure once before deployment; for rarely-invoked procedures, that confidence still decays afterward unless it is periodically re-earned — see [Rehearsing Rare Procedures with Deliberate Drills](rehearsing-rare-procedures-with-drills.md).
5. **Anchor Against Cognitive Tunneling**: When a checklist covers a complex failure, operators can become so absorbed in the checklist's specific sub-procedure that they lose track of the more fundamental task the procedure exists to serve. Make the first item of a complex diagnostic or recovery checklist an explicit restatement of that fundamental task (e.g. confirming the service is still serving *some* traffic before diving into root-causing why it's degraded), so operators under stress are pulled back to it rather than tunneling into a sub-procedure at the expense of the bigger picture.

For training operators to execute these playbooks under stress, see [On-Call Onboarding and Training](on-call-onboarding-and-training.md). For how to decide which items make the final cut when many candidates compete for the 5-9 slots, see [Checklist Item Selection Trade-offs](checklist-item-selection-tradeoffs.md). For how the checklist should be run once written — who has authority to invoke it and whether it is read silently or aloud — see [Checklist Execution as Team Communication](checklist-execution-as-team-communication.md).

A checklist is the right shape once the steps are known and mostly linear. Once a procedure has enough real branching or looping that a flat list forces the reader to jump around to trace a single path, consider [Flowcharts for Procedural Documentation](flowcharts-for-procedural-documentation.md) instead.
