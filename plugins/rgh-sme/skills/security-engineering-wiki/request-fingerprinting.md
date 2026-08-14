---
type: concept
title: Request Fingerprinting
description: >
  A canonical byte string built from method, path, selected headers, and a
  body digest — the payload actually signed — so client and server agree on
  what was authenticated despite serialization and wire-format differences.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 30"
---

# Request Fingerprinting

[Digital signatures for request
authentication](digital-signatures-for-request-authentication.md) bind
to a specific message, but "the message" for an HTTP API is not just the
body. Signing the raw body alone fails for two structural reasons:

- **Serialization is not canonical.** JSON property order, encoding, and
  normalization differ between implementations while remaining
  semantically identical — signatures operate on raw bytes, so signer and
  verifier must produce the same byte sequence or verification spuriously
  fails.
- **The request is more than its body.** An HTTP DELETE has an empty body
  but the action lives in the verb and URL; other context (timestamps,
  host) matters for [integrity](request-authentication-properties.md)
  and replay rejection.

A **request fingerprint** is the canonical string both parties sign and
verify. Typical components:

| Component | Role |
| --- | --- |
| `(request-target)` | Lowercase method plus path (e.g. `patch /chatrooms/1`) — captures verb and resource without relying on body |
| `host` | Which service the request targets |
| `date` | Request timestamp — enables rejecting stale/replayed requests |
| `digest` | Hash of the body rather than the body itself |

**Digest header instead of signing the full body.** Large bodies make
signing expensive; compute a hash (e.g. SHA-256), Base64-encode it, and
place it in a `Digest` header prefixed with the algorithm name (`SHA-256=<base64>`).
The server recomputes the body hash first and rejects immediately on
mismatch — a cheap [integrity](request-authentication-properties.md)
check before signature verification.

**Assembling the fingerprint.** Take an ordered list of component names
(e.g. `(request-target)`, `host`, `date`, `digest`), lowercase each
header name, and join as `header: value` lines separated by `\n`. This
ordered string is what gets signed.

**Signature header metadata.** The wire request must carry enough
metadata for the server to rebuild the identical fingerprint:

- `headers` — ordered list of components used (order matters)
- `keyId` — which registered public key to use (often the user ID from
  registration)
- `algorithm` — e.g. `rsa-sha256`
- `signature` — the signature bytes

These assemble into a `Signature` header as comma-separated quoted
`key="value"` pairs. The actual header order on the wire does not matter
— only the order recorded in the `headers` field governs fingerprint
construction.

**Server verification sequence:**

1. Recompute the body digest; reject if it does not match the `Digest`
   header.
2. Parse the `Signature` header into its fields.
3. Rebuild the fingerprint using the header list from the signature
   metadata.
4. Look up the public key for `keyId`.
5. Verify the signature against the fingerprint with that public key.

Getting any step wrong — especially canonicalization — produces
intermittent auth failures that look like client bugs but are really
protocol mismatches. Treat the fingerprint spec as part of the API
contract, not an implementation detail.
