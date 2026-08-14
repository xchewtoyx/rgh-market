---
type: concept
title: Stable vs. Volatile Documentation
description: >
  Requirements and goals change more slowly than design decisions;
  organizing documentation so volatile material depends on stable
  material, never the reverse, keeps both honest and easier to maintain.
sources:
  - title: Living Documentation
    resource: "Living Documentation: Continuous Knowledge Sharing by Design (Cyrille Martraire), ch. 9"
---

Not all project knowledge needs the same maintenance machinery. Some of it
— goals, vision, stable requirements, core domain concepts — is
"evergreen": it changes slowly enough to justify carefully written prose
that isn't regenerated or continuously synced with code. Other knowledge —
design decisions, implementation detail — is genuinely volatile and needs
to be kept current by different means (see [code as architecture
documentation](code-as-architecture-documentation.md)) or accepted as
likely to drift.

The corresponding rule for organizing documentation: keep stable and
volatile knowledge separate, use names for stable concepts that will
survive redesigns, organize artifacts along the stable axes rather than
around whatever implementation happens to exist today, and make volatile
material *depend on* stable material — never the other way around. A
[requirement](functional-requirement.md) should not reference a specific
implementation detail that might change; a design decision should
reference the requirement that drove it. Concrete artifact types that
belong on the stable side: README files, vision statements, domain vision
statements, goals documents, and impact maps — their value is durable
shared direction, not a changelog of what got built.

Apparent stability should still be tested periodically rather than assumed
forever — see [requirement revisit triggers](requirement-revisit-triggers.md)
for what should prompt that check. This principle is also the basis for
[requirement rationale](requirement-rationale.md) outliving the
[architectural decision](architectural-decision-capture.md) it originally
motivated: the requirement is the stable anchor a design can be
re-evaluated against even after the design itself has changed.
