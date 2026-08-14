---
type: concept
title: Temporary Access
description: >
  Time-bounding grants limits the blast radius of an authorization decision
  and reduces ambient authority when fine-grained controls aren't available.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 5"
---

# Temporary Access

Granting access that expires limits the risk of any single authorization
decision. It is especially useful when fine-grained per-action controls
don't exist yet but you still want the least privilege the available
tooling can express — a pragmatic stepping stone toward full
[least privilege](least-privilege.md).

Grant it either structurally (during on-call rotations, expiring group
memberships) or on demand (explicit user request), optionally gated by
[multi-party authorization](multi-party-authorization.md) or a
[structured justification](structured-justification.md).

Side benefits beyond risk reduction:

- **A natural audit point**: clear logging of exactly who had access at any
  given time (see [audit log design](audit-log-design.md)).
- **Prioritization data**: records of where temporary access is requested
  show which workflows still need safer APIs, so you can reduce those
  requests over time.
- **Less ambient authority**: the same reason administrators prefer `sudo`
  over operating as root — when you accidentally issue the
  delete-everything command, the fewer permissions you hold, the better.

"No permanent access" is the appropriate standing policy for the most
sensitive [access classifications](access-classification-by-risk.md).
