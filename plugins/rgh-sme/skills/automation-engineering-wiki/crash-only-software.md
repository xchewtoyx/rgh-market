---
type: concept
title: Crash-Only Software
description: >
  Deliberately omitting a graceful shutdown/startup path so the only way to
  stop or start a component is through its crash-recovery code, forcing
  that recovery path to be exercised — and hardened — on every run.
sources:
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 2"
---

# Crash-Only Software

Orderly startup and shutdown code paths get disproportionately little
testing relative to how critical they are: they run rarely (once per
deploy or maintenance window), so bugs in them surface only during the
exact moments — a crash, a power loss, an automated restart — when the
system can least afford a surprise. Crash-only software (Candea & Fox,
2003) resolves this by removing the orderly path entirely: the only
supported way to stop the software is to crash it, and the only supported
way to start it is via the crash-recovery path. There is no separate,
rarely-exercised "clean shutdown" logic to rot from disuse, because there
is no such logic at all — recovery is exercised on every single start,
constantly proving (or breaking loudly) that it still works.

This is a direct, structural answer to the same problem that motivates
[fire drills and other deliberately exercised
safeguards](confidence-decay-in-unpracticed-safeguards.md): rather than
scheduling periodic practice to keep a rarely-used recovery path trustworthy,
crash-only design makes the recovery path the *only* path, so it is
exercised by construction rather than by discipline. It also composes
naturally with [self-healing](self-healing-overload-response.md) designs
and with automated process supervisors that restart a failed component —
the supervisor doesn't need a separate "was this a clean or dirty exit"
branch, because every restart is handled identically. The precondition for
this to be safe is the same one [idempotent
automation](idempotency-in-automation.md) needs: recovery has to reach a
correct end state regardless of what state the crash left behind, since
that is now the *only* startup path the system ever runs.
