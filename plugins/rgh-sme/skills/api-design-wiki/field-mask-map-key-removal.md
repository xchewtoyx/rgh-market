---
type: concept
title: Field Mask Map Key Removal
description: >
  Deleting a dynamic map entry by naming its path in an explicit field mask
  while keeping that key absent from the PATCH body.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 8"
---

Static nested fields have two states: a value or `null`. [Map fields](map-field-bounds-and-defaults.md)
add a third: **absent key** (the key is not in the map).

[Implicit field mask inference](implicit-field-mask-inference.md) handles setting
or nulling map entries (`{"settings": {"test": "new value"}}` or
`{"settings": {"test": null}}`). **Removing a key entirely** cannot use
inference alone — JSON has no `undefined` literal for "delete this key."

Send an **explicit field mask** naming the key to remove with an **empty or
key-free body**:

```
PATCH /chatRooms/1?fieldMask=settings.test
Content-Type: application/json

{}
```

The mask names `settings.test`; the body omits it → server treats input as
undefined and deletes the key.

Implementation must check **presence in the input document**, not default
missing branches to placeholders (for example Python `input.get('settings',
{}).get('test')` conflates absent key with explicit null).
