---
type: concept
title: Deploy vs. Release
description: >
  Deploying (installing and starting a version of the software in production)
  and releasing (making a feature visible or usable to end users) are
  separate acts, and decoupling them separates technical risk from business exposure.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 10"
---

# Deploy vs. Release

- **Deploy**: the technical act of installing, configuring, and starting a
  specific version of the software binaries in a target environment,
  including production.
- **Release**: the business act of making the new functionality visible or
  usable to (some or all) end users.

Once these are separate, a build can be deployed to production — verified
there, running real infrastructure, absorbing real load — while remaining
invisible to users, because "deployed" no longer implies "released." This is
the mechanism [feature toggles](feature-toggle.md) implement: deploy
continuously, release on a separate schedule driven by business readiness
rather than technical readiness.

It also reframes what
[continuous delivery vs. continuous deployment](continuous-deployment.md)
actually differ on: both can deploy every passing change to production
automatically; the distinction that matters is whether *release* is a
manual business decision or happens automatically alongside deployment.
