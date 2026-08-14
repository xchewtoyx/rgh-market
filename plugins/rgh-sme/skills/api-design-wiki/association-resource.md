---
type: concept
title: Association Resource
description: >
  A first-class resource representing a many-to-many join with its own metadata,
  created and deleted like any other resource.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 14"
---

Many-to-many relationships — users and groups, students and courses — map to a
**join table** in storage. Expose those rows as a third **association resource**
(for example `Membership` joining `User` and `Group`) aligned one-to-one with
schema: three resources, not inlined member lists on parent resources.

**Create** joins; **delete** leaves. **Get/update** matter when the association
carries metadata (join time, role, `expireTime`) — otherwise list filters may
suffice.

**Naming:** domain terms when obvious (`CourseEnrollment`); otherwise
`Membership` or `Association`, optionally qualified (`CourseMembership`).

**Standard methods** follow the [standard method contract](standard-method-contract.md)
exactly — memberships are ordinary resources.

**Uniqueness:** only one association per pair — duplicate create (same user +
group, new id) → **409 Conflict**, not just duplicate-id conflicts.

**Read-only association endpoints:** the two referenced ids are **output only**
on update — change membership by delete + create, not by rewriting `userId` on
an existing row (silent ignore on update, like [soft deletion](soft-deletion.md)
flags).

**Referential integrity** when a joined resource is deleted: prefer **restrict**
(412) or **do nothing** (dangling pointer) — avoid cascade or set-null that
trigger mass writes across huge association sets.

See [association alias list methods](association-alias-list-methods.md) for
convenience subcollections. Trade-off: more surface area vs flexible relationship
metadata; group facts and member lists stay separate calls (`GetGroup` vs
`ListGroupUsers`).
