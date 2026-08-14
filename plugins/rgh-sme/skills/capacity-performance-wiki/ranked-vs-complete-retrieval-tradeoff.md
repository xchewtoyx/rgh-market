---
type: concept
title: Ranked vs. Complete Retrieval Trade-Off
description: Returning only the top-N ranked matches keeps interactive query latency bounded, but tooling tasks that need every match require a separate complete-scan mode — often implemented via priority sharding so the common case stays fast.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Titus Winters, Tom Manshreck, Hyrum Wright, eds.), ch. 19"
---

Search and lookup systems face a fork between two query modes with incompatible capacity profiles:

*   **Ranked retrieval (top-N):** return the best matches by a scoring function, stop after N candidates. Fast — bets that ranking surfaces the desired result in the first page. Matches web-search and interactive-navigation patterns where users rarely scroll past early results.
*   **Complete retrieval (all matches):** return every document that satisfies the query, often in deterministic (e.g., alphabetical) order. Slow — must scan and evaluate the full candidate set. Required for refactoring, global search-and-replace, static analysis, and other tooling that cannot silently drop matches.

Web search can always take ranking shortcuts; developer tooling on a large corpus cannot — a single missed match in a rename operation is a correctness bug, not a UX inconvenience.

## Priority Sharding as a Hybrid

One implementation pattern keeps both modes without slowing the common case:

1. **Shard the corpus by file priority** (importance, recency, reference count, or similar).
2. **Default mode** considers only high-priority shards — analogous to ranked web search returning quickly from the most likely subset.
3. **All-results mode**, explicitly requested, scans every shard and every chunk — paying the full cost only when the caller opts in.

The trade-off is **implementation and API complexity** in exchange for not forcing tooling workloads through a latency budget designed for interactive navigation, and not forcing interactive users to wait for a full-corpus scan.

## Relationship to Other Capacity Patterns

*   Ranked top-N is the retrieval-layer counterpart of capping an [unbounded result set](unbounded-result-set-antipattern.md) — both bound resource use per query by limiting how much of the match set is materialized.
*   **Supplemental retrieval** (rewriting a query into specialized sub-queries — e.g., definitions-only, filename-only — and merging results) is a middle path: it improves ranked-mode completeness for high-intent query shapes without scanning the entire corpus on every request.
*   When complete mode is needed, treat its latency and resource cost as a separate [load parameter](load-parameters.md) in capacity models — "queries per second" alone is misleading if a small fraction of requests trigger full-corpus scans.
