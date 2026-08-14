---
type: concept
title: Interface Evolution
description: >
  An interface is a contract that cannot be casually broken; changing one
  means choosing among deprecation, versioning, and extension, each with a
  different cost to the actors already depending on it.
sources:
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 15"
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann, Stocker, Lübke, Zdun, Pautasso), ch. 1"
---

Publishing an [interface's documentation](interface-documentation.md) is a
promise to whoever depends on it, and unlike a piece of internal
implementation, it cannot be casually changed once other elements rely on
it. There are three ways to change one:

- **Deprecation** — remove the interface, ideally with substantial advance
  notice. In practice, many actors only discover a deprecation when it
  actually breaks them, so a deprecation-warning error code returned for a
  transitional period is a common mitigation.
- **Versioning** — keep the old interface alongside the new one, and let
  each actor declare which version it uses; the old version is only
  deprecated once nothing still depends on it.
- **Extension** — leave the original interface untouched and add new
  resources for the desired capability. If the extension introduces no
  incompatibility, the element can implement the extended interface
  directly. If it does — for example, an address originally embedded as
  one string being split into a separate apartment-number field — the
  element needs an internal interface plus a **mediator** that translates
  between the external forms: parsing the string when invoked through the
  old interface, passing the field straight through when invoked through
  the new one.

Which of the three is appropriate depends on how much disruption the
existing actors can tolerate versus how much translation machinery the
element's owner is willing to maintain — versioning and mediated extension
both let old and new actors coexist, at the cost of carrying that
translation logic indefinitely, while deprecation eventually removes the
cost but forces every actor to move.

This is also why every resource exposed on an interface is a maintenance
commitment for the element's whole lifetime: actors will come to depend on
it, and **Hyrum's Law** observes that this isn't limited to what was
formally promised — "with a sufficient number of users of an interface, it
does not matter what you promise in the contract: all observable behaviors
of your system will be depended on by somebody." That doesn't mean the
documented contract boundary is meaningless — it's still what tells you
which behaviors you owe support for and which are used at the caller's own
risk — but it does mean an interface's owner should expect even
undocumented, incidental behavior to have consequences when it changes.

For public or widely consumed APIs specifically, there is effectively
**one real chance** to get the initial contract right: once clients depend
on a successful API, corrections grow expensive, feature removal becomes
effectively impossible without breaking clients, and [data
parsimony](api-architecturally-significant-requirements.md) pressure makes
contracts grow monotonically. That asymmetry is itself an architecturally
significant requirement — it argues for investing in [API design from
requirements artifacts](api-design-from-requirements-artifacts.md) and
[documenting trade-offs](documenting-trade-offs.md) before the first
external client integrates, not after.
