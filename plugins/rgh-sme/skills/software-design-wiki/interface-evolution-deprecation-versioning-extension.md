---
type: concept
title: "Interface Evolution: Deprecation, Versioning, and Extension"
description: >
  Three ways to change a published interface without breaking every actor
  that already depends on it — remove it with warning, keep both old and
  new side by side, or add new resources while leaving the original alone.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th ed. (Bass, Clements, Kazman, with Cesare Pautasso), ch. 15"
---

A published interface is a contract, and unlike free-floating internal
implementation it can't be casually rewritten — every resource an
[interface](interface-formal-and-informal-elements.md) exposes is
effectively a maintenance commitment for the element's lifetime, since
actors will come to depend on it. Three techniques cover how to change an
interface anyway, each with a different cost profile:

- **Deprecation** — remove a resource, ideally with extensive advance
  notice. In practice, many actors only discover a deprecation when it
  actually breaks them; a deprecation-warning error code returned for a
  transitional period is one mitigation, giving actors a signal before the
  removal actually lands.
- **Versioning** — keep the old interface alongside the new one, and let
  each actor specify which version it uses. The old version is deprecated
  (and eventually removed) only once nothing still depends on it. This
  costs ongoing maintenance of multiple live versions in exchange for never
  forcing an actor to move on someone else's schedule.
- **Extension** — leave the original interface completely untouched and
  add new resources alongside it for the desired change. If the new
  resources introduce no incompatibility with the old ones, the element can
  simply implement the extended interface directly, and this is the
  cheapest of the three techniques. If the extension *does* introduce an
  incompatibility — the original interface embeds an apartment number
  inside a single address string; the extended interface breaks it out into
  a separate parameter — the element needs an internal interface plus a
  **mediator** that translates between the external forms: the mediator
  parses the address string for the apartment number when invoked through
  the old external interface, but passes the already-separate parameter
  straight through when invoked through the new one. The mediator absorbs
  the translation cost so neither the old nor the new caller has to know
  the other form exists.

Each of the three techniques implies a different mix of [backward and
forward compatibility](backward-and-forward-compatibility.md): versioning
sidesteps the question by never asking one version to read the other's
data; extension leans on old consumers being forward-compatible with
whatever new producers add, following [schema evolution
rules](schema-evolution-rules.md) if the changed resource is structured
data rather than a plain method call; deprecation is only safe once
nothing still needs backward compatibility with what's being removed.

Choosing among the three is a cost trade-off, not a search for a uniformly
"correct" one: deprecation is cheapest to build but riskiest for actors
who miss the warning; versioning is safest for actors but means carrying
multiple live implementations; extension-with-mediator is a middle ground
that keeps both old and new actors served through one implementation, at
the cost of writing and maintaining the translation layer itself.

This applies beyond a single module's method signatures — a database
schema is itself an interface, and the same three techniques (deprecate a
column, version the schema, or add new columns alongside old ones) apply to
schema evolution for exactly the same reason.
