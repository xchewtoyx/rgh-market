---
type: concept
title: Mandatory Access Control as a Host-Level Defense Layer
description: >
  OS-enforced policy (SELinux, AppArmor) that restricts what a process can
  touch regardless of the user/group permissions it runs under, adding a
  layer defense in depth can fall back on when an application is compromised.
sources:
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Geerling), ch. 10, Server Security and Ansible"
---

# Mandatory Access Control as a Host-Level Defense Layer

Standard user/group/file-permission checks (discretionary access control)
answer only "does this user own or have been granted rights to this file?"
— they say nothing about what a *specific process* should be allowed to do
even while running as an otherwise-legitimate user. Mandatory access
control tools (SELinux on RHEL/Fedora-family systems, AppArmor elsewhere)
add a second, independently enforced policy layer: even a process running
as an authorized user can be confined to exactly the files, sockets, and
capabilities its role requires, so that compromising the process (e.g. via
an application vulnerability) does not automatically grant it everything
that user account could otherwise touch.

This is a concrete instance of [defense in depth](defense-in-depth.md):
it's the layer that still holds if firewall rules, file permissions, and
patched software all fail to stop a given exploit from executing code in
the first place. It composes with, rather than replaces,
[least privilege](least-privilege.md) at the account level and
[compartmentalization](compartmentalization.md) at the network level —
MAC policy is what keeps a compromise confined to what the *specific
process* needed, independent of what the account it runs under is
otherwise entitled to.

The common failure mode is disabling MAC enforcement entirely the first
time it blocks something unexpected, because diagnosing which policy rule
(or "boolean") needs adjusting takes more effort than turning the whole
mechanism off. That trades away a real defense layer for a one-time
convenience; treat an MAC denial as a signal to find and grant the
specific permission the workload needs, not as a reason to remove the
enforcement mechanism.
