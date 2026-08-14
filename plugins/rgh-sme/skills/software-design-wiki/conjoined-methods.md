---
type: concept
title: Conjoined Methods
description: >
  Conjoined methods are pieces of code that have been physically separated
  but can only be understood together — a red flag that a split (or a
  separation) was a mistake.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 9"
---

**Red flag: conjoined methods** — "It should be possible to understand each
method independently. If you can't understand the implementation of one
method without also understanding the implementation of another, that's a
red flag." The pattern generalizes beyond methods: any two pieces of code
that are physically separated but can only be understood together exhibit
the same problem.

Worked counter-example: a student project pulled error-logging calls out
into a dedicated `NetworkErrorLogger` class with methods like
`logRpcOpenError(...)`, invoked from call sites such as:

```java
try {
    rpcConn = connectionPool.getConnection(dest);
} catch (IOException e) {
    NetworkErrorLogger.logRpcOpenError(req, dest, e);
    return null;
}
```

This was pure added complexity with no benefit: the logging methods were
[shallow](shallow-modules.md) (often a single line, needing more
documentation than code), each invoked at exactly one call site, and tightly
coupled to that one site — a reader had to flip between the invocation and
the logging method in both directions to understand either one. The correct
fix was to inline the logging statement directly at the point of detection,
eliminating the extra interface entirely.

This is the sharpest illustration of why
[separation has a real cost](better-together-or-apart.md): splitting related
code apart is only good when the pieces are genuinely independent enough to
be read on their own.
