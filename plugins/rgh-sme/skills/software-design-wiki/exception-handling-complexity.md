---
type: concept
title: Exception Handling Is a Major Source of Complexity
description: >
  Exception handling — any code path for an uncommon condition, formal or
  informal — is inherently harder to write than the normal case, can spawn
  further exceptions of its own, and is hard to test, making it one of the
  worst sources of software complexity.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 10"
---

"Exception" here means any uncommon condition that alters normal control
flow, whether through a formal language exception mechanism or an informal
one like a sentinel return value. Exceptions arise from four broad sources:
bad caller arguments or configuration; an invoked operation that can't
complete (I/O failure, unavailable resource); distributed-system faults (lost
or delayed packets, unresponsive servers, unexpected peer behavior); and
internally-detected bugs or inconsistencies.

Handling an exception is nontrivial in either of its two forms: pushing
forward to complete the work despite it (resend a lost packet, recover from a
redundant copy), or aborting and propagating upward, which requires restoring
consistent state — unwinding partial changes — before reporting anything.
Worse, handling can itself spawn further exceptions: resending an allegedly
lost packet can create a duplicate if it wasn't actually lost, which the peer
must now also handle; recovering from a "lost" redundant copy fails if that
copy is also gone. These secondary exceptions are often subtler than the
original, and developers must eventually terminate the cascade by handling
some exception without generating a new one.

Language-level exception syntax compounds this: `try`/`catch` blocks are
verbose and disconnect handler code from the normal-case code they wrap — a
two-line deserialization loop can need five separate `catch` blocks, with the
boilerplate outweighing the actual logic and no clear map from which line
throws which exception.

Exception-handling code is also unusually hard to *test*: some conditions
(I/O errors) are difficult to trigger in test environments, so rarely-hit
paths accumulate latent bugs — "code that hasn't been executed doesn't work."
A study of production failures in distributed data-intensive systems found
that more than 90% of catastrophic failures were caused by incorrect error
handling, not the normal-case logic. The chapter's throughline is a direct
response to this: reduce the number of *places* exceptions must be handled at
all. See [too many exceptions](too-many-exceptions.md) for the diagnosis and
the four elimination techniques it motivates.
