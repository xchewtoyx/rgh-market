---
type: concept
title: Delivery-Pipeline Separation of Duties
description: >
  Mandatory peer review plus an automated deployment pipeline that alone
  can touch production satisfies regulatory separation-of-duties
  requirements without a human change-approval board.
sources:
  - title: Accelerate
    resource:
      "Accelerate: The Science of Lean Software and DevOps (Forsgren,
      Humble, Kim), ch. 7"
  - title: Continuous Delivery
    resource:
      "Continuous Delivery: Reliable Software Releases through Build,
      Test, and Deployment Automation (Humble, Farley), ch. 15"
---

# Delivery-Pipeline Separation of Duties

Regulated environments (PCI DSS, SOX, HIPAA, FISMA) require that the
person who authors a change not be the same person who can unilaterally
put it into production. The default assumption is that this needs a human
approval body — a Change Advisory Board reviewing changes before release —
but a CAB reviewing code without the author's context is a poor
substitute for separation of duties in practice: it adds a queue and a
paper trail without independently verifying the change is safe.

Two mechanisms satisfy the actual regulatory requirement without a CAB:

- **Mandatory peer review**: at least one team member other than the
  author reviews and approves every change in version control before it
  can merge.
- **Deployment exclusively through an automated pipeline**: no human has
  standing ability to push a change to production directly; only the
  pipeline can, and only for changes that passed review and tests. This
  is the delivery-side instance of
  [verify artifacts, not just people](verify-artifacts-not-people.md) —
  the pipeline is the choke point, and it enforces the separation
  structurally rather than trusting an approver's judgment in the moment.

Together these produce the record an auditor actually needs: an immutable
trail of commit SHA, author identity, reviewer identity, automated test
results, binary artifact checksum, and deploy timestamp for every
production change — see
[audit log design](audit-log-design.md) on why this granular,
machine-generated record is worth more than a human sign-off. Because the
pipeline itself generates the trail, compliance evidence is a byproduct of
normal delivery rather than a separate paperwork exercise.

This is separation of duties on the *human change-authorship* axis —
distinct from [role separation](role-separation.md), which separates
service-account identities so that compromising one job's credentials
doesn't grant another job's access. A system can have one without the
other: strong peer review with a shared, overprivileged service account
still lets a compromised account bypass the human control entirely.
