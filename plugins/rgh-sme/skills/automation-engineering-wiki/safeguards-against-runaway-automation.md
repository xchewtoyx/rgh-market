---
type: concept
title: Safeguards Against Runaway Automation
description: >
  Automation capable of acting at scale needs explicit rate limits,
  precondition checks, and an emergency stop built in, so a bug or bad
  input can't run to completion unchecked before a human can intervene.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 7"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 6"
  - title: "Building Secure and Reliable Systems"
    resource: "Building Secure and Reliable Systems (Google), ch. 8"
  - title: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Nygard), ch. 17"
---

# Safeguards Against Runaway Automation

Once automation is trusted to act without a human reviewing each step, the
question shifts from "did this run correctly" to "how much damage can a
single run do before something stops it." Designing for that means building
in, up front:

- **Rate limits** on how fast the automation can apply changes, so a bug
  produces a slow, noticeable trickle of damage instead of an instant
  fleet-wide one — see the [Governor pattern](governor-pattern.md) for a
  concrete implementation of this.
- **Safety checks** that validate preconditions before each action, rather
  than trusting the input or the previous step blindly. Deciding what a
  safety check does when it *can't* determine whether a precondition holds
  — serve anyway, or refuse — is the [failing safe vs. failing
  secure](failing-safe-vs-failing-secure.md) tradeoff.
- **An emergency pause or stop** — a way to halt a run already in progress,
  not just prevent starting a new one.
- **A change budget bounding scope, not just rate** — a cap on the
  magnitude or breadth of unsupervised change automation can make (e.g. one
  server shedding all its traffic is fine, but no automatic policy should
  let *all* servers shed traffic at once) — when the budget is exhausted,
  automation stops making changes and a human has to decide whether to
  raise the budget or intervene some other way. Automation stays in place
  throughout; only its authority to keep acting unsupervised is what runs
  out. This is a deliberate foothold for humans: automated response
  mechanisms should always leave a path for a human to step in on
  circumstances the automation's rules never anticipated, since a
  rule-based system's judgment is inherently limited to the cases its rules
  cover — expecting rules to eventually cover every case is the [fallacy of
  predetermination](fallacy-of-predetermination.md).

These safeguards exist specifically to bound [failure domain
amplification](failure-domain-amplification.md): they don't make the
automation less buggy, they make sure a bug's effects stay small and
recoverable instead of instantaneously global. They're complementary to,
not a substitute for, making the automation
[idempotent](idempotency-in-automation.md) — idempotency handles safe retry
after a partial failure, these safeguards handle bounding the failure
itself while it's happening.

They also don't need to arrive all at once. Google's rollout of automated
datacenter network repair went through an interim stage where the
automation handled risk assessment and the drain/undrain steps but skipped
verification for links judged low-risk — an intentionally imperfect
safeguard, accepted as a reasonable tradeoff to ship the higher-value parts
of the automation sooner, with the gap closed later once the automation had
proven itself. Automation that reaches this level of trust also stops
being "fire and forget": it needs the same ongoing ownership as any other
production system, including deliberate transfer of the operational
knowledge behind its safety limits as the engineers who built them rotate
off the team — a safeguard nobody remembers the reason for is one step
away from being removed for being "unnecessary." It also rarely gets
removed in one dramatic step — see [normalization of deviance via
decrementalism](normalization-of-deviance-via-decrementalism.md) for how a
safety limit typically erodes instead: through a long sequence of small,
individually-defensible loosenings that each pass review by comparison to
the value right before them, never to the original rationale.

These safeguards are usually designed per system, but a system that's safe
in isolation can still misbehave once it's one of several automated
systems reacting to each other — see [interacting automated control
loops](interacting-automated-control-loops.md). A related failure mode is
a single automated actor duplicating itself: a control-loop instance
presumed dead by a failure detector can wake up and keep acting on stale
authority after a replacement has already taken over — see [fencing
tokens against zombie actors](fencing-tokens-against-zombie-actors.md).

A narrower but common version of runaway automation is retry logic itself
becoming the problem: automation that keeps retrying a failing dependency
without limit can turn that dependency's brief blip into a sustained
outage, simply by adding load exactly when it can least be absorbed. See
[circuit breaker for automated
retries](circuit-breaker-for-automated-retries.md) for the specific
safeguard that bounds this.

Automated fault-injection ("chaos engineering") tools need the exact same
safeguards, just aimed at deliberately breaking things instead of fixing
them: start with a small blast radius (a single non-critical service in
staging, or a low-traffic canary), expand gradually only once each step is
verified safe, and always ship an automated kill switch that aborts the
experiment instantly if a real safety metric degrades. A fault-injection
tool without these same safeguards is itself an instance of runaway
automation — one deliberately triggered rather than accidental. It's also
the concrete mechanism for [keeping unpracticed safeguards from decaying
silently](confidence-decay-in-unpracticed-safeguards.md): the whole point
of scheduling deliberate fault injection is to prove a failover or
countermeasure still works before a real incident is the first time it's
exercised since it was built.
