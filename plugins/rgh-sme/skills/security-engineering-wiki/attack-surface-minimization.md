---
type: concept
title: Attack Surface Minimization
description: >
  Remove software, services, and open ports a system does not actively need,
  because anything running is something an adversary can try to exploit.
sources:
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Geerling), ch. 10, Server Security and Ansible"
---

# Attack Surface Minimization

Every installed package, running service, and open port is a potential
entry point, whether or not it is ever used for its intended purpose. A
host running software nobody needs anymore — a stale package, a forgotten
cron job, a port opened for a one-off debugging session and never closed —
gains nothing from carrying it, but hands an adversary one more thing to
probe. The framing worth carrying into design and review: infrastructure
is only as hard to breach as its single weakest, most exposed member —
one under-hardened host is often the whole entry point into an otherwise
well-defended network.

The structural fix is to actively remove what isn't needed rather than
merely leaving it unused: uninstall unused packages, close ports that
don't serve active traffic, and prune stale automation and jobs — treat
"we might need it later" as a reason to redeploy when the need actually
arises, not a reason to keep running it now. Configuration-managed,
disposable infrastructure supports this structurally: hosts rebuilt from a
known-good definition don't accumulate the cruft that hand-maintained
servers do over years of ad hoc changes.

This is a design-time complement to
[network exposure misconfiguration](network-exposure-misconfiguration.md),
which addresses *inbound* reachability (who can reach a given port at
all); attack surface minimization addresses whether the port, service, or
package needs to exist in the first place. Both serve the same end as
[least privilege](least-privilege.md) applied to the host itself rather
than to a credential: grant the system only the capabilities its actual
job requires, and treat anything beyond that as unjustified exposure.
