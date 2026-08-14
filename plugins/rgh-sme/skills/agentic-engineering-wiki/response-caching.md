---
type: concept
title: Response Caching
description: >
  Exact or semantic reuse of prior model or retrieval results to cut latency and
  cost — with eviction, cacheability rules, and cross-user leak vigilance.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 10"
---

System-level caches (distinct from provider KV/prompt caches) reuse work across
requests. Beyond the latency and cost savings, a cached response is also a
free fix for [output consistency](output-consistency-and-robustness.md): a
served-from-cache answer is trivially identical to the one served last time,
regardless of how much sampling variance the underlying model has.

**Exact caching** returns a prior result only for identical requests — product
summaries, prior vector-search hits, expensive multi-step or tool-heavy queries.
Use in-memory or Redis/Postgres with LRU/LFU/FIFO eviction. Do not cache
user-specific or time-sensitive queries; some teams train a cacheability
classifier. **Leak risk**: a query that looks generic but embeds user-specific
facts can poison the cache for the next identical string from another user.

**Semantic caching** matches by embedding similarity above a threshold. Higher
hit rate, higher wrong-answer risk, and nontrivial vector-search cost. Adopt
only when measured hit rate offsets correctness risk.

Place caches after the [model gateway](model-gateway.md) or inside it in a
[progressive agent architecture](progressive-agent-architecture.md).
