---
type: concept
title: Peer Review as Change Control
description: >
  Requiring a non-author team member to review and approve a change in
  version control is the only change-approval method DORA research found
  to correlate positively with both tempo and stability.
sources:
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 7"
  - title: "Serverless Design Patterns and Best Practices"
    resource: "Serverless Design Patterns and Best Practices (Zambrano), ch. 9"
---

# Peer Review as Change Control

Of the four change-approval paradigms DORA studied, peer review — at least
one non-author team member reviewing and approving a change in version
control before merge, e.g. a pull request approval — is the only one that
correlates positively with *both* delivery tempo and stability. Pair
programming on the change can satisfy the same intent when two engineers
shared authorship. See [change approval board pathology](change-approval-board-pathology.md) for
why the alternative (external CAB review) fails on both dimensions.

Peer review works where external CAB review doesn't because the reviewer
has the contextual system knowledge the author has, catching real defects
without introducing a queue, a handoff, or a separate approval authority
disconnected from the code.

Peer review is also the mechanism that satisfies regulatory
[segregation of duties](segregation-of-duties-via-pipeline-audit-trail.md)
requirements without a CAB.
