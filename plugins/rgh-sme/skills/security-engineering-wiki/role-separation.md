---
type: concept
title: Role Separation
description: >
  Run different jobs as different service accounts so that compromising
  one job yields only that role's access, not every job's.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 8"
---

# Role Separation

In microservice architectures, jobs run as *roles* (service accounts) with
credentials to authenticate to other services. If an adversary compromises
one job, they can impersonate its role network-wide — effectively
compromising every other job running as that same role, and reaching all
data any of those jobs could access.

The [blast-radius](compartmentalization.md) control: run different jobs as
different roles. Two microservices touching different data classes (say,
photos and text chats) should run as different roles *even when the same
team develops and operates both* — compromise of one then doesn't grant
the other's data.

Role separation composes with [location](location-separation.md) and time
separation, and is the service-to-service face of
[least privilege](least-privilege.md): a role's credentials should carry
exactly the access its job needs. Validate that cross-role operations
which should fail actually do
([continuous validation](continuous-validation.md)).

This is distinct from
[delivery-pipeline separation of duties](delivery-pipeline-separation-of-duties.md),
which separates the *human* who authors a change from the *system* that
can deploy it — a different axis that a shared, overprivileged service
account can undermine even when role separation is otherwise solid.
