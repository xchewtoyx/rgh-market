---
type: concept
title: Mandatory Code Review as Multi-Party Authorization
description: >
  Requiring a second person to review every change before it merges is a
  security control, not just a quality practice — it ensures no single
  individual can unilaterally introduce a change, and it must be genuinely
  mandatory and substantive to provide that guarantee.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 14"
---

# Mandatory Code Review as Multi-Party Authorization

Code review is usually framed as a quality practice — catching bugs,
spreading knowledge, keeping style consistent. It's also a security control:
requiring a second person's approval before a change merges means no single
account, however it was obtained, can unilaterally introduce a change to the
system. This is a form of multi-party authorization.

## Two conditions for it to actually work as a control

- **It must be mandatory, with no opt-out.** An adversary who can simply skip
  review when convenient isn't deterred by a review process that exists on
  paper.
- **It must be substantive, not a rubber stamp.** The reviewer has to
  actually understand the change and its implications, asking the author for
  clarification when needed — a review that approves without genuinely
  evaluating the change provides none of the security benefit, even though it
  satisfies the mandatory-approval requirement literally.

## Limitations

Code review doesn't protect against collusion between multiple insiders, or
against an external attacker who has compromised more than one insider
account. It's best treated as one layer of defense-in-depth alongside
automated testing (see [automated acceptance testing](automated-acceptance-testing.md))
and [software supply chain threat modeling](software-supply-chain-threat-model.md)
more broadly — not a control that, on its own, is assumed sufficient.

This same requirement applies to configuration changes, not just application
code — see [configuration management](configuration-management.md).
