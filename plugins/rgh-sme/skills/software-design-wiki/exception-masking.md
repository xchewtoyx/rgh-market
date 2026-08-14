---
type: concept
title: Exception Masking
description: >
  Exception masking detects and fully resolves an exceptional condition at a
  low level so that higher layers never learn it occurred — sometimes the
  best trade-off precisely because there's no useful action any higher layer
  could take.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 10"
---

Canonical example: TCP silently resends lost or corrupted packets so the
reliable-byte-stream abstraction above it never sees packet loss at all.

A more contested example is **NFS**: if a file server becomes unresponsive,
the NFS client transparently retries indefinitely, hanging the calling
application (with periodic "server not responding, still trying" console
messages) rather than surfacing an exception. The common complaint is "NFS
should just error out instead of hanging" — but exposing the error would be
strictly worse. An application has no useful recourse (it can't fix the
server), so it would either retry the operation itself — duplicating the
NFS layer's own retry logic at every single call site — or abort, cascading
into aborting its own callers too and collapsing the user's entire working
environment, which they'd then have to manually restart once the server
recovers. Masking is the better trade-off precisely because there's no good
alternative action available anywhere in the stack; users retain a manual
escape hatch (kill the hung application) if they don't want to wait.

Masking deepens the masking module: its interface shrinks (fewer exceptions
callers need to be aware of) while its functionality grows to include the
masking logic itself. It's a specific instance of
[pulling complexity downward](pull-complexity-downwards.md) — absorb the
handling once, low in the stack, rather than pushing it out to every caller.

Masking is not unconditionally safe — see
[limits of masking and defining away errors](limits-of-masking-errors.md).
It also sits at the opposite end of a spectrum from
[exception aggregation](exception-aggregation.md): masking wants a low-level,
widely-shared piece of code that swallows the exception on the spot, while
aggregation wants the exception to propagate as far as possible before being
caught. Both share the same underlying strategy — position the handling code
wherever it captures the largest possible number of would-be exceptions with
a single piece of code.
