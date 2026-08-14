---
type: concept
title: Version-Control Everything the Pipeline Depends On
description: >
  Not just application source: test suites, build and deployment scripts,
  infrastructure-as-code definitions, and configuration templates must all be
  in version control for a build to be reproducible from scratch.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 1, 2"
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 4"
---

# Version-Control Everything the Pipeline Depends On

For the [deployment pipeline](deployment-pipeline.md) to be reproducible —
so that the same commit always produces the same build and passes or fails
the same way — every input to that process must be version-controlled, not
just application source code:

- application source code and test suites
- build scripts and deployment scripts
- database migration scripts
- infrastructure-as-code definitions (config-management tool definitions, OS
  templates, container specs)
- web server, middleware, and network configuration files/templates

Practices that support this: commit small, atomic changes frequently
(daily or more per developer), write commit messages that reference the
issue/story driving the change, and keep the branch topology flat — see
[trunk-based development](trunk-based-development.md) — so there is one
canonical history rather than divergent copies of "the truth."

## Configuration in version control correlates more strongly than code

Empirical research found that version-controlling **system and application
configuration** specifically has a *stronger* correlation with software
delivery performance than version-controlling application code alone. This
matters because config is exactly the layer most likely to be treated as an
afterthought or edited by hand in place — precisely the
[snowflake server](snowflake-server.md) risk this whole practice exists to
close off. If forced to prioritize, bringing configuration under version
control pays off disproportionately relative to its typical treatment.
