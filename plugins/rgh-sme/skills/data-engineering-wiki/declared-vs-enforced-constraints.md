---
type: concept
title: Declared vs. Enforced Constraints
description: >
  Why a primary key or foreign key in a cloud warehouse is often only
  documentation, not a guarantee — and why that pushes uniqueness and
  referential-integrity validation into the pipeline itself.
sources:
  - title: Data Modeling with Snowflake
    resource: "Data Modeling with Snowflake (Gershkovich), ch. 5"
---

Most cloud data warehouses support declaring the standard relational
constraint types — `PRIMARY KEY`, `UNIQUE`, `FOREIGN KEY`, `NOT NULL` — but
that doesn't mean all four are actually *enforced*, in the sense of the
database blocking a write that would violate them. On Snowflake's standard
table type, for instance, only `NOT NULL` is enforced; `PRIMARY KEY`,
`UNIQUE`, and `FOREIGN KEY` are purely **orientative** — a load can insert a
duplicate "primary key" value or a foreign key with no matching parent row,
and the database will not stop it. This isn't a Snowflake quirk specifically;
it reflects a broader pattern in MPP and columnar cloud warehouses, where
enforcing uniqueness or referential integrity would require an index the
storage engine isn't built to maintain cheaply at scale (see
[copy-on-write load cost](copy-on-write-load-cost.md) for why).

This trade-off predates cloud MPP warehouses: even traditional on-prem RDBMS
platforms disable DBMS-enforced referential integrity for warehouse loads,
for the same underlying reason — a well-built [surrogate key
pipeline](surrogate-key-pipeline.md) already performs the equivalent
in-memory lookups to translate business keys into surrogate keys, so a
DBMS-level FK check is redundant work paid twice at load volumes the check
wasn't designed for. A useful staged-trust practice: enable DBMS-enforced RI
during ETL development and initial historical load, as a belt-and-braces
check on the pipeline's own key-resolution logic; once a run completes with
no RI violations, drop or unenforce the constraint so it stops costing
insert/update overhead on every subsequent load, while keeping the declared
(but now unenforced) constraint for the optimizer-hint value described below.

The declared constraints are still valuable even unenforced — they document
the intended grain and relationships for humans and for BI tools that
auto-generate joins from foreign-key metadata, and query optimizers can use
a declared-but-trusted constraint as a hint to skip unnecessary joins (a
trust flag, commonly called something like `RELY`, tells the optimizer the
constraint genuinely holds even though the platform never checked it — worth
setting on any constraint a pipeline's own validation has actually verified,
since it carries no cost and can let the optimizer eliminate joins it would
otherwise have to run). But
"documented" is not "guaranteed": a pipeline cannot rely on the warehouse to
catch a duplicate key or an orphaned foreign key the way an OLTP application
database would. That responsibility shifts onto the pipeline's own
[data quality validation gates](data-quality-validation-tests.md) — an
explicit duplicate-key check after a load, or a referential check against
the parent dimension before or after a fact load — rather than the schema
declaration doing that work automatically.
