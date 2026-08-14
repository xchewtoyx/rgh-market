---
type: concept
title: Handling Secrets in Infrastructure Code
description: Four complementary approaches — encryption, secretless authorization, runtime injection, and disposable secrets — for keeping passwords and keys out of infrastructure source code while still making them available where needed.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 7"
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), ch. 5"
---

Infrastructure code often needs secrets — credentials to call a platform API, a password to provision into a database. Secrets must never be committed in plaintext to [version control](version-control-for-infrastructure-code.md): even a private repository leaks history, forks, and backups too easily, and leaked secrets in source are one of the most common causes of security breaches. Four approaches, often combined, keep secrets out of code while still making them usable:

- **Encrypting secrets** — tools such as git-crypt, blackbox, sops, and transcrypt let you commit an encrypted secret to the repository; the decryption key itself must live somewhere else, via one of the other approaches. Ansible's own built-in Vault is a tool-specific instance of this same approach: it encrypts a variables file (or any other file it can reference — role defaults, host/group vars, even a task include) in place with a password the author supplies out of band, and decrypts it in memory only at apply time given that same password, supplied interactively, from a locally-stored password file, or from an executable that prints it. Its security is bounded entirely by how well that password is kept secret, and — like any commit-then-encrypt approach — encrypting a secret that was previously committed in plaintext does not remove the plaintext from version-control history, so the underlying credential must still be rotated.
- **Secretless authorization** — many platforms let you authorize an action without a secret at all, by attaching an identity to a compute instance (for example, an AWS IAM instance profile) so a stack tool running there is simply permitted to act, or by authorizing connections based on network identity rather than a shared password. This shifts the attack surface to protecting the privileged instance itself, rather than removing risk outright, but it does remove one more secret that could leak from somewhere else.
- **Runtime secret injection** — supplying the secret as a [stack instance parameter](stack-parameter-design-principles.md) at apply time rather than baking it into code: read from a local, uncommitted file during local development, or pulled from CI/CD agent secret storage or a [configuration registry](configuration-registry.md) for unattended runs.
- **Disposable secrets** — generating a secret on the fly and using it on a need-to-know basis, so no human or long-lived store ever needs to hold it; for example, a database-provisioning stack generates a password and hands it directly to the application-server stack that needs it, or a secrets management service like HashiCorp Vault mints and rotates credentials automatically. One-time passwords are the extreme version of this idea.

Which of the [stack configuration patterns](stack-parameter-design-principles.md) you use for ordinary parameters constrains which of these secret-handling techniques fits naturally — for example, [stack configuration files](stack-configuration-files-pattern.md) committed to source control can never hold secrets directly, while a [stack parameter registry](stack-parameter-registry-pattern.md) or [pipeline stack parameters](pipeline-stack-parameters-pattern.md) can integrate with a secrets manager for injection at apply time.
