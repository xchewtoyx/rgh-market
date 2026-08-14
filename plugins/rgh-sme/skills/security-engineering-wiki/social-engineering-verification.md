---
type: concept
title: Out-of-Band Verification of Credential Requests
description: >
  Treat any unexpected request for credentials or sensitive access as
  suspicious by default and confirm it through a separate channel before
  acting, since a phone call is cheaper than a breach.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 10"
---

# Out-of-Band Verification of Credential Requests

A social-engineering attempt almost always looks, on its face, like a
routine request — a message from "IT," an urgent email from "a coworker"
asking for a password reset link to be clicked, a call from someone
claiming to need account details to fix a problem. The individual on the
receiving end is the actual control here: treat any request touching
credentials, secrets, or sensitive access as suspicious by default,
regardless of who appears to be asking, and verify it through a channel
different from the one the request arrived on — a phone call or an
in-person check — before acting. The asymmetry is the whole argument: a
quick verification call is cheap; a ransomware payload triggered by one
click is not.

This is the human-layer instance of the same reasoning
[attacker TTPs](attacker-ttps.md) formalizes at the technical layer:
attackers have a catalogue of concrete methods for extracting credentials
that don't require breaking any technical control at all, because the
person holding the credential is the easier target. It also runs in the
opposite direction from [insider risk](insider-risk.md)'s trusted-access
framing — here the concern is an external party impersonating a trusted
identity to borrow the access that identity would legitimately have.

Structurally, this individual-level habit is what [least privilege](least-privilege.md)
and [breakglass](breakglass.md) processes assume is in place: those
controls limit what a successfully phished credential can do, but they
don't prevent the phish itself — that first line of defense is a person
declining to act on an unverified request.
