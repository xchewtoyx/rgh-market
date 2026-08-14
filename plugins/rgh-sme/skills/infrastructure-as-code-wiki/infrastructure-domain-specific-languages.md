---
type: concept
title: Domain-Specific Languages for Infrastructure
description: Why most infrastructure tools use a language purpose-built to model infrastructure concepts rather than a general-purpose programming language, and the trade-offs of each choice.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 4"
---

A domain-specific language (DSL) is a small language focused on one aspect of a system — in this case, infrastructure. Ansible, Chef, and Puppet each provide a DSL with constructs for packages, files, services, and user accounts; Terraform and CloudFormation provide DSLs with constructs for virtual machines, disk volumes, and network routes. Modeling the domain directly like this makes the code easy to read even for someone unfamiliar with the specific tool, because it maps closely to the concepts being managed.

Most infrastructure DSLs are also [declarative](declarative-vs-imperative-infrastructure-code.md); some are *internal* DSLs written as a subset of a general-purpose language (Chef is Ruby), others are *external* DSLs interpreted by a separate engine (Terraform's HCL is unrelated to the Go language its interpreter is written in).

More recently, tools such as Pulumi and the AWS CDK use general-purpose, imperative languages (TypeScript, Python, Java) directly, trading the DSL's tight domain fit for the general-purpose language's mature ecosystem — IDE support, refactoring tools, and above all unit testing support, which most infrastructure-specific testing tools don't provide well.

A recurring design smell is code that mixes both paradigms in one place: extending a declarative syntax like YAML with ad hoc conditionals and loops, or embedding literal configuration values ("2GB RAM") inside procedural logic. When declarative code needs to support real variation, the better move is usually to keep the declaration simple and extract the variable logic into an imperative library — see the [infrastructure domain entity pattern](infrastructure-domain-entity-pattern.md) — rather than growing the declarative language's expressiveness in place.
