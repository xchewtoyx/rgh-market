---
type: concept
title: Secretless Authorization
description: >
  Authorize an action by verified identity — a workload's IAM role, its
  network origin — instead of a shared secret it presents, because a
  secret that was never issued can't be leaked, stolen, or committed to
  version control by mistake.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code, 3rd Edition (Morris), ch. 7"
  - title: "Terraform: Up & Running, 3rd Edition"
    resource: "Terraform: Up & Running, 3rd Edition (Brikman), ch. 6"
---

# Secretless Authorization

Most authorization schemes work by checking a secret the caller presents:
a password, an API key, a token. Secretless authorization instead
authorizes based on a property of the caller that doesn't need to be
kept secret to be trustworthy — a cloud platform's own identity for the
compute instance making the call (an IAM instance profile or workload
identity), or, more weakly, the caller's verified network origin. A
compute instance authorized this way for a database or API needs no
password on disk, in an environment variable, or baked into a build —
because there's no credential value for a leak, a version-control commit,
or a stolen backup to expose in the first place. This is the strongest
answer to [secrets committed to version control](secrets-in-version-control.md):
a class of leak with no secret to leak.

**Federated identity extends the same pattern to CI/CD running outside
the cloud provider it needs to authorize against.** A pipeline job can
present a short-lived, provider-issued token (an OIDC JWT identifying
"this specific pipeline run") to the target cloud's token service and
receive a scoped, time-limited credential in exchange — no static access
key is ever stored in the CI system at all. This gets the same property a
cloud-native instance identity gets automatically (no standing secret to
leak from CI's own credential store), while also working for pipelines
that don't run on the target cloud's own compute. Compare this to storing
long-lived static credentials as CI secrets: a leaked static key grants
whatever it was scoped to until someone notices and rotates it, while a
leaked federated token is only ever narrowly scoped and already close to
expiry.

**This shifts the attack surface rather than eliminating it.** Tying
authorization to "runs as this identity" or "connects from this address"
means anyone who compromises that identity or that network position
inherits the authorization it carries — the same exposure a stolen secret
would have created, just relocated to whatever grants the identity itself.
Protecting the compute instance or network boundary that the trust rests
on becomes the real control, which is exactly the reasoning behind
[compartmentalization](compartmentalization.md) and
[least privilege](least-privilege.md) applied to that instance: minimize
what runs on it and who can reach it, because its identity is now doing
a secret's job. A useful framing: a compromised instance that never held
a static secret is no more exposed than one that did, and having removed
the secret entirely removes it as a target independent of that instance —
it can no longer be found sitting in a config file, a log, or a backup
somewhere else in the system.

**When a secret genuinely can't be avoided, generate it on demand instead
of provisioning it as a standing value.** A database password created
automatically at provisioning time, handed directly to the consuming
service, and never displayed to or stored by a human closes most of the
same exposure paths a secretless design closes — there is no long-lived
value sitting in a password manager, a config file, or someone's memory
to leak. [Credential rotation](credential-rotation.md) is the same idea
generalized: a disposable secret is simply rotation compressed to "every
time," which is also why regularly practiced rotation and secretless
design point at the same underlying goal — the shorter a secret's
effective lifetime and the fewer places it's ever visible, the less there
is for an attacker to find.
