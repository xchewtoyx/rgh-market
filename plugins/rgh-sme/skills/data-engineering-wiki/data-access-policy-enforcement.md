---
type: concept
title: Data Access Policy Enforcement
description: >
  Enforcing who can access what data at the access point itself — an API, a
  virtualization layer — rather than trusting every consumer to comply with
  a written policy.
sources:
  - title: Deciphering Data Architectures
    resource: "Deciphering Data Architectures (Serra), ch. 11"
---

A [data governance program](data-governance-program.md) can write down rules
about who is allowed to access what data, how it may be used, and when
access should be granted or denied — covering classification, authentication
and authorization, encryption, retention, and disposal. Writing the rules
down is necessary but not sufficient: a rule that lives only in a document
depends on every consumer independently knowing about it and choosing to
comply.

**Data access policy enforcement** closes that gap by routing every request
for data through a mechanism — an API, a driver, or a
[data virtualization](data-federation-and-virtualization.md) layer — that
checks the request against policy before granting access, rather than
letting consumers reach storage directly. A healthcare organization
restricting patient-record access to authorized medical staff, verified by
an API that checks credentials before returning any data, is the canonical
shape: the policy is enforced structurally, at the one path every request
must pass through, instead of relying on every downstream tool and query
tool to individually respect an access rule it may not even know exists.

The distinguishing feature versus table- or row-level security configured on
one specific storage engine: a policy enforcement point sits in front of
*every* access path a consumer might use (API, virtualization, direct
connection), so a rule holds regardless of which tool or route a given
consumer happens to use to reach the data — not just the one path someone
remembered to lock down.
