---
type: concept
title: Documentation as Code
description: >
  Treat documentation like code — version-controlled, owned, reviewed,
  and bug-tracked alongside the system it describes — so maintenance
  rides existing engineering workflow instead of a separate, decaying wiki.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 12"
---

Documentation is a tool written in a different language — usually prose rather than a programming language — but it serves the same engineering purpose: enforce consistency, improve clarity, and prevent comprehension errors. Like code, it needs **rules, syntax, and style decisions**; like code, **ownerless documents go stale**.

Treat documentation as code wherever possible:

- Internal policies and style guides to follow
- Storage under **source control** with review history
- **Clear ownership** accountable for maintenance
- **Review on change**, ideally in the same changelist as the code or behavior the document describes
- Issues tracked the same way code defects are
- Periodic evaluation — tested, in some respect, rather than published once and forgotten
- **Freshness and accuracy measured** where tooling allows (still often lags code tooling)

**Canonical documentation** matters when multiple copies of the same guidance exist: designate one primary source, consolidate or deprecate duplicates, and make the canonical copy easy to find — short stable links and docs colocated with the code they describe both help. Without ownership and review, a shared wiki scales into duplicate, obsolete pages nobody can fix: the people who hit bad docs are not the people empowered to repair them, and quality becomes a top developer complaint. Moving important documentation into the same depot and review workflow as code reverses that — engineers feared higher bars would hurt quality; the opposite happened because maintenance became normal engineering work rather than a separate chore.

Most documentation an engineer writes day to day is **code comments** — documentation-as-code is not only about standalone Markdown files but about every supplemental text required to do the job. See [maintaining and deprecating documentation](maintaining-and-deprecating-documentation.md) for freshness metadata and deprecation, and [WHO WHAT WHEN WHERE WHY for documents](who-what-when-where-why-for-documents.md) for where canonical copies should live.
