---
type: concept
title: Missing Versus Null Policy
description: >
  Wire conventions for absent fields, explicit null, and default application
  on create and update operations.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 5"
---

APIs must define three states for optional fields:

- **Missing** — key absent from the message.
- **Null** — key present with null value.
- **Default** — server applies documented default when missing (often on create
  only).

The same question recurs for every primitive and collection type: should
`{color:""}` , `{color:null}`, and `{color}` omitted resolve to the same
meaning? Serialization libraries will not converge without an explicit API
decision — the ambiguity is not JSON-specific (Protocol Buffers exhibits similar
confusion).

On **update**, distinguish "leave unchanged" (omit field) from "clear/set null"
(explicit null) from "set value." Mixing semantics across methods breaks
[backward compatibility](backward-compatibility-policy.md).

[Map fields](map-field-bounds-and-defaults.md) handle null vs `{}` cleanly;
[atomic list fields](atomic-list-field.md) treat `[]` as meaningful, complicating
defaults. [Boolean fields](boolean-field-conventions.md) and
[numeric fields](numeric-field-bounds.md) face zero-value traps when the format
has no true null for primitives. [String fields](string-field-bounds-and-encoding.md)
sometimes use empty string or a `"default"` sentinel — document per field.

State explicitly in the [API description](api-description.md); enforce in
validation (`validateOnly` dry runs when offered).
