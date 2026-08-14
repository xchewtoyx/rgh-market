---
type: concept
title: Limits of Information Hiding
description: >
  Information hiding is only appropriate when the hidden information is
  genuinely not needed outside the module — information that callers
  legitimately need, such as tunable configuration, must be exposed instead
  of reflexively hidden.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 5"
---

If external code legitimately needs a piece of information — for example,
configuration parameters that must be tuned differently across different uses
of the same module — hiding it isn't a virtue, it's an obstacle. The better
outcome, when achievable, is for a module to auto-configure itself so the
information doesn't need to be supplied by any caller at all. When that isn't
possible, the design skill is correctly identifying which information truly
must escape the module boundary, rather than applying
[information hiding](information-hiding.md) reflexively to everything and
forcing callers to work around it.
