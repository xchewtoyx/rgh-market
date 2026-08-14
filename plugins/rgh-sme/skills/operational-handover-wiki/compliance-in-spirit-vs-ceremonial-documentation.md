---
type: concept
title: Compliance in Spirit vs. Ceremonial Documentation
description: Satisfying the actual knowledge, traceability, and control needs behind a compliance framework's documentation requirement instead of producing documents that only exist to check the audit box.
sources:
  - title: "Living Documentation"
    resource: "Living Documentation (Martraire), ch. 13"
  - title: "Continuous Delivery"
    resource: "Continuous Delivery (Humble, Farley), ch. 15"
---

Regulatory or process frameworks (e.g. ITIL, SOX, HIPAA) often mandate documentation as an audit requirement. The easy response is to produce ceremonial documents whose only purpose is passing the audit — written once, rarely read, and disconnected from how the system is actually operated. This satisfies the letter of the requirement while providing none of its intended value, and adds exactly the kind of stale, untrustworthy documentation that erodes confidence in the rest of the wiki.

## Compliance in Spirit

Instead, identify what the framework's documentation requirement is actually trying to guarantee — typically some combination of:

- **Knowledge**: Someone (not necessarily the original builder) can explain how the system works and why.
- **Traceability**: A decision, change, or incident can be traced back to who made it, when, and why.
- **Control**: There is a real mechanism ensuring changes go through appropriate review or approval, not just a record claiming one exists.

Then satisfy that underlying need using documentation that is genuinely useful for operating and maintaining the system — the same runbooks, decision logs, and change-control records this domain already produces for operational reasons. A single well-maintained set of operational documentation, kept current because it's actually used, satisfies both the audit requirement and the operational need. A separate ceremonial document produced only for the auditor satisfies neither well, and doubles the maintenance burden.

Traceability and control needs in particular can sometimes be satisfied by a mechanism rather than a document at all: an automated deployment pipeline that stamps every release with its source commit, approver identity, and passing test results produces a tamper-proof audit trail as a byproduct of normal operation, which can satisfy a separation-of-duties or change-approval requirement more reliably than a manual sign-off form ever does — see [Automated Guardrails for Safe Changes](automated-guardrails-for-safe-changes.md) for the same logic applied to safety rather than compliance.

## Applying This During Handover

When a handover includes compliance obligations (see the regulatory exposure criteria in [Launch vs. Handoff Readiness Reviews](launch-vs-handoff-readiness-reviews.md)), check whether the compliance documentation and the operational documentation are the same artifacts or two separate, divergent sets. If they've diverged, that's a sign the compliance documentation has become ceremonial — reconciling them into one genuinely useful set is usually better than maintaining both.
