---
type: concept
title: Low-Dependency Design
description: A resilience pattern where a simplified, alternative serving path is built with minimal dependencies to ensure critical functions survive when the main infrastructure stack fails.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 8"
---

Modern high-capacity services rely on deep infrastructure stacks (virtualization, orchestrators, scheduling platforms, service meshes, and distributed databases). While these layers enable rapid scaling and rich features, they also accumulate failure risk—the aggregate error rate increases as error budgets across cooperating platforms compound. 

When extreme availability is required for critical functions, reliability engineers employ **low-dependency design**.

## Core Characteristics

A low-dependency component is a secondary, highly simplified implementation of a critical service pathway. It is characterized by:
1.  **Minimal Dependencies**: The component operates directly on raw or local resources, avoiding network calls, complex coordinate systems, or shared clustering software where possible (e.g., utilizing locally cached read-only files instead of a remote database).
2.  **Feature and Bandwidth Reduction**: To keep the implementation simple and understandable, non-essential features, real-time data freshness, and bandwidth capacity are deliberately sacrificed.
3.  **Isolated Failure Domains**: The alternative path must share no common failure domains (hardware, network links, or control planes) with the primary path.

## Common Examples

*   **Emergency Administration Networks**: During a global network outage, dynamic software-defined networks (SDNs) and complex routing planes can prevent administrator access. A low-dependency, separate static management network with limited bandwidth allows engineers to log in and deploy fixes.
*   **Local Event Logging**: If a remote logging endpoint is unreachable, a low-dependency client writes event records to local storage, serving local requests using cached state and queueing external synchronization to retry once connectivity returns.
*   **Static Fallbacks**: A web application serving static cache files or cached HTML directly from a CDN origin when the primary dynamic rendering application tier or database goes down.

## Alignment with Dependency Composition

A low-dependency design is an application of [independent failover reliability composition](independent-failover-reliability-composition.md). By creating a path that does not inherit the complex constraints of the primary stack, it prevents localized infrastructure outages from escalating into a global service failure. However, converting these paths into soft dependencies is essential; otherwise, the secondary path remains a hidden source of [cascading failure](cascading-failure.md) or logic bugs. See [hard vs soft dependency](hard-vs-soft-dependency.md).
