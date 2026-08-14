---
type: concept
title: Champion-Dependent Projects
description: A system or initiative that survives only because one enthusiastic individual personally defends it decays once that person leaves, even if nothing about the system itself changed.
sources:
  - title: "Designing Connected Content"
    resource: "Designing Connected Content (Atherton, Hane), ch. 10"
---

Some systems and initiatives are technically sound — well-structured, well-documented, working exactly as designed — and still stall or decay after the person who championed them moves on. The failure mode isn't in the artifact; it's that ongoing investment, defense against "let's redesign this from scratch" pressure, and day-to-day advocacy depended entirely on one individual's personal enthusiasm rather than being written into anyone's job description or the organization's budgeting process. When that person leaves, "the project [is] undefended" — no successor inherits the responsibility to keep arguing for it, so it quietly loses funding, attention, and eventually correctness, without any single decision to abandon it.

## Why This Differs From Ordinary Handover Failure

This is not the same failure as missing documentation or an undocumented system (see [Snowflake Servers](snowflake-servers.md)) — the champion-dependent system can be perfectly documented and still fail, because what's missing isn't technical knowledge but institutional *ownership*: nobody with organizational standing has an assigned responsibility to keep sponsoring it. It is also distinct from a planned [operational responsibility transition](operational-responsibility-transition.md) between teams, which addresses the deliberate handoff of a live system; a champion-dependent project often has no transition at all — the champion simply leaves, and no one was ever designated to take their place.

## Recognizing the Pattern

- The project's survival is discussed in terms of one person's advocacy ("as long as X is here, it's safe") rather than a budget line, a team charter, or an assigned owner role.
- Visible, flashy work (a redesign, a new feature) attracts stakeholder attention and resourcing more easily than invisible structural investment, so the champion is perpetually re-litigating the project's value against louder, more visible priorities — a fight that stops happening the moment they're not there to have it.
- Success is measured by outsiders on visible surface quality, not on the underlying investment, so a technically excellent but visually dated system reads as neglected and an easy target for replacement once its defender is gone.

## Mitigations

- **Institutionalize ownership before the champion leaves**: assign a role or team, not a person, as the accountable owner, so the responsibility survives personnel changes by construction.
- **Make the win visible beyond the core team**: if only the project committee understands what was built and why, outsiders will see "a construction site" rather than progress — communicate value broadly enough that more than one person would notice and object if the project were abandoned.
- **Budget for ongoing governance, not just initial build**: a one-time investment with no ongoing maintenance/advocacy line item reverts to being nobody's job as soon as the initial excitement fades.
