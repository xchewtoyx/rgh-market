---
type: concept
title: Localizing Rather Than Eliminating Global Dependencies
description: >
  A variable that feels globally needed is usually only genuinely used in a
  handful of places; separating code that fetches or stores data from code
  that merely computes on data already supplied naturally shrinks or
  eliminates the felt need for a true global.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 9"
---

For the worst-case feeling of "everything needs the database" (or some other
pervasive global resource), search for where the supposedly global-scope
variable is *actually* used. Despite being globally *accessible*, most
globals turn out to be genuinely used in only a small number of places. A
design that cleanly separates "objects that fetch or store data" from
"objects that just compute on data already supplied to them" naturally
localizes — and often eliminates outright — the felt need for a true global,
because the computing code never needed direct access to the resource in the
first place; it only needed the data.

If a variable really is used absolutely everywhere, that's not evidence the
global is unavoidable — it's diagnostic of missing layering altogether in
the application's overall structure. This is the constructive fix underlying
[breaking singleton dependencies](breaking-singleton-dependencies.md): rather
than only making the global fake-able for tests, restructure so fewer things
need direct access to it at all.
