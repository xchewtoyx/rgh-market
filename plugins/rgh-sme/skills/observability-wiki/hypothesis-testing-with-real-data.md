---
type: concept
title: Test Hypotheses Against Real Data, Not Speculation
description: It's tempting to speculate about a root cause before actually looking at telemetry, but this introduces blind spots — the real cause is often in code or a signal the debugger hasn't looked at recently, and it only surfaces once assumptions are set aside and the data is actually examined.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 15"
---

When debugging a performance problem, it's tempting to jump straight to a plausible-sounding theory and start acting on it, rather than first gathering evidence. This tendency is strongest exactly when it's most dangerous: performance bugs often live in code the debugger hasn't touched in a long time, which is precisely the code an untested assumption is least likely to implicate. A concrete example: a slow web server was assumed to have a backend bottleneck, but a profiler instead showed that logging every input to disk and calling `sync` on it was the actual cause — invisible to intuition, obvious once measured.

*Observability* is the property of being able to determine what a system is doing by examining its outputs; tracing solutions (e.g. Dapper, Zipkin) are a concrete, commonly reached-for tool for this kind of investigation — a debugging session might open with as basic a question as "can you find a slow trace?" This principle — always ground a hypothesis in what the telemetry actually shows before acting on it — is a core input to the [core analysis loop](core-analysis-loop.md) and the corrective for [confirmation bias in debugging](confirmation-bias-in-debugging.md).

Before the data comes back, it's also worth [stating the hypothesis with a calibrated confidence level](calibrated-confidence-in-hypothesis-statements.md) rather than as a flat claim — it keeps the eventual test result a genuine update rather than a binary right/wrong verdict.
