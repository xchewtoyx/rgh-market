---
type: concept
title: Secret Leakage Through Derived Artifacts
description: >
  A secret supplied safely can still end up materialized in plaintext
  inside a tool's own output — state files, plan files, logs — which then
  need the same protection as the secret store itself, or the careful
  supply path was pointless.
sources:
  - title: "Terraform: Up & Running, 3rd Edition"
    resource: "Terraform: Up & Running, 3rd Edition (Brikman), ch. 6"
  - title: Infrastructure as Code, Patterns and Practices
    resource: "Infrastructure as Code, Patterns and Practices (Wang), ch. 8"
---

# Secret Leakage Through Derived Artifacts

Getting a secret to a tool safely — an external secrets manager, an
environment variable, [secretless authorization](secretless-authorization.md) —
only protects the *input* path. Many tools then persist what they did
with that secret in a derived artifact of their own: infrastructure
tooling that provisions a resource with a generated or supplied password
commonly records that password, in plaintext, inside its own state or
plan output, because the tool needs the value again on the next run to
know the resource's current configuration. Terraform's state file is the
concrete instance: however carefully a database password was supplied —
`sensitive = true` variables, a KMS-encrypted file, a secrets-manager data
source — the resolved value still lands in plaintext inside
`terraform.tfstate`, because the state file's job is to record the actual
provisioned configuration, secrets included.

**The failure mode this creates**: a team that carefully hardens the
secret's supply path while treating the tool's own output as "just
config" or "just logs" has moved the leak, not closed it. The derived
artifact needs the identical protection profile as a secrets store proper,
because for practical purposes it *is* one:

- **Encrypt it at rest and in transit**, the same baseline
  [encryption](encryption-baseline-controls.md) applies to any store
  holding secret material, not a lighter one because the artifact's
  primary purpose isn't secrets storage.
- **Restrict access as tightly as [least privilege](least-privilege.md)
  would demand for the secrets themselves** — only the pipeline identities
  and the small set of administrators who genuinely need it, not
  "anyone who can read infrastructure config."
- **Audit reads of it**, the same as any other
  [access to sensitive material](audit-log-design.md) — this artifact is
  now on the list of places a secret lives, and an investigation needs to
  be able to ask who read it.

**Generalize the check beyond any one tool**: any process that consumes a
secret and produces a durable output — state files, debug logs, crash
dumps, cached API responses, generated documentation — is a candidate for
this failure. Before trusting a careful secret-supply mechanism, verify
what the consuming tool does with the value afterward; a well-protected
input feeding an unprotected output leaves the secret exactly as exposed
as if it had never been protected on the way in.

**Build logs are the everyday instance most likely to be overlooked.**
CI/CD tools commonly echo the exact commands and variable values they
execute, so a secret passed on the command line or interpolated into a
plan output can end up sitting in plaintext in build history — a store
usually retained far longer, and read by far more people, than anyone
intended for a secret. Tool-native masking (redacting values flagged as
sensitive before they hit the log stream) closes this specific case, but
it's a narrower fix than it looks: masking only catches values the tool
was told to treat as sensitive, so a secret that flows through
unflagged — a derived value, a concatenated string — passes straight
through unredacted. Treat masking as a backstop for the input path, not a
substitute for controlling what the derived artifact retains.
