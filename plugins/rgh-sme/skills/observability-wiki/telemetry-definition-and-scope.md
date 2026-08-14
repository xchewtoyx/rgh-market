---
type: concept
title: Telemetry Definition and Scope
description: Telemetry is the automated collection and transmission of measurements from running systems, spanning business, application, infrastructure, client-software, and deployment-pipeline layers to support debugging, capacity planning, and security auditing.
sources:
  - title: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations"
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 14"
  - title: "Database Reliability Engineering"
    resource: "Database Reliability Engineering (Laine Campbell & Charity Majors), ch. 9"
---

Telemetry is the automated process of collecting measurements and operational data from remote components and transmitting them to centralized systems for monitoring, analysis, and debugging. A robust telemetry strategy must cover both production and pre-production environments across the entire lifecycle of a system, not just the active request-serving path.

A complete telemetry strategy spans five distinct layers, each answering different questions:

* **Business** — Business outcomes and conversion rates (e.g., transactions, sign-ups, revenue, churn, A/B test splits). This layer is what turns a purely technical metric into a business one: Amazon's 2008 finding that every additional 100ms of latency cost roughly 1% of sales (later corroborated by Akamai, Google, and Zalando, among others) could only have been discovered — and could only be tracked as it improved or worsened afterward — because latency telemetry and business-outcome telemetry were both being collected and could be correlated against each other.
* **Application** — Code execution and user experience (e.g., transaction latency, response times, stack traces, exceptions). See [what to capture in a wide event](wide-event-attribute-checklist.md) for application event structure.
* **Infrastructure** — System components and dependencies (e.g., database, OS metrics, network throughput, storage I/O). See [The Four Golden Signals](four-golden-signals.md) for resource-level and endpoint monitoring.
* **Client software** — Frontend and mobile environments (e.g., errors, crashes, client-side load time). See [outcome-completion-rate as a UX proxy](outcome-completion-rate-as-ux-proxy.md).
* **Deployment pipeline** — Software delivery performance (e.g., build times, deployment frequency, failure rates, promotions).

## Telemetry as a Security and Compliance Signal

Operational telemetry and security auditing share a common collection substrate. In addition to diagnosing ordinary software bugs, fault telemetry and access logs double as security signals:

* **Application Layer**: Telemetry should capture syntax errors and connection drops. For instance, a sudden spike in database syntax errors (SQL exceptions) is a leading indicator of active SQL injection (SQLi) attempts rather than simple client bugs.
* **Database Layer**: Security audit telemetry must track structural changes (DDL statements), user/privilege mutations, and login anomalies. Logins originating from IP addresses or hostgroups outside the defined application-tier subnet are primary indicators of compromised credentials or network bypasses.
* **Operating System Layer**: File integrity monitoring should track configuration modifications and file writes against the deployment's immutable "golden image" configuration. Sustained CPU **steal time** or unexplained memory swapping should be monitored to detect unauthorized background resource consumption.

Explicitly audit for these telemetry gaps after every incident or security review to continually refine the system's defenses — see [closing telemetry gaps from past incidents](closing-telemetry-gaps-from-past-incidents.md).
