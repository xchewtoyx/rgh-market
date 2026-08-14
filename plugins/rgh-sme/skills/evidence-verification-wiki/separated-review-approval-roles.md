---
type: concept
title: Separated Review Approval Roles
description: >
  Splitting independent review into distinct approval bits — correctness, ownership
  fit, and standards conformance — so each check can be performed by the right reviewer.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 9"
---
# Separated Review Approval Roles

Large-scale review workflows often require **multiple distinct approvals** before a change is accepted. At Google, three permission bits combine flexibly:

1. **LGTM (looks good to me)** — another engineer attests the change is comprehensible and does what the author claims (a correctness/comprehension check).
2. **Owner approval** — a code owner for that part of the tree attests the change is appropriate for that area (gatekeeping long-term maintainability and scope).
3. **Readability approval** — a language-readability reviewer attests the change follows language style and best practices.

One person may satisfy all three on small teams; larger or less experienced authors may need a peer LGTM first, then owner/readability sign-off focused on maintainability questions ("Will this be easy to maintain? Does it add technical debt? Do we have expertise to keep it?").

## Why Separation Scales Review
Splitting roles lets reviewers specialize, avoids forcing one reviewer to cover every dimension at once, and allows an early correctness LGTM from a teammate before seeking owner sign-off — a staged verification path rather than a single bottleneck.

## Verification Action

When a document cites "approved" or "reviewed," identify **which approval roles** were actually satisfied. LGTM alone does not prove ownership fit or standards conformance; owner approval alone does not prove another engineer verified correctness. Missing role separation on high-stakes changes is a process gap worth flagging — compare [evidence triangulation](evidence-triangulation.md) for why one verification pass rarely covers every failure mode.
