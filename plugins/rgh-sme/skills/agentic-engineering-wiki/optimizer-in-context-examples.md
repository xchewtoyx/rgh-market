---
type: concept
title: Optimizer In-Context Examples
description: >
  Show the textual optimizer worked examples of desired variable properties so
  rewrites match target style, format, or quality traits.
sources:
  - title: "TextGrad: Automatic Differentiation via Text"
    resource: "TextGrad (Yuksekgonul et al.), Appendix B"
---

Besides gradients and constraints, TextGrad can condition
[textual gradient descent](textual-gradient-descent.md) on **in-context
examples** of good (or illustrative) variable values: “base on the following
examples when modifying the {role_description}” with an `<EXAMPLES>` block.
Authors claim this helps the optimizer implement desired properties of the
optimized variable.

Use sparingly: examples compete for context with
[textual optimizer momentum](textual-optimizer-momentum.md) and batch
feedback. Prefer short exemplars that show format and reasoning habits under
[optimization variable role description](optimization-variable-role-description.md),
not full task solutions that invite copying. Validate that examples do not
leak eval items under
[eval observation anti-leakage](eval-observation-anti-leakage.md) when used
offline.
