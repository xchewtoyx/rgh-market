---
type: concept
title: Secrets Management in Pipelines
description: >
  Passwords, private keys, and API credentials must never be stored in plain
  text in version control, and must instead be encrypted at rest or injected
  securely at deploy/runtime by a dedicated secrets manager.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 2"
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 14"
  - title: "Terraform: Up & Running"
    resource: "Terraform: Up & Running, 3rd ed. (Yevgeniy Brikman), ch. 10"
  - title: Serverless Design Patterns and Best Practices
    resource: "Serverless Design Patterns and Best Practices (Brian Zambrano), ch. 9"
---

# Secrets Management in Pipelines

Secrets are configuration values with a stricter constraint than ordinary
[configuration injection](configuration-injection.md): they cannot be committed
to version control in plain text at all, because version-control history is
effectively permanent and often broadly readable. Two acceptable patterns:

- Encrypt secret values before they enter version control (e.g. with a vault
  tool or GPG), decrypting only at deploy/runtime.
- Keep secrets out of version control entirely and inject them at runtime via
  a dedicated secrets manager, so the pipeline never persists the plaintext
  value anywhere it doesn't strictly need to.

Either way, the deployment pipeline's automation must be able to retrieve and
inject secrets without a human pasting them in by hand — otherwise the
pipeline reintroduces exactly the manual, undocumented step that
[configuration management](configuration-management.md) discipline exists to
remove.

## Prefer short-lived federated credentials over long-lived static ones

A pipeline that deploys to cloud infrastructure needs some credential with
enough privilege to create, modify, or destroy real resources — historically
solved by storing a long-lived cloud admin credential as a pipeline secret.
This is a high-value, high-blast-radius target: anyone who compromises the
CI system (a malicious dependency in a build step, a leaked log, a
compromised plugin) inherits that credential's full standing privilege
indefinitely. The stronger pattern is federated, short-lived credentials —
the pipeline run presents proof of its own identity (e.g. an OIDC token
scoped to a specific repository and branch) to the cloud provider, which
exchanges it for temporary credentials scoped only to what that run needs
and that expire on their own shortly after. A compromise of the CI system
under this model yields, at worst, a narrowly-scoped credential that expires
soon, instead of a standing master key. Where the pipeline itself can't be
trusted with even scoped apply privileges, push the privileged step out to
an isolated, locked-down execution environment that the main CI system can
trigger but doesn't itself hold credentials for — the same
[build privilege separation](build-privilege-separation.md) logic applied to
deployment credentials rather than signing keys.

## Service credentials vs. human credentials

Grant secrets access to services, not humans, and only when a given service
genuinely needs a given secret to operate. If a human needs to access
something resembling a secret, it's usually actually a password for personal
use rather than an application secret — issue that human a separate
credential rather than widening access to the service's own secret. Keeping
these two credential classes distinct means rotating or revoking one never
requires touching the other.

## CI provider UI vs. tracked configuration

Hosted CI systems typically split variables into two classes:

- **Non-sensitive configuration** (test database host, environment name, region)
  can live in tracked pipeline YAML — visible in code review, versioned with
  the application.
- **Secrets** (production database passwords, cloud access keys) are set once
  in the CI provider's encrypted environment-variable UI and referenced by
  name in deploy steps, never committed. Deployment tools and cloud SDKs pick
  them up as ordinary environment variables at runtime.

Some providers also inject build-context markers (e.g. a variable indicating
"running inside CI") so test bootstrap code can branch — linked service
containers reachable at `localhost` in CI versus named Docker links locally.
That keeps one test suite working in both environments without duplicating
test logic.
