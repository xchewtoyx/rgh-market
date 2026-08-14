---
type: concept
title: Digital Signatures for Request Authentication
description: >
  An asymmetric keypair lets each request carry cryptographic proof of
  origin and integrity that a third party can verify — something shared
  secrets and HMAC cannot provide.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 30"
---

# Digital Signatures for Request Authentication

A digital signature is a byte string that, beyond reasonable doubt, can
only have been produced by someone holding one half of a special
credential pair — and can be verified with the other half. The defining
property is **asymmetry**: the credential that *generates* a signature
(the private key) is not the credential that *verifies* it (the public
key); each role has a single holder.

Why this satisfies the three [request authentication
properties](request-authentication-properties.md):

- **Origin** — only the private-key holder can produce a valid signature,
  so possession of the private key *is* the identity proof (there is no
  secondary check like a photo ID).
- **Integrity** — the signature is bound to the signed message; any
  change to the message invalidates the signature.
- **Nonrepudiation** — only one party holds the private key, so that
  party cannot later claim the signature was forged; a verifier (including
  a third party with the public key) needs no cooperation from the
  server. This is the structural reason
  [nonrepudiation](nonrepudiation.md) demands asymmetric credentials.

**Shared secrets and HMAC** are acceptable when the server is the only
verifier and requests never need to be proven to an outsider — both
parties hold the same key, so either could have produced the MAC. That
symmetry is fine for server-to-server authentication where
[nonrepudiation](nonrepudiation.md) is not required, but fails the
moment a disinterested third party must attest that user 1234 — not the
API operator — originated a specific request.

The high-level lifecycle:

1. The user (not the server) generates a public-private keypair and
   keeps the private key secret — see [identities for active
   entities](system-identities.md) for why server-side generation
   undermines nonrepudiation.
2. The user registers with the API by submitting the public key; the
   server assigns an identifier and stores the public key for later
   verification.
3. The user signs every request with the private key; the server
   verifies with the stored public key.

What to sign is not obvious — signing only a JSON body fails on
canonicalization and ignores method, path, and headers. Production
implementations build a canonical [request
fingerprint](request-fingerprinting.md) as the signed payload. Use
[secure cryptographic APIs](secure-cryptographic-apis.md) for the
signing primitives rather than assembling algorithms by hand.
