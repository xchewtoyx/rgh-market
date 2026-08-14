---
type: concept
title: Application Runtime Layer
description: The layer of a system, assembled from infrastructure-platform resources, that provides the execution environment an application actually runs in — and the app-driven approach to designing it.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 10"
---

The application runtime layer sits between an [infrastructure platform](infrastructure-platform-layers.md) and the applications running on it, composed of [infrastructure stacks](infrastructure-stack.md) that supply the execution environment, data management, and connectivity an application needs. Designing this layer starts from the applications that will use it: what languages and runtimes they need, whether they deploy to servers, containers, or FaaS, whether they're single instances or distributed services, and what their connectivity and data requirements are.

An **application-driven infrastructure** strategy builds runtime environments to fit an organization's actual application portfolio rather than assuming every application will become fully cloud-native. Many organizations' software isn't cloud-native and the cost of rewriting it often isn't justified by the benefit, so runtime environments need to support both new applications running as containers or FaaS and existing applications with more traditional deployment needs — often provided through a shared [abstraction layer](abstraction-layer-for-infrastructure.md) rather than forcing every consumer to work at the infrastructure-primitive level.

In practice, the boundary between the infrastructure, runtime, and application layers is fuzzier than the model suggests — different people and teams need access to resources at different levels of abstraction and control — so systems should be designed with composable pieces that can be presented differently to different users, rather than absolute boundaries. Related runtime-layer concerns covered separately include [deploying applications to server or container clusters](application-cluster-as-code.md), [service discovery mechanisms](service-discovery-mechanisms.md), and [FaaS serverless infrastructure](faas-serverless-infrastructure.md). See [matching deployment model to workload shape](matching-deployment-model-to-workload-shape.md) for how a workload's own characteristics — not just what the runtime layer offers — should drive which of these to reach for.
