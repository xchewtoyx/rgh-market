---
type: concept
title: Stack Parameter Design Principles
description: Guidance for keeping stack instance parameters simple, so configurability doesn't undermine the consistency that reusable stacks exist to provide.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 7"
---

A [reusable stack](reusable-stack-pattern.md) needs to vary slightly between instances — a smaller cluster in a development environment, a unique identifier per instance to avoid collisions on infrastructure resources that require globally unique names. But every parameter you add is a knob that can push instances toward inconsistency, which is exactly what [minimizing variation](minimize-variation-principle.md) is meant to prevent — the more configurable a stack is, the harder it is to understand and test the behavior of any given instance.

Practical rules for keeping stack parameters under control:

- Prefer simple parameter types — strings, numbers, maybe lists and key-value maps. Avoid passing complex nested data structures.
- Minimize the number of parameters. Don't add a parameter for something you "might" need later; add it when you actually need it — you can always add one later. See [flexibility mechanism cost justification](flexibility-mechanism-cost-justification.md) for the underlying cost reasoning behind this rule.
- Avoid parameters that act as conditionals producing significantly different infrastructure shapes (for example, a boolean that toggles whether a whole service gets provisioned). This kind of variation is a sign the stack should be split, not parameterized.

When following this advice becomes difficult, that's usually a signal to refactor the stack — often splitting it into multiple stack projects rather than growing its parameter surface.

A parameter is really an incomplete solution: it pushes a decision the module's own code could have resolved onto whoever calls it, and every parameter added this way is a value someone downstream now has to research, choose correctly, and keep current as conditions change. Before adding one, ask whether the module could instead derive a good value itself — a database module facing a "connection pool size" decision can size the pool from the host's actual available memory and expected concurrency rather than asking every caller to guess a number; a retry-interval parameter can instead be computed from recently observed response times. A parameter only earns its place when the caller genuinely has domain knowledge the module cannot derive on its own (an environment's expected traffic tier, say) — not merely because working out a sensible default inside the module felt harder than exporting the decision.

Choosing *how* to supply parameter values to a stack instance is a separate decision — see the family of patterns from [manual parameters](manual-stack-parameters-antipattern.md) through [configuration files](stack-configuration-files-pattern.md), [wrapper stacks](wrapper-stack-pattern.md), [pipeline parameters](pipeline-stack-parameters-pattern.md), and the [parameter registry](stack-parameter-registry-pattern.md).
