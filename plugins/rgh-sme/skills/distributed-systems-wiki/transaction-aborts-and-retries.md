---
type: concept
title: Transaction Aborts and Retries
description: >
  Aborts exist so transactions can be safely retried — but retrying correctly
  must handle duplicate effects, overload, and permanent errors.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 7"
---

# Transaction Aborts and Retries

The whole point of an [abort](acid-transactions.md) is that the application
can safely retry: nothing from the failed attempt persists. Yet retry logic
is commonly missing (many ORMs surface an abort as an exception and give up)
or wrong. A correct retry policy handles:

- **Ambiguous success.** If the transaction committed but the *acknowledgment*
  was lost on the [network](unreliable-networks.md), a retry executes it
  twice. Deduplication needs an application-level
  [idempotency](idempotency.md) mechanism — the database can't distinguish a
  retry from a new request.
- **Overload.** If aborts are due to the database being overloaded, blind
  retries amplify the problem. Retry a bounded number of times with
  exponential backoff, and treat overload errors differently from conflicts.
- **Permanent errors.** Retrying a constraint violation is pointless; only
  transient errors (deadlock, serialization conflict, temporary network
  issue) warrant retry. Optimistic schemes like
  [SSI](serializability.md) make conflict-abort-retry the *normal* path, so
  the retry loop is mandatory there.
- **External side effects.** Emails, payments, and messages sent during the
  transaction happen again on retry — side effects must move outside the
  transaction or be deduplicated themselves.
