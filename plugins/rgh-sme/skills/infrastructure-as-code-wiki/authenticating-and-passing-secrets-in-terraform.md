---
type: concept
title: Authenticating and Passing Secrets in Terraform
description: Concrete Terraform mechanisms for provider authentication and resource secrets — environment variables, sensitive variables, encrypted files, and secrets-manager data sources — and why Terraform state and plan files still leak secrets in plaintext regardless.
sources:
  - title: Terraform Up & Running
    resource: "Terraform: Up & Running, 3rd Edition (Yevgeniy Brikman), ch. 6"
---

Two distinct problems fall under "secrets" in a Terraform codebase, each with its own concrete mechanisms in this tool, on top of the general approaches in [handling secrets in infrastructure code](handling-secrets-in-infrastructure-code.md):

**Authenticating Terraform itself to a cloud provider.** For human use, never hardcode credentials in a `provider` block; use provider environment variables (`AWS_ACCESS_KEY_ID`/`AWS_SECRET_ACCESS_KEY`) injected by a short-lived credential wrapper (`aws-vault exec dev-role -- terraform plan`) rather than long-lived static keys sitting in a shell profile. For CI/CD (machine users), the strongest option is OIDC federation — the CI system presents a short-lived, cryptographically-verifiable identity token to the cloud provider's STS-equivalent, which exchanges it for a scoped, temporary credential — avoiding both static keys stored in CI secrets and the narrower applicability of cloud-native instance-profile credentials (which only work when the CI runner itself lives inside that cloud).

**Passing secrets to the resources Terraform provisions**, such as a database password: mark the variable `sensitive = true` (which suppresses it from `plan`/`apply` console output) and supply the value via a `TF_VAR_*` environment variable; decrypt a KMS-encrypted file at plan time (SOPS and similar); or read it directly from a centralized secrets store via a data source, such as AWS Secrets Manager or SSM Parameter Store, decoded with `jsondecode()`.

Whichever mechanism supplies the secret, it ends up in the [Terraform state file](terraform-state-file.md) in plaintext regardless, since Terraform records every resource attribute in state — `sensitive = true` only hides it from console output, not from state or from a saved plan file. This makes encrypting the [remote backend](terraform-remote-backend-and-locking.md) at rest and in transit, and tightly restricting IAM access to the state bucket, a mandatory complement to whichever secret-passing mechanism is used, not an optional hardening step.
