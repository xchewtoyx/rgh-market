---
type: concept
title: Documentation Targets Ineptitude, Not Ignorance
description: Distinguishing failures caused by not applying known knowledge consistently from failures caused by not having the knowledge at all, to scope what operational documentation can actually fix.
sources:
  - title: "The Checklist Manifesto: How to Get Things Right"
    resource: "The Checklist Manifesto (Gawande), Introduction"
---

Human failure in operating a system falls into three distinct categories, and they call for entirely different remedies:

- **Necessary fallibility**: Failure caused by an absolute limit — physical, informational, or conceptual — that no amount of process or documentation can overcome.
- **Ignorance**: Failure because the knowledge needed doesn't yet exist anywhere, for anyone. The remedy is research, investigation, or building new expertise — not better documentation of what's already known.
- **Ineptitude**: Failure where the necessary knowledge exists and is known to someone, but isn't applied consistently or correctly in the moment — because it was forgotten, skipped under pressure, or never reached the person who needed it. This is the only one of the three that operational documentation (runbooks, checklists, playbooks) can actually fix.

## Why This Distinction Matters for Handover

Runbooks and checklists are, specifically, an ineptitude-class remedy: they exist to make sure knowledge that already exists gets applied reliably, not to generate knowledge that doesn't exist yet. This gives a useful diagnostic when a documented procedure keeps failing after handover:

- If operators are skipping or misapplying a known-correct step, the fix is better [runbook and checklist design](runbook-checklist-design.md) — that's an ineptitude problem.
- If operators are consistently following the documented procedure and it still isn't working, more checklist discipline won't help — that's a sign the documentation is encoding stale or incomplete knowledge (a documentation-maintenance problem, see [Documentation Maintenance Workflows](documentation-maintenance-workflows.md)) or the situation has drifted into genuinely unknown territory that needs investigation, not a checklist.

Misdiagnosing an ignorance-class or necessary-fallibility-class failure as an ineptitude problem — and responding by adding more checklist items or demanding stricter compliance — will not fix it, and can add noise that makes the checklist less effective at the ineptitude failures it's actually good at catching.
