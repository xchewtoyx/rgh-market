---
type: concept
title: Significant Digits in Capacity Calculations
description: Rules for carrying measurement precision correctly through capacity arithmetic, so a calculation never reports more precision than its least-precise input actually supports.
sources:
  - title: "Guerrilla Capacity Planning"
    resource: "Guerrilla Capacity Planning (Neil J. Gunther), ch. 3"
---

Every capacity measurement carries uncertainty — no instrument, including OS-level kernel counters, is exact. Reporting a derived calculation with more digits than its inputs justify (the "sin of precision") creates a false impression of accuracy that can mislead a downstream decision. **Significant digits (sigdigs)** rules keep a calculation's stated precision honest.

## Counting Significant Digits

Scan the number left to right: if it has an explicit decimal point, count the first nonzero digit and everything to its right (including trailing zeros) — e.g. `0.000050` has 2 sigdigs. If it has no decimal point, append one, then count up to (and including) the last nonzero digit, ignoring trailing zeros before that implicit point — e.g. `200300` has 4 sigdigs (`2003`), and critically, `50` has only **1** sigdig while `50.0` has **3** — the same-looking number can carry very different implied precision depending on how it's written.

## The Golden Rule and Its Two Cases

A calculated result should never carry more sigdigs than its least-precise input.

*   **Sum rule:** a sum or difference is never more precise than the least precise addend. Round every addend to the same *decimal place* as the least precise one before adding — e.g. summing 2.95, 32.7, and 1.414 to the precision of 32.7 (its 3 sigdigs, 1 decimal place) means rounding to 3.0 + 32.7 + 1.4 = 37.1, not the naive 37.064.
*   **Product rule:** multiplication and division routinely manufacture spurious extra digits. Round the more-precise factor to one more sigdig than the less-precise factor before multiplying (to avoid compounding rounding error mid-calculation), then round the final result down to match the *less* precise original factor's sigdig count.

A worked example of why this matters: a widely-cited "dollars per 100th-of-a-second of response time" cost formula multiplied an hourly rate given as "$50" (1 sigdig — an estimate, not a precise measurement) against a precisely-measured transaction count. Carrying sigdigs correctly through the calculation shows the answer is only good to 1 sigdig — rounding to the nearest $100,000, not the nearest dollar the original publication reported. Applying the instrument-error rule below to that same $50 input (±$5, i.e. ±10%) brackets a valid range that the originally published, falsely-precise figure actually falls *outside* of, meaning it understated the true value despite looking exact.

## Rounding: Round-Half-to-Even

The traditional "round half up" rule (round 7.245 up to 7.25) introduces a small systematic upward bias, because 5 of the 9 possible next-digits (5–9) round up versus only 4 (1–4) rounding down. The modern fix rounds an exact trailing "5" to whichever adjacent value makes the preceding digit **even** (drop the 5 if the preceding digit is already even, round up if odd) — e.g. 7.245 rounds to 7.24, not 7.25, because 4 is already even. Most spreadsheet ROUND functions still implement the old, biased rule — do not assume a tool applies round-half-to-even by default.

## Expressing and Reporting Error

Report a measurement as $Y \pm \Delta Y$, not as a bare number:

*   **Instrument error** — a rule of thumb: uncertainty equals half the value of the smallest significant digit the instrument reports. A CPU utilization reading of "20%" should be understood (and ideally reported) as "20% ± 5%," not as an exact value.
*   **Error bars on every plot** — since error can vary per data point, error bars should too where the underlying variance is known, rather than using a single fixed margin across an entire chart.

## Practical Takeaway

The precision a capacity plan can claim is capped by its noisiest input, not its most precise one — and OS-level kernel performance counters, the ultimate source for almost every capacity-planning tool, are themselves typically only accurate to about ±5%, because they were built for OS developers, not capacity planners. Reporting more digits than that is decoration, not information.
