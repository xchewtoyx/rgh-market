---
type: concept
title: Idempotency as a Requirement for Safe Automation
description: >
  Automation that isn't idempotent can leave a system in an inconsistent,
  half-configured state when it fails partway through, so anything designed
  to run unattended must be safe to retry or re-run from any point.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 7, 24"
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Unmesh Joshi), ch. 15 (Idempotent Receiver)"
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 10 (Define Errors Out of Existence)"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 27"
---

# Idempotency as a Requirement for Safe Automation

A script that fails halfway through a multi-step change leaves the system in
whatever state the completed steps produced — not the starting state, and
not the intended end state. If a human was driving, they'd notice the
failure and decide how to recover. Once the same script is triggered by a
scheduler or another service instead of a human, that judgment call
disappears: the next run needs to be able to pick up from an arbitrary,
possibly half-completed state and still reach the correct end state, rather
than assuming it's starting clean.

This is why idempotency stops being a nice-to-have once automation moves
past the "human runs it and watches" stage of the [automation maturity
spectrum](automation-maturity-spectrum.md) — a non-idempotent operation
retried automatically after a partial failure can actively make things
worse rather than converging on the correct state. It's one half of what
makes automation safe to run unattended; the other half is bounding how much
damage a single run can do if something does go wrong, which is what
[safeguards against runaway automation](safeguards-against-runaway-automation.md)
and [failure domain amplification](failure-domain-amplification.md) cover.

Automated schedulers make this concrete: a distributed cron system that
elects a new leader after a failure has to decide, from a persisted
execution log, whether a job whose run status is unknown should be
re-triggered or skipped — and that decision is only ever safe to make
automatically if running the job twice is no worse than running it once.
Without that guarantee, leader failover turns into either silently skipped
work or a duplicate run, and the system has no way to tell honestly which
one just happened.

Idempotency only makes a *repeated* action harmless, though — it does
nothing for the case where the old leader isn't repeating the same
decision but acting on stale information the new leader has already
overridden. That distinct failure mode needs its own guard; see [fencing
tokens against zombie actors](fencing-tokens-against-zombie-actors.md).

Not every action is naturally idempotent the way "set this key to this
value" is — an action like "create a lease" or "provision a resource"
legitimately fails as a duplicate the second time it runs, which is
exactly wrong if the first attempt actually succeeded and only its
*response* was lost before the caller saw it: the caller retries, gets a
"duplicate" error, and misreads that as "my request never went through."
For actions like this, safe automatic retry needs explicit deduplication,
not just an operation that happens to tolerate repetition: give each
calling actor a stable identity and have every request it sends carry a
monotonically increasing request number; the receiver stores the result
of each (identity, request number) pair it executes, and on seeing that
pair again returns the stored result instead of re-running the action.
This turns "retry until you get an answer" into a safe default for any
action, not just the subset that's naturally idempotent by luck of its
own semantics — at the cost of needing to expire old dedup entries once
the caller has confirmed it received them (or once the actor's session
itself is presumed dead), so the dedup table doesn't grow without bound.

An alternative to that bookkeeping — and often the better fix — is to
redefine what the action actually *means* so a repeat is no longer a
distinct case to detect at all. An operation defined as "delete this
resource" has to fail (or track dedup state) if run twice, because the
resource is legitimately gone the second time; the same operation
redefined as "ensure this resource does not exist" is trivially,
definitionally idempotent, because "already absent" is just the normal
successful outcome, not an error. The same reframing applies to most
automation actions: "create this record" (fails on retry) versus "ensure
this record exists with this content" (succeeds identically every time);
"start this service" versus "ensure this service is running." Automation
built around these ensure-style, state-defined operations doesn't need
per-request deduplication at all for the common case — retries just
converge to the same end state on their own. This is the same principle
behind [convergent orchestration](convergent-vs-direct-orchestration.md):
declaring and re-asserting a desired state is inherently safer to repeat
than issuing an imperative one-time command.

On [managed compute](pets-vs-cattle.md), idempotency becomes a client
requirement as well as a server one: service discovery and load balancing
mean backends can disappear mid-request, so callers must retry — and
mutating retries must be safe. Client-assigned identifiers (an order ID
generated before the first attempt) let the server recognize and dedupe a
repeat. A subtler duplication source is scheduler split-brain: contact
with a machine is lost, work is rescheduled elsewhere, then the original
machine returns — two instances both believe they are the same replica
until the address-resolution layer disambiguates. Whichever instance is
not referenced there must terminate, but until then both may serve traffic;
see [fencing tokens against zombie
actors](fencing-tokens-against-zombie-actors.md) for the general pattern
of rejecting stale authority, and idempotent handlers for surviving the
duplicate requests that interval produces.
