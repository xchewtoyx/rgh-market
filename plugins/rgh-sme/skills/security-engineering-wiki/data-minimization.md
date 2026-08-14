---
type: concept
title: Data Minimization
description: >
  The strongest protection for sensitive data is never collecting it in the
  first place — decide by concrete downstream need, not by convenience.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), chs. 7, 10"
---

# Data Minimization

The single best protection for sensitive or private data is to never ingest
it in the first place. Every dataset a system holds is a dataset it must
defend, [audit](audit-log-design.md), back up securely, and eventually
delete correctly — collecting data "just in case" imports all of that cost
for no offsetting benefit until an actual downstream need materializes.

This follows from thinking through realistic misuse and breach scenarios
*before* a pipeline is built, rather than assuming best-case handling:
for each field a system proposes to collect, ask concretely how it could
leak, be misused internally, or be compelled out by legal process, and
require a genuine downstream consumer to justify collecting it at all. A
security posture that only produces "the illusion of safety" — a compliance
checkbox rather than real reduction in what could go wrong — is the failure
mode this guards against (see
[security theater vs. genuine security practice](security-theater-vs-genuine-practice.md)).

Data minimization is the point-of-ingestion complement to
[offloading sensitive data](offloading-sensitive-data.md): offloading
removes data you already must handle by routing it through a third party;
minimization prevents the data from entering your systems' scope at all.
Where minimization isn't possible because the data is genuinely needed,
[access classification by risk](access-classification-by-risk.md) and
[least privilege](least-privilege.md) take over as the next line of
defense.

**Where identity still needs to be tracked without retaining the
identifying value itself, tokenize at ingestion rather than deferring
it** — hash the identifier before it ever lands in storage. But a naive,
unsalted hash of a low-entropy input (an email address, a phone number,
a name) is not the protection it looks like: the input space small
enough that an attacker with a plausible guess (a known customer's
email) can simply hash that guess and compare, recovering the identity
without ever "breaking" the hash function itself — the weakness is in
the input's guessability, not the algorithm. This is the same "know what
the tool actually guarantees" caution as
[secure cryptographic APIs](secure-cryptographic-apis.md): a hash applied
to the wrong kind of input, or without salting, produces the *appearance*
of protection while leaving the identity trivially recoverable to anyone
who can enumerate plausible inputs.
