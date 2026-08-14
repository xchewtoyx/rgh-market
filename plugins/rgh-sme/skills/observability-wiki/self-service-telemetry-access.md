---
type: concept
title: Self-Service Telemetry Access
description: Telemetry should be reachable by anyone who needs it via self-service dashboards or APIs, without production access, privileged accounts, or filing a ticket — gatekept telemetry access silently throttles how fast problems get found.
sources:
  - title: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations"
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 14"
  - title: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure"
    resource: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure (Sigelman et al.), §5"
---

When getting a basic metric (e.g. CPU usage across hosts for a service) requires filing a ticket and waiting for someone to assemble a report, the effective cost of looking at telemetry at all goes up, and people stop doing it until something is already badly broken. Self-service access — dashboards and query APIs anyone on the team can use directly — removes this friction, and has repeatedly been the difference between catching a slow degradation early and finding out from a customer (or, in one case, from another company whose own systems were trending downward before their own team noticed).

**Information radiators** — dashboards or displays placed in a highly visible shared location — are a related practice: making system health visible by default, rather than something you have to go looking for, signals that the team has nothing to hide from visitors or from itself. Some organizations extend this to public-facing status pages, trading transparency for customer trust.

This is a dashboard-design/access concern distinct from *what* to put on a dashboard (see [purposes of monitoring](purposes-of-monitoring.md)) — it's about who can reach the dashboard and how much friction stands between "I have a question" and "I have an answer."

The payoff of investing in self-service access shows up directly in adoption: Google's Dapper was, as a prototype, only usable with hands-on help from its own developers; once it shipped a general-purpose query API plus an interactive web UI that let users investigate independently, it reached roughly 200 distinct engineers on a typical weekday (750–1000 over a week) — usage that hand-held access could never have scaled to. The self-service layer didn't just make existing usage more convenient, it was what made broad usage possible at all. It also surfaced uses the tracing team never designed for — resource-accounting systems, tools checking that sensitive services stuck to an approved communication pattern, an analysis of RPC compression strategies — because opening the underlying data to a simple API let a much larger community than the owning team build against it, rather than every use case having to be anticipated and built by the team that owns the data.
