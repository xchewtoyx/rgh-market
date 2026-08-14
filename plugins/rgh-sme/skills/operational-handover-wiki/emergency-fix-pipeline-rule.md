---
type: concept
title: Emergency Fix Pipeline Rule
description: The operational rule requiring all emergency patches and hotfixes to pass through the standard automated delivery pipeline to prevent regressions.
sources:
  - title: "Continuous Delivery"
    resource: "Continuous Delivery (Humble and Farley), ch. 10"
---

During a production outage or high-severity incident, the pressure to restore service quickly often leads teams to bypass standard procedures. However, applying manual patches directly to production environments is an anti-pattern that frequently compounds the outage or causes future regressions.

## The Golden Rule of Emergency Fixes

**All emergency fixes and hotfixes must follow the exact same deployment pipeline as routine changes.**

The fix must be committed to version control, run through automated compile and test suites, packaged, and deployed using the standard deployment automation.

## Rationale for the Rule

Bypassing the automated pipeline to execute manual hotfixes introduces several severe risks:

- **Secondary Outages**: Manual changes bypass compile-time checks, unit tests, and integration tests, making it easy to introduce syntax errors, dependency conflicts, or database deadlocks that worsen the incident.
- **Configuration Drift**: Manual modifications on production servers create drift. The production environment is no longer in sync with the configuration definitions in version control.
- **Overwritten Fixes**: Any manual fix applied directly to a server will be wiped out and lost during the next standard, automated deployment. This can cause a resolved bug to silently reappear weeks later.
- **Audit Failure**: Manual changes bypass the logs and version-control histories that record what ran, when, and who authorized it, making post-incident forensic analysis and regulatory compliance audits impossible.

## Operational Prerequisites

For this rule to be viable under pressure, the organization must ensure that:
- The deployment pipeline is fast, predictable, and completes in minutes.
- The pipeline's current status and failures are highly visible to operators.
- Rollback mechanisms (such as feature flags or load-balancer redirects) are automated and tested regularly to mitigate the need for rapid hotfixes in the first place.

For details on how to plan for emergencies and rollbacks, see [Operational Release Readiness Plan](operational-release-readiness-plan.md) and [Playbook Maintenance Tension](playbook-maintenance-tension.md).
