---
type: concept
title: Low-Level vs High-Level Infrastructure Languages
description: The distinction between stack code that maps directly to platform-provided resources and stack code that declares entities at a higher level of abstraction, letting a tool or library decide how to realize them.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 5"
---

Most popular [stack](infrastructure-stack.md) management tools use low-level infrastructure languages: the code directly exposes and wires together the resources the infrastructure platform provides (virtual machines, address blocks, gateways, routes), and the author is responsible for assembling them into something useful.

A high-level infrastructure language instead declares entities that don't map one-to-one onto platform resources — for example, declaring an `application_server` with just a public IP, and letting the underlying tool or library decide how to provision the networking and compute resources that requirement implies. Platform-as-a-Service offerings and packaged application clusters often provide this level of abstraction out of the box; where they don't, teams build it themselves as an [abstraction layer](abstraction-layer-for-infrastructure.md) of reusable components.

This distinction is orthogonal to, but often correlated with, the choice between [declarative and imperative code](declarative-vs-imperative-infrastructure-code.md): low-level stack code is usually declarative, while high-level abstractions that need to vary their output based on context are usually built with imperative libraries, as in the [infrastructure domain entity pattern](infrastructure-domain-entity-pattern.md).
