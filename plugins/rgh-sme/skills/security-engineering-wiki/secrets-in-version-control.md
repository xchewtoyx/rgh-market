---
type: concept
title: Secrets Committed to Version Control Are Compromised
description: >
  A secret that ever touched version control history must be treated as
  leaked and rotated, because encrypting or deleting it afterward does not
  remove it from history that others may already hold.
sources:
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Geerling), ch. 5"
---

# Secrets Committed to Version Control Are Compromised

Passwords, API keys, and private keys should never live as plaintext in a
repository: anyone with read access to the repo, or to any clone or
mirror of it, can read not just the current state of a file but its full
history. Deleting the secret in a later commit does not remove it — the
old commit, and the secret in it, persists in every clone that already
exists.

This makes the fix-after-the-fact instinct a trap: encrypting a
previously-plaintext secret in place (with a tool such as Ansible Vault,
or any file-level encryption) protects it going forward, but does nothing
about the plaintext value sitting in earlier commits. The only correct
response to a secret that ever touched history unencrypted is to treat it
as disclosed and [rotate](credential-rotation.md) it — history rewriting
(rebasing out the offending commit) is not a substitute, since any fork,
clone, or CI cache made before the rewrite still holds the old history.

**Keep secrets out of version control from the start**, via one of two
architectures:

- **An external secrets manager** (a KMS, or a dedicated service such as
  HashiCorp Vault or a cloud provider's secret store) — the repository
  holds only a reference (a key name or ARN), and the secret value is
  fetched at deploy or run time over an authenticated channel.
- **A repository-embedded, encrypted-at-rest secret** — the encrypted
  blob is safe to commit; the decryption password or key is stored
  separately (never in the same repo) and supplied out-of-band (an
  environment variable, a password file with restrictive permissions, or
  an interactive prompt) at the point of use. Secrecy then depends
  entirely on that separately-held key, so managing and protecting it
  becomes the real problem — see [secure cryptographic
  apis](secure-cryptographic-apis.md) for what "protecting a key" needs
  to mean.

Both architectures share the same underlying rule this note captures:
persistent, shared storage that a security review cannot fully enumerate
the readers of (a git history, a backup, a log) should never hold a
plaintext secret, because you cannot later un-disclose it. Where the
platform supports it, [secretless authorization](secretless-authorization.md)
goes a step further and removes the secret from the picture entirely,
rather than finding a safer place to keep it.
