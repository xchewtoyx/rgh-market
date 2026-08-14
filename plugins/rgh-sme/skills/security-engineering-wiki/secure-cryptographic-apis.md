---
type: concept
title: Secure Cryptographic APIs
description: >
  Crypto misuse by non-experts is the norm, so give engineers libraries
  like Tink that are hard to misuse, refuse raw key material, and build in
  rotation — while knowing what such libraries cannot prevent.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 6"
---

# Secure Cryptographic APIs

Cryptographic primitives have catastrophic failure modes invisible to
non-experts: combine a standard, secure cipher like AES subtly wrongly
with authentication and an attacker observing only accept/fail responses
can use your service as a decryption oracle. Experience says crypto code
not written and reviewed by experienced cryptographers commonly has
serious flaws — using crypto correctly is really, really hard.

The remedy is the [safe-types](safe-types.md) philosophy applied to
crypto: an API that is hard to misuse. Google's Tink design principles:

- **Secure by default** — e.g. the API makes AES-GCM nonce reuse (a
  subtle, common, authenticity-destroying mistake) impossible; built on
  proven, well-tested primitive implementations.
- **Usability** — engineers work with well-understood abstractions like
  "authenticated encryption (AEAD)" rather than primitive knobs.
- **Readability/auditability** — employed schemes are visible in code and
  centrally controlled.
- **Agility** — built-in [key rotation](credential-rotation.md) and
  deprecation of broken schemes.
- **Key management integration** — the API *does not accept raw key
  material*, steering users to KMS services instead of keys on disk or in
  source code; keyhunt/password-hunt sweeps never fully clean a codebase
  that made raw keys easy.

**Know what the library does not guarantee.** Tink prevents low-level
misuse, not design-level mistakes: hashing credit-card or Social Security
numbers "for protection" fails because the input space is small — the
right tool was authenticated encryption, and no crypto library choice
detects that. Likewise a secure-by-construction web framework prevents
XSS but not business-logic bugs. Reviewers must understand precisely
which properties a framework guarantees and which remain the
application's problem.
