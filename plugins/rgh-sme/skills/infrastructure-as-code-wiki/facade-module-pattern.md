---
type: concept
title: "Pattern: Facade Module"
description: A declarative module that wraps a single infrastructure resource with a simplified interface, exposing only a few parameters and hardcoding the rest.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 16"
---

A facade module (also called a *wrapper module*) provides a simplified interface to a single underlying resource from the stack language or platform, exposing a handful of parameters to callers and hardcoding everything else — for example, a `shopspinner-server` module that lets callers set just a name and memory size, while hardcoding the base image, provisioning role, and network placement every server of that kind should share.

Facade modules work best for simple, well-understood use cases, and are naturally declarative, since they don't need to vary their output much. They standardize and simplify a common case, and improvements to the module immediately benefit every stack that uses it — but they add an extra layer of indirection to read, debug, and maintain, and they inherently limit flexibility, so they don't fit every use case for the resource they wrap.

A facade module that doesn't meaningfully simplify or add value over using the underlying resource directly is an **obfuscation module** — a facade gone wrong, usually created either by over-applying [DRY](infrastructure-domain-specific-languages.md) to code that only looks similar, or by trying to invent a "better" language on top of the stack tool's own. If a module neither simplifies its resource nor adds real value, replace its usages with the stack language directly. An **unshared module** — one used in only a single place — is a related smell: dividing a stack's code into modules purely for internal organization, when it isn't reused, adds versioning and maintenance overhead for no benefit (a case of *YAGNI*); splitting the stack itself, or just organizing files within it, is usually better. A [bundle module](bundle-module-pattern.md) extends the facade idea to multiple related resources.
