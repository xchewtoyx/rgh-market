---
type: concept
title: Infrastructure as Code
description: An approach to infrastructure automation, based on software development practices, that defines and changes systems by applying versioned code rather than making changes by hand.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 1"
---

Infrastructure as Code (IaC) is an approach to infrastructure automation that emphasizes consistent, repeatable routines for provisioning and changing systems and their configuration. Rather than making changes directly — through a console, CLI, or by hand — you change code, then use automation to test and apply those changes to the real system. The tool reads the code and either creates new infrastructure or reconciles existing infrastructure to match it.

IaC applies Agile software engineering practices — Test Driven Development, Continuous Integration, and Continuous Delivery — to infrastructure, on the premise that changes are the biggest source of risk to a running system, changes are inevitable and continuous over a system's life, and the only way to improve a system is to change it. See [optimizing infrastructure for continuous change](optimizing-infrastructure-for-continuous-change.md) for the reasoning behind treating change as routine rather than exceptional.

IaC rests on three core practices, each of which reinforces the others:

- [define everything as code](define-everything-as-code.md)
- [continuously test and deliver infrastructure changes](infrastructure-delivery-pipeline.md)
- [build infrastructure from small, simple, loosely coupled pieces](infrastructure-component-coupling-and-cohesion.md)

Adopting IaC depends on having a dynamic [infrastructure platform](infrastructure-platform-layers.md) — one you can provision and change on demand through an API — since the value of defining infrastructure as code comes from being able to apply that code quickly and repeatedly.

"IaC" is sometimes used narrowly for provisioning tools like Terraform, distinct from "configuration management" tools like Ansible or Puppet — this bundle treats both as facets of the same discipline; see [Infrastructure as Code vs Configuration Management](infrastructure-as-code-vs-configuration-management.md) for why, and for where the practical differences between them actually live.
