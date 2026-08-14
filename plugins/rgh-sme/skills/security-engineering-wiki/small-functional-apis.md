---
type: concept
title: Small Functional APIs
description: >
  Replace broad interactive interfaces with narrow, single-purpose API
  endpoints so least privilege can actually be expressed, enforced, and
  audited.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 5"
  - title: Infrastructure as Code
    resource: "Infrastructure as Code, 3rd Edition (Morris), ch. 12"
---

# Small Functional APIs

"Make each API endpoint do one thing well." Avoid open-ended interactive
interfaces (an SSH shell exposing the whole POSIX API, an endpoint that
accepts a programming language) in favour of small, well-defined
primitives — e.g. CRUD operations on a unique ID. A narrow surface is the
precondition for [least privilege](least-privilege.md): you can only grant
"exactly the permission for this action" if the action exists as a
distinct, nameable endpoint.

Pay particular attention to the **administrative API** — setup/teardown,
maintenance, and emergency endpoints. It is arguably more important than
the user-facing API: typos there cause catastrophic outages, and it is the
most attractive attack surface. Being internal-only, it is also cheaper to
change early — so invest in its design before internal tooling ossifies
around it.

Why size matters:

- A large API exposed to a caller (interactive SSH session against POSIX)
  is nearly impossible to constrain or audit. Naive session auditing —
  bash history, `script(1)` transcripts — only keeps honest people honest:
  an attacker runs `:!/bin/evilcmd` from inside vim and the transcript is
  unreadable ncurses noise. Stronger syscall-level capture is possible but
  hard.
- A small API yields granular [audit logs](audit-log-design.md) ("pushed
  config with hash 123...456") that support strong assertions about what a
  user did or did not do.
- A small API gives an approver in
  [multi-party authorization](multi-party-authorization.md) confidence in
  precisely what they are authorizing.

A worked contrast, distributing a config file to web servers: automation
over full SSH means a bug or credential compromise in the automation *is*
a fleet-wide compromise. Narrow alternatives — reusing the software-update
pipeline, an OpenSSH `ForceCommand` that only accepts a config on stdin, or
a small sidecar/in-process receiver over authenticated RPC — all shrink
what a compromised pusher can do, and enable independent safety checks via
[trust segmentation](trust-segmentation.md).

Even short of narrowing the API itself, the same shrink-the-blast-radius
logic applies to how the pusher authenticates to the fleet it configures.
A single SSH key installed on every server for the configuration tool to
use is a fleet-wide skeleton key: exposing it once compromises every
server at once. A unique key per server instance bounds a single key's
compromise to a single server, at the cost of a harder key-management
problem (the tool now needs access to every server's distinct key without
that access itself becoming as broad as the shared key it replaced).
Dividing the estate into separate security realms — each served by its
own configuration-management instance with access to only that realm's
keys — is the intermediate option: coarser than per-server keys, but it
still bounds a compromise of the configuration tool itself to one realm
instead of the whole fleet. **Pull-based configuration sidesteps the
problem differently**: if each server fetches and applies its own
configuration rather than a central process pushing to it, no server
needs to accept inbound connections from a configuration tool at all —
[attack surface minimization](attack-surface-minimization.md) applied to
the configuration mechanism itself, removing the exposure rather than
scoping the credential that uses it.

When the small API proves insufficient in an emergency, that is what
[breakglass](breakglass.md) is for — and each breakglass use is a signal
that the normal API is missing a needed, safer primitive.
