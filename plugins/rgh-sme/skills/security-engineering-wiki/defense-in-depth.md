---
type: concept
title: Defense in Depth
description: >
  Multiple, sometimes redundant defense layers, each designed to catch the
  failures of the previous one — N+1 redundancy for your defenses.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), chs. 1, 8"
---

# Defense in Depth

Defense in depth establishes multiple defense perimeters so attackers have
limited visibility and successful exploits are harder to launch. Sufficient
complexity makes it impossible to demonstrate a system is immune to
compromise; layers exist because you *assume* some defenses will fail. The
core intuition: you don't trust all your capacity to a single router — why
trust a single firewall or any single defense? It is N+1 redundancy for
defenses.

**The Trojan Horse as attack-stage analysis.** Troy fell because every
stage went unopposed. Mapping stages against defenses (the same move as
the [cyber kill chain](cyber-kill-chain.md)):

1. *Threat modeling / vulnerability discovery* — attackers reconnoiter;
   you can't prevent it, so detect it and treat it as signal (monitor
   port/application scans, watch look-alike DNS registrations that presage
   spear phishing, buy [threat intelligence](threat-intelligence.md)).
   Your inside knowledge lets your own assessment beat the attacker's —
   but beware blind spots for vectors you deem unlikely.
2. *Deployment* — the horse arrives at the gate: detect and stop via
   traffic inspection, virus detection, execution control, sandboxes,
   privilege provisioning that flags anomalous use.
3. *Execution* — soldiers emerge: limit blast radius; box the horse in
   (sandboxing, [compartmentalization](compartmentalization.md)).
4. *Compromise* — damage done; response speed now determines how long the
   compromise lasts.

**Layering in practice — Google App Engine** ran untrusted third-party
code inside Google's production network. Defenses stacked so each layer
anticipated the previous layer's failure:

- Removed risky built-in APIs (network and filesystem I/O) and replaced
  them with "safe" versions calling other infrastructure; banned
  user-supplied compiled bytecode and shared libraries so the removals
  couldn't be reintroduced.
- Audited runtime data-object implementations for memory-corruption-prone
  features (yielding upstream fixes) — while assuming the audit would
  miss things.
- Compiled the runtime to Native Client bitcode to block classes of
  memory-corruption and control-flow attacks the audit missed.
- Added ptrace sandboxing to filter unexpected syscalls, terminating the
  runtime and paging at high priority on violation.

Over five years the layers contained every real breakout attempt (all by
researchers), and — a design property worth copying — as an attack
penetrates deeper, the compromise signal gets *stronger*, focusing defender
attention. External researchers still found gaps: layered defense
complements, not replaces, outside scrutiny.

Independent encryption layers are another everyday instance: encrypt at
the application layer even though disks encrypt at device level, so a
flawed drive-controller implementation doesn't expose data to physical
access. Plan every layer for the failure of the outer ones — perimeter
breach, endpoint compromise, [insider](insider-risk.md) attack — and
design with lateral movement in mind, intending to stop it.

At the single-host level, the same principle motivates keeping
[mandatory access control](mandatory-access-control.md) enabled even
though firewalls, patched software, and file permissions already exist —
it's the layer that still confines a compromised process if all of those
fail.
