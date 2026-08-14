---
type: concept
title: "Pattern: Infrastructure Domain Entity"
description: A high-level, imperative-language component that dynamically provisions the lower-level infrastructure resources needed for a business concept, driven by Domain-Driven Design.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 16"
---

An infrastructure domain entity implements a high-level component — such as "the infrastructure needed to run this application" — by combining multiple lower-level resources, with logic that varies what it provisions based on the caller's actual requirements (for example, sizing a cluster differently for `high`, `medium`, or `low` expected traffic). Because it needs to produce genuinely different results in different cases, it should be written in an imperative language rather than a declarative one — see [declarative vs imperative infrastructure code](declarative-vs-imperative-infrastructure-code.md) — which is what distinguishes it from a [bundle module](bundle-module-pattern.md), a similarly cohesive collection of resources that stays close to static.

The pattern borrows from Domain-Driven Design: it treats infrastructure delivery as a domain in its own right (the business of building, delivering, and running software) and designs components top-down from what a use case requires, rather than bottom-up from the low-level resources available — the inverse of how a bundle module is usually approached. This top-down, use-case-first design is what makes domain entities a natural building block for an [abstraction layer](abstraction-layer-for-infrastructure.md) that a platform team offers to application teams.

A domain entity with poor cohesion — one that's absorbed too many divergent responsibilities — degrades into a [spaghetti module](spaghetti-module-antipattern.md), the same failure mode that results from trying to build this pattern's dynamic behavior using a declarative language instead of an imperative one.
