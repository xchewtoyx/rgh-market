---
type: concept
title: Decoupling Deployment from Release
description: >
  Treat installing new code in production and exposing it to users as two
  separate acts, so that technical delivery risk and business exposure risk
  can be managed independently.
sources:
  - title: "Continuous Delivery"
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 10"
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 26"
---

# Decoupling Deployment from Release

*Deploy* and *release* are two different acts that are easy to conflate
because they traditionally happened at the same moment:

- **Deploy** — installing a specific build of the software into a
  production environment and starting it running.
- **Release** — making the new behavior visible or available to users.

Once these are separated, each can be scheduled and de-risked on its own
terms. Code can be deployed to production, verified there under real
conditions (real infrastructure, real dependency versions, real traffic
patterns it doesn't yet serve), and left dormant — with no user-facing risk
— until someone makes the business decision to release it.
[Feature flags](feature-flag-blast-radius-isolation.md) are the most common
mechanism for this: the deployed binary contains the new code path, but a
flag keeps it off until release is deliberately triggered, independent of
and usually much later than the deploy.

This decoupling is what makes "deploy on every commit, release on a
business schedule" possible — it's the difference between [continuous
delivery and continuous deployment](continuous-deployment-vs-continuous-delivery.md):
CD pipelines can push every passing change all the way to production
constantly without that implying every change is instantly visible to
users.

For a multi-tenant service, the same separation can be extended outward to
customers themselves rather than controlled only internally — see
[customer-facing release tracks](customer-facing-release-tracks.md).

The same separation applies to *cadence*: how often the team *can* deploy
need not equal how often users *receive* updates. A smooth continuous
delivery process may produce viable releases daily or hourly while the
product intentionally pushes to users weekly — or less — based on user
needs (mobile data cost, disruption, platform constraints). Modular
architecture and per-device configuration can further limit what each user
downloads (unused translations, wrong-architecture binaries), keeping
client size down while deploy capability stays high.
