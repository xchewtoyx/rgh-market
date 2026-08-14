---
type: concept
title: Network Exposure Misconfiguration
description: >
  Default-open network and storage configuration — public buckets, SSH
  open to the entire internet — is a self-inflicted attack surface that
  whitelisting by default eliminates.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 10"
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 9"
---

# Network Exposure Misconfiguration

A large share of real breaches trace not to a sophisticated exploit but to
plainly open exposure that nobody meant to leave open: a storage bucket
readable by anyone on the internet, a compute instance with inbound SSH
open to `0.0.0.0/0`, a database accepting inbound connections from any
address. None of these require an attacker to defeat a control — there
was no control to defeat. Scale matters here: a 2015 scan found 30,000+
publicly exposed MongoDB instances — over 595 TB of data — reachable
because the default configuration bound to `0.0.0.0` rather than
localhost; a single vendor default, left unchanged across thousands of
independent deployments, is what turned one misconfiguration into a
class of breach. This is the concrete, everyday form the
[cloud shared responsibility model](cloud-shared-responsibility-model.md)
warns about: the provider did not fail, the customer left the door open.

The structural fix is to always know exactly which IPs and ports are open,
to whom, and why, and to default to **whitelisting**: allow only the
specific systems or users that need access, rather than opening a
connection broadly "just in case" or "for convenience." This is the same
posture [zero trust networking](zero-trust-networking.md) takes at the
identity layer — no ambient access from being merely present on a network
— applied here at the perimeter-configuration layer instead. It addresses
*who can reach* a given port; whether the port or the service behind it
should exist at all is the companion question
[attack surface minimization](attack-surface-minimization.md) asks.

Encryption in transit does not substitute for this control: HTTPS
protects data on the wire but does nothing if the storage behind it is
itself left publicly reachable (see
[encryption as a baseline control](encryption-baseline-controls.md)).
Treat exposure review as a standing, recurring check rather than a
one-time setup step — misconfiguration accumulates as systems change, and
the [access classification by risk](access-classification-by-risk.md) a
system was designed against can silently drift if nothing re-verifies
that only the intended callers can actually reach it.
