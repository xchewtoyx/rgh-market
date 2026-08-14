---
type: concept
title: Unused Permission Revocation
description: >
  Automatically revoking access that goes unused over a defined window
  closes latent privilege accumulation without requiring every grant to be
  time-bounded upfront.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 10"
---

# Unused Permission Revocation

Access grants accumulate over time even in organizations that grant
carefully at the point of request: roles change, projects end, and a
permission that was genuinely needed six months ago quietly becomes a
standing hole nobody remembers to close. The complementary control to
granting narrowly is monitoring what's actually *used* and removing what
isn't — for example, automatically revoking a data-warehouse role from an
analyst who hasn't queried it in six months, with a simple ticket-based
path to re-request it if the need resurfaces.

This differs from [temporary access](temporary-access.md) in when the
constraint applies: temporary access bounds a grant's lifetime at the
moment it's issued, while unused-permission revocation continuously
re-evaluates *already-standing* access against actual behavior, catching
exactly the grants that were never given an expiry because nobody could
predict how long they'd be needed. Driving this requires the same
[audit log](audit-log-design.md) and access-monitoring data that
[testing least privilege](testing-least-privilege.md) and
[access classification by risk](access-classification-by-risk.md) already
depend on — usage-based revocation is a mechanical consumer of the same
"who has access to X, and are they using it" data those practices require
you to be able to answer.
