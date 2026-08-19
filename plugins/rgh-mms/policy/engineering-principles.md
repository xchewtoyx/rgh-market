# Engineering Principles

Governance policy for agentic development across all registered product
repositories. Product repos pin a harness version; this document is canonical
at that pinned version.

## Core principles

1. **Smallest useful change.** Prefer the minimum diff that solves the problem.
2. **Library-first, thin adapters.** Business logic in libraries; CLI and portal
   files are presentation layers.
3. **Batteries over bespoke machinery.** Use proven tools before inventing
   frameworks.
4. **Evidence over vibes.** Falsifiable predictions (contracts), tests, and
   settled outcomes beat narrative confidence.
5. **Progressive disclosure.** Bootstrap docs stay lean; deep reference loads
   on demand.
6. **Leave it cleaner.** Remove dead code and stale docs touched by your change.

## Testing

- One behavior per test; parametrize input families.
- Mandatory negative-path coverage for new branches and validation.
- Assert documented guarantees, not just line coverage.
- Run the product repo's `ci.local_command` before returning from implementor.

## Complexity

- Respect the profile/repo complexity ceiling; decompose rather than suppress.
- A comment introducing a block is a function name in disguise — extract it.

## Documentation

- User-facing or behavior changes update docs and changelog in the same
  commit — a `changelog.d/` fragment, per
  [`workflows/documentation.md`](../workflows/documentation.md#changelog-fragments).
- Prose describes current behavior, not aspirations.

## Provenance

- Quantitative claims and patterns ported from another repo cite their source
  inline: `**Source:** <repo>/<path>`, next to the claim they support.

## Delivery

- One issue, one fresh branch, one PR.
- Agents never self-merge and never force-push unless explicitly allowed in
  `.agentic/harness.yaml` local exceptions.
- Human merge is a hard gate for load-bearing delivery.
