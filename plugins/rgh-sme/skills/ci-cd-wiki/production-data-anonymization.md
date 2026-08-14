---
type: concept
title: Production Data Anonymization for Lower Environments
description: >
  Raw production database copies must never be loaded into dev or test
  environments; use automated ETL scripts to sanitize and obfuscate personal
  and sensitive data before it enters any non-production environment.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 12"
---

# Production Data Anonymization for Lower Environments

Copying a raw production database into a dev, test, or staging environment is
a privacy and regulatory risk (PII exposure) as well as a security risk (a
lower-security environment now holds sensitive data). Where production-scale,
production-shaped data is genuinely needed — for example to satisfy
[capacity test environment fidelity](capacity-test-environment-fidelity.md)'s
realistic-data-volume requirement — the data must first pass through an
automated ETL pipeline that sanitizes, obfuscates, or scrubs personally
identifiable and sensitive fields before the dump is imported downstream.

This has to be automated and run as part of the environment-provisioning
pipeline, not a manual one-off scrub — a manual process is exactly the kind of
step that gets skipped under time pressure, defeating the point.
