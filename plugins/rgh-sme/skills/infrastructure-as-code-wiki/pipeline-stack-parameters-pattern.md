---
type: concept
title: "Pattern: Pipeline Stack Parameters"
description: Defining per-environment stack parameter values in the configuration of a delivery pipeline tool, rather than in the stack project itself.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 7"
---

This pattern sets [stack instance](stack-parameter-design-principles.md) parameter values in the configuration of the [delivery pipeline](infrastructure-delivery-pipeline.md) stage that applies the stack, rather than in a file or script within the stack project. If the pipeline tool is itself configured as code, the values still end up version-controlled, just outside the stack project — and configuration values stay separate from infrastructure code, so a downstream environment's configuration can change without progressing a new code version through the whole pipeline from scratch.

It's a natural choice for teams already applying infrastructure code through a pipeline, but it has a serious drawback once a stack needs more than a handful of parameters: it couples configuration to the delivery process, makes the pipeline itself a single point of failure (you can't fix or rebuild an environment in an emergency without the pipeline available), and makes it hard to develop or test the stack code outside the pipeline. Keep the pipeline configuration for applying a stack as small as possible; most logic should live in a script the pipeline calls, per [wrapper scripts for infrastructure tools](wrapper-scripts-for-infrastructure-tools.md), rather than in the pipeline configuration itself. Most CI/CD tools' secret-management features pair naturally with this pattern for supplying [secrets](handling-secrets-in-infrastructure-code.md) as parameters.
