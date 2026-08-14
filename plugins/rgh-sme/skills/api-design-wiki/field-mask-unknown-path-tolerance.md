---
type: concept
title: Field Mask Unknown Path Tolerance
description: >
  Silently ignore field-mask paths that do not match the current schema so
  clients survive API evolution without hard errors.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 8"
---

Do not error when a [field mask](field-mask.md) names a field absent from the
current resource or request. APIs evolve — fields are added and removed — so a
client's mask may reference an older or newer schema.

Treat structures as dynamic: unmatched mask entries behave as `undefined`;
retrieval and update proceed without failure. This pairs with documented
[backward compatibility](backward-compatibility-policy.md) expectations when
fields disappear from responses.
