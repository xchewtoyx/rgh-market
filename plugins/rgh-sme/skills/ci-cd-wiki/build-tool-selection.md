---
type: concept
title: "Build Tool Selection: Imperative vs. Declarative"
description: >
  Imperative build tools (Make, Ant, Rake) give full control over explicit
  build steps at the cost of maintainability; declarative tools (Maven,
  Gradle) trade some flexibility for a consistent, enforced lifecycle.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 6"
---

# Build Tool Selection: Imperative vs. Declarative

- **Imperative tools** (Make, Ant, Rake): the developer writes the exact
  step-by-step procedure. Maximum flexibility, but scripts tend to grow
  verbose and duplicated as a codebase scales, since there's no shared
  convention forcing similar projects to look alike.
- **Declarative / convention-over-configuration tools** (Maven, Gradle): the
  developer declares project metadata, dependencies, and plugins; the tool
  enforces a standard lifecycle (compile, test, package, deploy) and directory
  layout. Consistent across projects and comes with built-in dependency
  resolution, at the cost of flexibility for non-standard workflows.

Regardless of which family is chosen, the tool's job is compilation,
dependency resolution, and unit testing — not system-level provisioning or
deployment. Use scripting languages (Python, Ruby, Bash, PowerShell) or
dedicated configuration-management tools (Puppet, Chef, Ansible) for OS
orchestration and deployment; see
[deployment script design](deployment-script-design.md). Mixing the two
concerns inside a single build-tool script is a common source of unmaintainable
pipelines.

Whichever tool is chosen, it must still satisfy
[single-command build](single-command-build.md).
