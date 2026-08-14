---
type: concept
title: SQL Injection
description: >
  Untrusted input that gets interpreted as part of a query's structure
  instead of as data — the general injection pattern, defended primarily
  by never building query structure from input at all.
sources:
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 9"
  - title: "Release It!, 2nd Edition"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Nygard), ch. 11"
---

# SQL Injection

SQL injection is the concrete, well-studied instance of the general
injection pattern: an application concatenates untrusted input into a
query string, and an attacker supplies input that is interpreted as query
*structure* — additional clauses, a `UNION` pulling in another table, a
statement terminator followed by a second statement — rather than as the
inert data value the application intended. The consequences reach beyond
reading unauthorized rows: injected SQL can invoke stored procedures at
whatever privilege the application's database connection holds, so the
blast radius of one injection point is bounded by how much that
connection can do, not by what the vulnerable query was supposed to do.

**Defense layers, in order of how much each one buys:**

- **Prepared/parameterized statements are the primary defense.** The query
  structure is fixed before any input is bound to it, so injected input is
  always treated as a literal value, never as executable structure — the
  vulnerability class is structurally prevented rather than filtered.
- **Allow-list input validation covers what prepared statements can't.**
  Some inputs control structure legitimately — a dynamic table name, a
  sort direction, a column to filter on — and parameterization has no
  answer for them, since the placeholder mechanism only binds values, not
  identifiers or clauses. Validate these against a fixed allow-list of
  acceptable values rather than trying to blocklist dangerous ones.
- **Harm reduction bounds what a successful injection can still do.** This
  is [least privilege](least-privilege.md) and
  [compartmentalization](compartmentalization.md) applied to the database
  connection itself: give each application its own database user scoped
  to only what it needs, remove stored code and privileges the
  application doesn't use, and keep the database engine patched — so an
  injection that does land is contained rather than becoming
  full-database compromise.
- **Monitoring is the backstop, not the defense.** Log every failed and
  successful SQL statement; a spike in syntax errors is a leading
  indicator of injection attempts (an attacker probing query structure
  produces malformed SQL before they produce working SQL), and query
  patterns containing `UNION`s or stray statement terminators are worth
  flagging. This is [defense in depth](defense-in-depth.md): monitoring
  catches what got past the first two layers, it doesn't substitute for
  them.

The same shape recurs outside SQL wherever an interpreter parses a
combined structure-plus-data string built from untrusted input — command
injection into a shell, expression injection into a template engine,
cross-site scripting (untrusted input interpreted as HTML/JavaScript
structure instead of display text, defended by context-aware output
encoding rather than a filter), or prompt injection into an LLM's
[instruction and data separation](defensive-prompt-engineering.md) all
share the identical root cause and the identical primary fix: keep
untrusted input out of the positions a parser treats as structure, and
never rely on a filter for input where a structural separation is
available instead.
