---
type: concept
title: Out-of-Band Change Remediation
description: The discipline of immediately backporting an emergency manual fix made directly to running infrastructure back into version-controlled code, so the fix doesn't become invisible, permanent configuration drift.
sources:
  - title: Infrastructure as Code Patterns and Practices
    resource: "Infrastructure as Code, Patterns and Practices (Rosemary Wang), ch. 2"
---

An out-of-band change is a fast, mutable fix applied directly to a running system outside the normal code-and-pipeline process — hotfixing a firewall rule or a package version during an incident, when there's no time to wait for a full [delivery pipeline](infrastructure-delivery-pipeline.md) run. This is sometimes genuinely the right call under incident pressure, but it's also exactly how [configuration drift](configuration-drift.md) starts: the running system and the version-controlled code that's supposed to describe it now disagree, and if nothing corrects that, the next ordinary code change risks reverting the fix, or the fix becomes an undocumented, only-in-one-place [snowflake](snowflake-system.md) characteristic.

Remediation closes this gap immediately: as soon as the emergency is over, the actual change made out-of-band gets backported into the IaC configuration and committed, so version control and reality agree again, and the next normal pipeline run won't silently undo the fix. This preserves the reproducibility and idempotency the rest of the practice depends on, rather than letting emergency response quietly accumulate untracked exceptions.

This is the specific "close the loop" half of a broader discipline — see [normalizing the emergency fix process](governance-in-pipeline-based-workflow.md) for the complementary idea that if a step can safely be skipped in an emergency, it should be examined for removal from the normal process too, and the [three D's troubleshooting framework](three-ds-troubleshooting-framework.md), which lists checking for drift caused by exactly this kind of unremediated out-of-band change as the first thing to investigate when a later change fails unexpectedly.
