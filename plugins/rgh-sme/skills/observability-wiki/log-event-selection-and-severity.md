---
type: concept
title: Log Event Selection and Severity Conventions
description: Consistent severity-level conventions and a shared checklist of which event categories deserve a log entry keep application logs both complete enough to investigate incidents and quiet enough to be usable.
sources:
  - title: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations"
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 14"
---

**Severity levels and their intent:**

- **DEBUG** — anything happening in the program; usually disabled in production, enabled temporarily for troubleshooting.
- **INFO** — user-driven or system-specific actions (e.g. "beginning credit card transaction").
- **WARN** — conditions that could become an error (e.g. a slow DB call); may trigger an alert or investigation.
- **ERROR** — error conditions (API failures, internal errors).
- **FATAL** — must-terminate conditions (e.g. can't bind a network socket).

A practical test for the ERROR/WARN boundary: imagine being woken at 4 AM by this message — "low printer toner" is not an ERROR.

**Categories of events worth a log entry**, independent of severity: authentication/authorization decisions (including logoff), system/data access, system/application changes (especially privileged ones), data changes (add/edit/delete), invalid input (possible injection or malicious input), resource usage (RAM/disk/CPU/bandwidth), health/availability, startups/shutdowns, faults/errors, circuit-breaker trips, delays, and backup success/failure. Organizing logs into hierarchical categories (non-functional: performance, security; feature-related: search, ranking) makes this checklist tractable at scale rather than an unstructured firehose.

This severity/category discipline is what makes [centralized log-to-metric conversion](centralized-log-to-metric-conversion.md) and later incident investigation both possible — see also [structured logging](structured-logging.md) for making the resulting log lines machine-queryable rather than free text.
