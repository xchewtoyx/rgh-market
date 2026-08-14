---
type: concept
title: Implicit Field Mask Inference
description: >
  Deriving an update field mask from the PATCH body by treating every set field
  path as selected, with explicit null distinct from omission.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 8"
---

When no explicit [field mask](field-mask.md) accompanies a standard update,
infer one from the request body: walk the object recursively; for every field
whose value is **set** (not `undefined`), add its dotted path to the mask.

`PATCH {"description": "New description"}` → mask `["description"]` — only
that field changes.

`PATCH {"description": null}` → mask `["description"]` with value **null** —
explicitly clears the field; this is not the same as omitting `description`,
which would leave it untouched under inference rules.

This ties directly to [missing versus null policy](missing-versus-null-policy.md).
Dynamic maps add a third state — absent key — handled by
[field mask map key removal](field-mask-map-key-removal.md).
