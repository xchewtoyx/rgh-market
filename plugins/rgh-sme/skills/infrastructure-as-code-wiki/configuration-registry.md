---
type: concept
title: Configuration Registry
description: A service that stores configuration values for multiple purposes — stack parameters, service discovery, cross-stack integration — as a hierarchical or key-value store separate from any one project's code.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 7"
---

A configuration registry is a service that stores configuration values that many different tools and purposes can draw on — feeding [stack instance parameters](stack-parameter-registry-pattern.md), enabling [service discovery](service-discovery-mechanisms.md), or supporting [cross-stack dependency discovery](integration-registry-lookup-pattern.md). When talking specifically about supplying values to stack instances, the more specific term is a [stack parameter registry](stack-parameter-registry-pattern.md) — a particular use case of a general configuration registry.

Implementation options span a spectrum: registries bundled with an infrastructure automation toolchain (Chef Infra Server, PuppetDB, Ansible Tower, Salt Mine) are convenient but create lock-in to that toolchain; general-purpose products (Zookeeper, etcd, Consul, doozerd) avoid that lock-in but need you to design a naming and structure convention yourself; cloud platform key-value services (such as AWS SSM Parameter Store) avoid running your own server but tie you to that platform; and DIY registries built on existing file, object, or package-repository infrastructure are quick to start but tend to accumulate custom glue code as needs grow.

A single organization-wide registry ("one registry to rule them all") is appealing but often impractical, because many specialized tools bring their own registries that are very good at their own narrow task (license management, service discovery, user directories); bending all of them into one system is an ongoing maintenance burden. It's usually better to know which system is the authoritative source of truth for each kind of data, and pull from wherever that is, than to force consolidation — some teams instead broadcast configuration changes as events over a messaging system so interested systems can keep their own view in sync.
