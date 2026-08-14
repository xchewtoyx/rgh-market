---
type: concept
title: Blue-Green Deployment
description: >
  Maintain two identical production environments and cut traffic over from
  the active one to the newly deployed one with a single router change,
  giving near-instant rollback at the cost of double the resources.
sources:
  - title: "Release It!"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Nygard), ch. 13"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook: Practical Ways to Implement SRE (Google SRE series), ch. 16"
---

# Blue-Green Deployment

Blue-green deployment maintains two identical, full-sized production
environments: "blue" (currently serving live traffic) and "green" (idle).
To release, deploy the new version to green, run automated sanity checks
against it, then switch the router or load balancer so all traffic points
at green. Blue becomes idle and is the rollback target.

Properties:

- **Rollback is trivial and instant**: switch the router back to blue — no
  redeploy, no data to unwind (as long as the change didn't also mutate
  shared state incompatibly; see [expand-and-contract schema migration](expand-and-contract-schema-migration.md)
  for how to keep schema changes compatible with an instant cutback).
- **Cost**: roughly double the production footprint, since a full idle
  environment is kept on standby.
- **Cutover is instantaneous** by default, but the same two-environment
  setup can be run as a gradual cutover instead — shifting traffic to green
  incrementally rather than all at once — which turns blue-green into a
  form of [canary release](canary-release.md).

Compare with [rolling deployment](rolling-deployment.md), which updates the
existing fleet in place instead of maintaining a second environment, and
trades instant rollback for lower resource cost.
