---
type: concept
title: Deployment Choke Point
description: >
  A deployment policy only has teeth if every deployment request is forced
  through a single point that evaluates it — any path that bypasses that
  point defeats the policy regardless of how strict it is.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 14"
---

# Deployment Choke Point

A [provenance-based deployment policy](provenance-based-deployment-policy.md)
is worthless if an adversary — or an impatient engineer — can deploy directly
to production infrastructure without going through the point that evaluates
it. A choke point is a location through which every deployment request must
flow, with everything downstream of it configured to accept requests only
from that point.

## Example

In a Kubernetes cluster, the master node is a natural choke point for
deploying to that cluster's pods: configure worker nodes to accept
deployment requests only from the master, and evaluate policy at (or via) the
master itself — Kubernetes's Admission Controller webhook exists specifically
for this. Alternatively, a proxy placed in front of the choke point can
perform the policy check, provided the actual admission point is locked down
to accept traffic only from that proxy — otherwise an adversary bypasses the
proxy entirely by talking to the admission point directly.

This principle generalizes beyond Kubernetes: whatever mechanism actually
places an artifact into a running environment — a deployment script invoking
SSH, a package manager pull, a cloud provider API call — needs to be the
*only* such mechanism available, or a
[deployment breakglass](hotfix-through-pipeline.md) that's audited and rare
is the sole deliberate exception, not one of several equally available paths.
