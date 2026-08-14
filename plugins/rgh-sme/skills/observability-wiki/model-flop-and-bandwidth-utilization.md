---
type: concept
title: Model FLOP/s and Bandwidth Utilization (MFU, MBU)
description: >
  For LLM inference, nvidia-smi "GPU utilization" only reports time the
  GPU was busy, not how efficiently — MFU and MBU measure achieved
  FLOP/s and memory-bandwidth fractions of peak, and are the useful
  efficiency signals for cost and bottleneck diagnosis.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering: Building Applications With Foundation Models (Chip Huyen), ch. 9"
---

Vendor GPU dashboards commonly surface **nvidia-smi "GPU utilization"**:
the percentage of time the GPU was actively processing *something*. That
is not efficiency. A GPU rated for 100 ops/s that is doing 1 op/s can
still report 100% under this definition, so the number is a weak signal
for whether you are getting your money's worth — a concrete case of a
[known instrument lie](calibrated-trust-in-known-instrument-lies.md) to
calibrate against rather than abandon wholesale.

Two utilization ratios from the ML systems literature are more useful for
inference (and training) efficiency tracking:

- **MFU (Model FLOP/s Utilization)** — observed throughput (tokens/s)
  divided by the theoretical maximum throughput at the chip's peak
  advertised FLOP/s (term from the PaLM paper, Chowdhery et al., 2022).
  Example: 20 tokens/s achieved against a 100 tokens/s theoretical peak
  → MFU 20%.
- **MBU (Model Bandwidth Utilization)** — memory bandwidth consumed
  (parameter count × bytes/param × tokens/s) divided by the chip's
  theoretical memory bandwidth. Example: a 7B model in FP16
  (2 bytes/param) at 100 tokens/s uses 700 GB/s; on an A100-80GB
  (≈2 TB/s peak) that is MBU 70%. This is why quantization matters for
  bandwidth-constrained decode — fewer bytes per parameter, less
  bandwidth per token.

Throughput relates linearly to both ratios, so some teams conflate them
with tokens-per-second; keep the distinction: TPS is the raw rate,
MFU/MBU say how close that rate is to what the hardware could do.
Expected shape depends on the bottleneck:

- Compute-bound phases (prefill, many image-generation workloads) tend
  toward higher MFU / lower MBU.
- Memory-bandwidth-bound phases (autoregressive decode, long-context
  loads) tend toward lower MFU / higher MBU.

Training MFU is typically higher than inference MFU because workloads
are more predictable and batch better; within inference, prefill usually
shows higher MFU than decode. Treat "good" thresholds as
workload-and-hardware-specific (PaLM-era training examples spanned
roughly 20–46% MFU across large models) — useful for
[trend comparison on the same stack](bare-metrics-need-comparison-context.md),
not as universal targets. Chip makers sometimes quote peak FLOP/s under
favorable sparse-matrix conditions that real dense inference cannot hit,
so absolute MFU against vendor peak is a softer number than MFU trend
over time on fixed hardware and workload.

Do not maximize utilization for its own sake: higher MFU/MBU with rising
cost *and* latency is not a win. Pair these gauges with
[TTFT/TPOT histograms](llm-inference-latency-metrics.md),
[token/cost rates](llm-token-and-cost-metrics.md), and
[goodput](llm-inference-goodput.md) so efficiency gains are judged
against user-visible latency and dollars per completed request.
