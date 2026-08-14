---
type: concept
title: Snowflake Servers
description: A system that has been hand-configured through undocumented, ad-hoc changes to the point that it cannot be reliably recreated from any written record.
sources:
  - title: "Ansible for DevOps"
    resource: "Ansible for DevOps (Geerling), ch. 1"
  - title: "Continuous Delivery"
    resource: "Continuous Delivery (Humble, Farley), ch. 1"
  - title: "Infrastructure as Code"
    resource: "Infrastructure as Code (Morris), ch. 2"
---

A "snowflake server" is a system whose current configuration exists only as the accumulated result of manual, one-off changes — an admin logging in and adjusting something, repeated over months or years, with no record of what was changed or why. Each one is unique ("no two alike") and, critically, unreproducible: if it were destroyed, no one could rebuild an equivalent from documentation, because the documentation never existed in the first place.

## Why This Is a Handover Failure Mode, Not Just a Technical One

A snowflake server is the terminal case of the question this domain exists to answer: can someone who wasn't involved safely operate, maintain, or change this system? For a snowflake, the answer is no by construction — there is no artifact, written or executable, that captures what the system actually is. Tribal knowledge lives only in the head of whoever made the last undocumented change, and it leaves when they do.

Ad-hoc shell scripts partially help (they at least record *some* of the steps taken) but typically don't handle every edge case of keeping multiple servers in sync, and they degrade into the same problem once they accumulate enough manual patches and exceptions.

See [Infrastructure-as-Code Properties for Safe Change](iac-properties-for-safe-change.md) for the specific discipline of backporting emergency out-of-band changes into code before they can silently accumulate into a snowflake.

## Remedies

- **Make the definition the source of truth**: declarative, machine-applied configuration means the definition and the running system are the same artifact, so there is nothing left to reconstruct from memory — see [Self-Documenting Declarative Systems](self-documenting-declarative-systems.md). Applied specifically to servers, this is the [phoenix server pattern](phoenix-server-pattern.md): a machine disposable and rebuildable from scratch on demand.
- **Design the system to need less tribal knowledge in the first place**, rather than relying on someone eventually writing it all down after the fact — see [Reducing Documentation Need Through System Design](reducing-documentation-need-through-system-design.md).
