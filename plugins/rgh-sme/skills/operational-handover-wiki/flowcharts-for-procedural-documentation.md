---
type: concept
title: Flowcharts for Procedural Documentation
description: A visual flowchart of a multi-step operational procedure is often less ambiguous and easier to follow correctly than the equivalent text-based, step-numbered writeup.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements (Leffingwell), ch. 18"
---

A long procedure — provisioning a new deployment, standing up a new environment, working through a multi-stage cutover — can always be written as a numbered list of steps. But once the procedure has any real branching (skip step 4 if condition X, loop back to step 2 if the check fails, hand off to a different owner partway through), a flat numbered list stops conveying the actual shape of the work. The reader has to hold the branching logic in their head while reading linear prose that wasn't designed to represent it.

A **flowchart or activity diagram** of the same procedure makes the control flow the thing you look at directly, rather than something you have to reconstruct from cross-references between numbered steps ("if this fails, go back to step 2"). The same content is being communicated either way — the diagram doesn't add information the prose lacks — but the visual form is easier to follow correctly precisely because branches, loops, and parallel paths are things flowcharts are built to show, and things prose has to work around.

## When it's worth the extra authoring effort

Not every runbook needs a diagram; a genuinely linear procedure is better left as a numbered list, since drawing a straight line as a flowchart adds a diagram to maintain without adding clarity. Reach for a flowchart specifically when the procedure has enough real branching, looping, or handoff points that a reader following numbered prose would have to jump around the document to trace a single path through it. This overlaps with, but is a different tool from, the checklist format described in [Runbook and Checklist Design](runbook-checklist-design.md): a checklist is the right shape for a sequence of steps that must all happen (or be verified); a flowchart is the right shape once "which step happens next" genuinely depends on a decision made along the way.
