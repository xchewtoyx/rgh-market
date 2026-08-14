---
type: concept
title: Security Architecture View
description: >
  Documenting security as its own cross-cutting view of the architecture,
  since its relevant elements are otherwise scattered thinly across every
  structural diagram and easy to lose track of as a whole.
sources:
  - title: Software Architecture in Practice, 4th Edition
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 22"
---

# Security Architecture View

Ordinary architecture documentation is organized by structure — module
views, runtime component-and-connector views, deployment views — each
useful for its own purpose but each showing only a thin slice of the
system's security posture. A single sign-in flow might touch a UI module,
an auth service component, a credential store, and a deployment boundary,
with no one structural diagram showing how they combine into "how this
system authenticates." A **security view** is a deliberately cross-cutting
document assembled by pulling the security-relevant pieces out of every
other view and presenting them together, purpose-built for a security
[design review](security-design-review.md) or audit rather than for
construction.

What belongs in it: which components play a security role and how they
communicate; where security-relevant data is stored (credentials, keys,
audit records); environmental/physical security measures the software
depends on; the operation of security protocols in use; the points where
humans interact with the security machinery (approval prompts,
[breakglass](breakglass.md), credential entry); and how the system is
meant to detect and respond to a threat or vulnerability once one appears.

This is the documentation counterpart to
[attack trees](attack-trees.md): the attack tree tells you which scenarios
need a response, and the security view is where an agent can check, in
one place, whether the components that should provide each response
actually exist and are wired together — rather than reconstructing that
picture by cross-referencing every structural diagram in the system by
hand.
