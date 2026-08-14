---
type: concept
title: Shallow Modules
description: >
  A shallow module's interface is complicated relative to the functionality
  it actually provides, so it doesn't meaningfully help fight complexity —
  the benefit of hiding internals is negated by the cost of learning and
  using the interface itself.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 4"
---

**Red flag: shallow module.** A linked-list class is a mild example: insert
and delete are only a few lines each, so wrapping them in a class interface
barely reduces anything a caller has to know. A sharper real example, from a
student project:

```java
private void addNullValueForAttribute(String attribute) {
    data.put(attribute, null);
}
```

This adds a new thing to learn (the method's existence and name) without
hiding any meaningful complexity — callers still effectively need to know
about the underlying `data` map. Proper documentation for it would run longer
than its body, and calling it takes more keystrokes than just writing
`data.put(attribute, null)` directly. It is pure interface cost with no
[depth](deep-modules.md) to offset it.

Small modules tend to be shallow, which is why "classes and methods should be
small" as an unqualified rule is dangerous — see [classitis](classitis.md) for
what happens when that rule is followed to its logical extreme.
