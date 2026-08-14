---
type: concept
title: Software, System, and Enterprise Architecture Scope
description: >
  Software architecture, system architecture, and enterprise architecture
  are three different scopes of structure that constrain each other, and
  a design document should state explicitly which one it is describing.
sources:
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 1"
---

**Software architecture** is the set of structures needed to reason about
a software system. **System architecture** is a broader scope: it maps
functionality onto hardware, software, *and* people, and is concerned with
things software architecture is not — power, weight, physical dimensions,
and other non-software constraints. **Enterprise architecture** is broader
still: the structure and behavior of an organization's business processes,
information flow, personnel, and organizational subunits, of which
software is only one concern among several.

Each broader scope supplies constraints the narrower one must live inside,
and the boundary between adjacent scopes is not fixed in advance — there
is typically real negotiation between a system architect and a software
architect over which functionality is allocated to hardware versus
software, for instance. A design document that doesn't state which of
these three scopes it's describing invites readers to hold it accountable
for concerns (organizational process, physical hardware constraints) that
were never in scope for the document, or conversely to assume constraints
from a broader scope were already accounted for when they weren't. Stating
the scope explicitly is a specific case of the discipline captured in
[scope of work vs scope of product](scope-of-work-vs-scope-of-product.md),
applied to architecture description rather than requirements.
