---
type: concept
title: Phoenix Server Pattern
description: Making a server disposable and automatically rebuildable from scratch so a new operator never needs to know its manual configuration history.
sources:
  - title: "Continuous Delivery"
    resource: "Continuous Delivery (Humble, Farley), ch. 2"
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 10"
---

A "phoenix server" is a machine that can be destroyed and rebuilt automatically from an automated configuration script at any moment, ending up in the same known-good state every time. It is the direct antidote to a [snowflake server](snowflake-servers.md): where a snowflake's true configuration exists only as an unrecoverable history of manual changes, a phoenix's configuration exists entirely as a script someone can read, version, and re-run.

## Why This Matters for Handover

The pattern converts a question a new operator cannot safely answer — "what state is this box actually in, and why?" — into one they don't need to ask at all: the running system and its definition are guaranteed identical, because the running system was produced by re-executing the definition. Recovery, disaster response, and environment duplication all stop depending on someone's memory of the machine's history.

This is the same move as [self-documenting declarative systems](self-documenting-declarative-systems.md): make the automated definition the sole source of truth rather than treating documentation as a separate artifact that has to be kept in sync with a hand-maintained machine.

## Precondition

The pattern only works if provisioning is genuinely automated end-to-end — OS install, middleware, and application configuration all driven by version-controlled scripts, with no manual step assumed as a prerequisite. A server that is "mostly" rebuilt by script but still needs one undocumented manual tweak after provisioning has quietly reverted to being a snowflake.

## Full Rebuild vs. Incremental Convergence

Two ways to keep a fleet of servers in a known state, with different implications for a future operator's confidence in that state:

- **Baking**: build a complete image (OS + packages + configuration) and replace a server outright by deleting it and recreating it fresh from the current image. Every rebuilt server ends up in an identical, fully-understood state — this is the phoenix pattern at its strongest.
- **Frying**: leave the running server in place and apply only the incremental changes configuration management determines are needed. Faster and less disruptive per change, but a server that has only ever been fried has reached its current state through some particular sequence of past incremental updates, not a single, replayable definition — a new server built fresh from today's image is only guaranteed *identical* to it in theory, since small drift can silently accumulate along the fried lineage. A fleet with both freshly-baked and long-fried members has effectively split into two lineages that must both be accounted for when testing the next change.

Treat "fried" servers as running on borrowed disposability: they still avoid the worst snowflake failure mode (an unrecoverable configuration), but they don't get the full phoenix guarantee that a rebuild produces exactly what the definition says, until they are periodically refreshed from a full bake.
