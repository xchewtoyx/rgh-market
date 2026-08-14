---
type: concept
title: Infrastructure for FaaS Serverless
description: What still needs to be defined and provisioned as infrastructure code around Function-as-a-Service platforms, even though the servers running the code are invisible to the developer.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 14"
---

Function as a Service (FaaS) executes application code on demand — in response to an event or a schedule — and terminates it once it completes, rather than running it as a continuous process the way a server or container would. "Serverless" is a loose term here: the code still runs on a server, just one that's invisible to the developer, and the same is arguably true of containers; what's actually distinctive about FaaS is that the workload is short-lived rather than long-running. This is also why some people prefer the term FaaS to "serverless," which is ambiguous with *Backend as a Service* (an externally hosted service).

FaaS platforms follow the same two implementation models as [application clusters](application-cluster-as-code.md): provided as a service by the infrastructure platform (AWS Lambda, Azure Functions, Google Cloud Functions) or self-deployed as a packaged solution (Fission, Kubeless, OpenFaaS, Apache OpenWhisk) onto infrastructure you provision. FaaS-as-a-service usually leaves far less for you to define directly — no host server sizing, for instance — which meaningfully reduces the infrastructure code you need to write and manage.

Even so, FaaS code is rarely infrastructure-free: it usually needs networking for inbound triggers and outbound calls, and it reads and writes to storage, databases, and message queues, all of which are ordinary infrastructure resources that need to be defined, provisioned, and tested like any other stack element — many stack tools (Terraform, CloudFormation) let you declare the FaaS code deployment itself as part of the same stack. FaaS code still needs to be delivered and tested through a [pipeline](infrastructure-delivery-pipeline.md) like any other code, and teams should understand how their specific FaaS platform isolates execution, since some can leak data between invocations through shared temporary storage, with implications for security and compliance.
