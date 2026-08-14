---
type: concept
title: Terraform Module Versioning and Promotion
description: Pinning a Terraform module consumer to a specific tagged version of the module's source, and rolling changes through environments by advancing that pin one environment at a time.
sources:
  - title: Terraform Up & Running
    resource: "Terraform: Up & Running, 3rd Edition (Yevgeniy Brikman), ch. 4"
---

A Terraform module's `source` argument can point at a local path, a Git repository (`source = "github.com/org/repo//subdir?ref=TAG"`, where the double slash separates the repository from the subdirectory inside it), a private SSH Git URL, or a registry entry (`source = "hashicorp/consul/aws"`). Pinning `ref` to a Git tag rather than a branch is what makes a module's version explicit and stable for a given caller.

Modules are conventionally versioned with semantic versioning: a MAJOR bump means an incompatible change (removing an input, changing something that forces resource replacement); MINOR means a backward-compatible addition (a new optional input with a sensible default); PATCH means a backward-compatible fix. This mirrors the general [semantic versioning](server-image-as-code.md) discipline used for [server images](server-image-as-code.md) and other infrastructure artifacts.

Promoting a module change through environments works by advancing which tagged `ref` each environment's caller code points at, one environment at a time: tag the new module version, update the `stage` caller to the new `ref`, run `terraform init -upgrade` and apply, validate in `stage`, and only then update the `prod` caller to the same `ref` — production keeps running the old, still-pinned version throughout, unaffected by the tag existing. This is a concrete implementation of the general [apply-time project integration pattern](apply-time-project-integration-pattern.md): each environment applies whatever module version its own caller code currently points at, rather than every environment being forced onto the same version simultaneously.
