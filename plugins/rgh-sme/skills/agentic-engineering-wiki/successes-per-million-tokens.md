---
type: concept
title: Successes Per Million Tokens
description: >
  A cost-normalized accuracy metric — expected task successes per million
  tokens spent — for comparing harness configurations that trade accuracy
  against token cost.
sources:
  - title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
    resource: "Agentic Harness Engineering (Lin, Liu, Pan, et al.), App. A"
---

[pass@1](pass-at-k-and-pass-hat-k.md) alone can't rank two harness
configurations when one is more accurate and the other cheaper — reporting
pass@1 and token cost as two separate columns leaves the trade-off implicit,
forcing a reader to eyeball which gain is "worth" which cost. Succ/Mtok folds
both into a single number:

Succ/Mtok = (pass@1 × 10^6) / (mean tokens per trial)

— read as "the expected number of successes per million tokens spent." A
configuration that raises pass@1 by spending proportionally more tokens can
score *worse* on Succ/Mtok than a cheaper, slightly-less-accurate one; a
configuration that holds accuracy roughly flat while cutting token spend
scores strictly better.

Report pass@1 and token cost separately when the two vary independently and a
reader needs to see which one moved — combining them into a ratio too early
hides that. Fold them into Succ/Mtok specifically when comparing
configurations that are explicitly trading one for the other (e.g. a
[component-level harness ablation](component-level-harness-ablation.md) where
one variant is both more accurate and more expensive than another), so the
comparison has a single number to rank by instead of two that can point in
opposite directions.
