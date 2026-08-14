---
type: concept
title: Hash-Based Change Detection
description: >
  Concatenating and hashing a row's tracked columns into one value so a load
  can detect whether anything changed with a single equality check instead
  of comparing every column individually.
sources:
  - title: Data Modeling with Snowflake
    resource: "Data Modeling with Snowflake (Gershkovich), ch. 13"
---

When an [upsert or merge](table-load-patterns.md) needs to decide whether an
incoming record actually differs from what's already loaded, comparing every
tracked column individually against its target value gets unwieldy as the
column count grows, and easy to get subtly wrong (a forgotten column silently
never triggers an update). The alternative: concatenate all the tracked
columns into one string and hash it (MD5 is the common choice) on both the
incoming and existing row, then compare the two hashes with a single
equality check:

```sql
SELECT MD5(col1 || col2 || ... || colN) AS diff_hash
-- then:
IFF(hash_new = hash_old, 'same', 'changed')
```

This collapses an N-column comparison into one, which matters both for
readability (the merge's change-detection logic doesn't need updating every
time a new tracked column is added — it just needs the column added to the
hash expression) and for load performance, since a single-column hash
comparison is cheaper for the query engine to evaluate at scale than a
multi-column boolean expression. It's the same technique used across load
patterns that need "did anything change?" as a fast yes/no: driving
[table load pattern](table-load-patterns.md) merges, and specifically
[SCD Type 2 loads](scd-type2-load-via-change-stream.md), where the hash
comparison is what decides whether a new history row needs to be written at
all.

**When a dimension has both Type 1 and Type 2 attributes, keep separate
hash columns per SCD-type group** rather than one hash over every tracked
column — a `hash_type1` over the overwrite-in-place attributes and a
`hash_type2` over the versioned ones. The two groups trigger different load
actions (an in-place update versus a new history row), so collapsing them
into a single hash would force checking which specific columns changed
anyway to decide which action to take, defeating the point of a single
cheap equality check.

Hashing has one real cost beyond computing the hash itself: a **collision**
— two genuinely different attribute combinations producing the same hash —
would cause the merge to treat a real change as "no change" and silently
skip writing it. This risk is small and algorithm-dependent, not zero;
choose a hash function with a low enough collision probability at the
dimension's actual cardinality rather than assuming any hash is
interchangeable with any other.

**Caching only the hash, natural key, and surrogate key columns** — rather
than the dimension's full attribute set — is what makes
[pinning a wide dimension in memory](surrogate-key-pipeline.md) for the
change-detection lookup practical even when the dimension has dozens of
tracked attributes: the comparison only ever needs those three narrow
columns, never the attributes themselves.

**Skipping a lookup entirely can be a valid optimization** when its result
is predictable often enough to not be worth checking: a new-record lookup
can be skipped by routing every incoming record through Type 2 processing
uniformly (new and Type 2-changed records are inserted the same way
regardless), and a Type 1 comparison can be skipped by issuing an
unconditional update for every record — worthwhile specifically when most
records are expected to carry a Type 1 change anyway, or when the target
database supports a native upsert that folds the comparison into the write
itself.
