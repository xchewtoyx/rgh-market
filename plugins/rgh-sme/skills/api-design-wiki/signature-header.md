---
type: concept
title: Signature Header
description: >
  Wire metadata that records how a request fingerprint was built and carries
  the digital signature for server-side verification.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 30"
---

After computing a [request fingerprint](request-fingerprint.md), the client
signs that canonical string and attaches a `Signature` header. The server must
reconstruct the identical fingerprint, so the header records **how** it was
built:

| Field | Role |
| --- | --- |
| `headers` | Ordered list of headers used in the fingerprint — order matters |
| `keyId` | Which registered public key verifies the signature (often the user id) |
| `signature` | The digital signature bytes (encoded for transport) |
| `algorithm` | Signing algorithm (for example `rsa-sha256`) |

Format: comma-separated quoted `key="value"` pairs, for example:

```
keyId="1234",algorithm="rsa-sha256",headers="(request-target) host date digest",signature="..."
```

The client also sets `Digest` (body hash) and `Date`. Actual header order on
the wire does not matter because the `headers` field inside `Signature`
defines fingerprint order.

Server verification: confirm `Digest` matches the body; parse `Signature`;
recompute the fingerprint with the declared header list; load the public key
for `keyId`; verify the signature against the fingerprint.

This describes the **authentication surface of the message** — where
credentials and proof live on the wire — not identity lifecycle or threat
modelling.
