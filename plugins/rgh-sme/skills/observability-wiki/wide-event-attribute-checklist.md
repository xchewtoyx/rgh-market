---
type: concept
title: Wide Event Attribute Checklist
description: A practical checklist of attribute categories to capture on a wide event — service/code context, request/execution flow, user/business context, and operational info — each unlocking specific investigative queries later.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 6"
---

"Arbitrarily wide" means no practical ceiling on how much context a single event carries — well-instrumented codebases end up with hundreds of attributes per event. A practical (non-exhaustive) checklist of what to capture, by category:

- **Service/code context**: service name/team/environment/on-call channel (ties who gets paged to what broke); infrastructure metadata (instance ID, memory, CPU, instance type, AZ/region, k8s cluster/pod); build info (version, git hash, deploy ID, PR/diff URL, deploy age — answers "did something just get deployed?"); feature-flag values per request (compare a new-code cohort against control instantly); runtime/library/datastore versions (answers "does this correlate with the recent framework upgrade?").
- **Request and execution flow**: HTTP attributes (route, method, status, body sizes); route/parameter attributes parsed into structured fields (group p99 by `http.route` rather than regexing a raw path later); async/summary stats (counts and cumulative durations of DB/cache/vendor calls per request) to spot bimodal or outlier request shapes; error attributes, notably a stable, unique, greppable identifier per throw-site — see [exception slugs for error attribution](exception-slug-for-error-attribution.md). See also [timings as attributes, not child spans](timings-as-attributes-not-child-spans.md) for a specific pitfall in this category, and [proxy-mediated success and latency reporting](proxy-mediated-success-and-latency-reporting.md) for why self-reported success/latency fields can be unreliable exactly when they matter most.
- **User and business context**: user ID, tier/plan, auth method, team/org ID, account age; rate-limit state (limit/remaining/used/reset) so support questions about throttling are queryable rather than guesswork; cache hit/miss flags; localization fields.
- **Operational info**: `uptime_sec` (and its log-scale transform, to visualize both fresh and long-running instances on one graph) to spot crash loops; periodically-sampled system metrics (memory, CPU, GC pause, event-loop lag) attached to spans for fast-triage correlation — explicitly not meant for alerting or rigorous statistics, just quick context.
- **Domain-specific attributes**: whatever is unique to the business (vendor transaction IDs, queue depth at submission time) — no generic framework can supply these; they require domain expertise.

A useful filtering convention: tag one designated span per request/job as `main = true` — see [the main-span flag convention](main-span-flag-convention.md) — so queries can isolate the primary unit of work from noisy child spans.
