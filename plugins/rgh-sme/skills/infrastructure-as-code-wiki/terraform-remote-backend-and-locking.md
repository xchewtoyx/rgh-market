---
type: concept
title: Terraform Remote Backend and State Locking
description: Storing Terraform state in managed, encrypted cloud storage with distributed locking, rather than locally or in Git, so concurrent applies can't corrupt it.
sources:
  - title: Terraform Up & Running
    resource: "Terraform: Up & Running, 3rd Edition (Yevgeniy Brikman), ch. 3"
---

A remote backend stores the [Terraform state file](terraform-state-file.md) in managed cloud storage rather than a local file or Git, addressing state's need for durability, encryption, and — critically — locking. The canonical AWS implementation pairs an S3 bucket (with versioning enabled, so a corrupted state can be rolled back, and server-side encryption at rest) with a DynamoDB table used purely for distributed locking: Terraform writes a lock record keyed on `LockID` before an operation and releases it after, so a concurrent `plan` or `apply` from someone else fails immediately with a lock error instead of racing.

Bootstrapping a remote backend is a two-stage process, since the backend infrastructure itself needs somewhere to keep its own state: write the code that creates the S3 bucket and DynamoDB table and apply it with local state first, then add the `backend "s3"` block to the same configuration and run `terraform init` again, which detects the new backend and offers to migrate the existing local state into it.

Remote backend encryption addresses data at rest, but does not by itself solve the plaintext-secrets problem — state still holds every resource attribute unencrypted once decrypted for use, so access to the backend bucket itself needs strict IAM controls; see [authenticating and passing secrets in Terraform](authenticating-and-passing-secrets-in-terraform.md) for the fuller picture. Locking prevents *simultaneous* applies, but does not prevent someone applying an outdated, divergent version of the code after waiting their turn for the lock — the same problem [applying code from a centralized service](applying-code-from-a-centralized-service.md) addresses more generally.
