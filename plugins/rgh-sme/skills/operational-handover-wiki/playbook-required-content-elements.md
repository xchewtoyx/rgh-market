---
type: concept
title: Playbook Required Content Elements
description: An operational playbook must layer business judgment (when, who to notify, what to verify) on top of the technical how-to, and should be authored jointly by developers and operators.
sources:
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 2"
---

A playbook is not simply the technical steps for performing an operation — it is developer documentation with an additional layer of operational judgment on top. Four kinds of content need to be present for a playbook entry to be usable by someone who wasn't involved in building the procedure:

- **How**: the technical steps to carry out the procedure (e.g., the exact commands or control-panel actions for a failover).
- **When**: the conditions under which this procedure should be invoked at all, as opposed to some other response.
- **Who to notify**: which teams or individuals need to know the procedure is being run, before and after.
- **What to check**: which dependencies, preconditions, or downstream systems must be verified both before starting (is it safe to proceed) and after finishing (did it actually work).

The last point generalizes into a rule that applies to every documented procedure, not just failovers: every step should include a way to verify success or failure, so an operator following the playbook doesn't have to guess whether the procedure actually worked.

## Joint Authorship

A playbook that covers real operational scenarios can't be written by either side alone: operations staff know which scenarios actually happen in practice and what business context matters when they do, but only the developers know every code-level error condition and the supporting tools available to diagnose or resolve it. Treat playbook writing as a joint deliverable between the team that built the system and the team that will run it, not a document ops writes unassisted from observed behavior or devs write unassisted from the code.

## Relationship to Upstream Dependency Contracts

The "who to notify" element covers teams downstream of a procedure; see [Upstream Dependency Contract](upstream-dependency-contract.md) for the mirror-image practice of documenting what's owed to you by teams and systems your own procedures depend on.

## Relationship to Communicating Intent

The four elements here cover what a procedure entry must contain to be *executable*; they don't by themselves cover what a recipient needs to *improvise correctly* when the actual situation doesn't cleanly match any documented trigger. See [Communicating Intent for Improvisation](communicating-intent-for-improvisation.md) for the complementary practice of stating the purpose behind a procedure, not just its steps and trigger conditions.

## Relationship to Checklist Ergonomics

This note describes what content a playbook must contain; [Runbook and Checklist Design](runbook-checklist-design.md) describes how to format and structure that content so it can be executed accurately under pressure once it exists. A playbook entry that has all four content elements above but is formatted as a wall of undifferentiated prose still fails under stress — both concerns are necessary.

Writing out a procedure to this level of explicit detail also has a side effect beyond making it followable: it exposes exactly which steps are mechanical and repeatable versus which genuinely require human judgment, making the playbook a stepping stone toward [automating the procedure it describes](reducing-documentation-need-through-system-design.md) rather than an end state in itself.
