---
type: concept
title: Public Key Registration
description: >
  An API contract pattern where clients register a public key at account
  creation and later prove identity by signing requests rather than sending
  passwords.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 30"
---

In signature-based authentication, identity means "whoever holds the credential
that established this account." The **client** generates the keypair and keeps
the private key secret; the server must not generate or transmit private keys
(nonrepudiation and interception risk).

Registration is a single atomic create: the client submits a public key; the
server assigns an id (for example user `1234`) and stores the key for later
verification. Minimal surface: `CreateUser` and `GetUser`, with `User`
carrying `id` and `publicKey`. Signing and verification run in client and
server libraries — not as separate API methods.

This replaces username/password on the wire with [request fingerprint](request-fingerprint.md)
signing from account creation onward.
