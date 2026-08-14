---
type: concept
title: Significant Digit Discipline
description: A calculated result can never be reported to more significant digits than its least-precise input actually supports, no matter how many digits the arithmetic produces.
sources:
  - title: "Guerrilla Capacity Planning"
    resource: "Guerrilla Capacity Planning (Neil J. Gunther), ch. 3"
---

# Significant Digit Discipline

Arithmetic on measured numbers (as opposed to exact counts) manufactures digits that look precise but carry no real information — a calculator or spreadsheet will happily report a result to ten decimal places regardless of how uncertain the inputs were. **Significant digit discipline** is the practice of reporting a calculated result to no more precision than its least-precise input actually justifies. Gunther calls the failure to do this the "sin of precision" — the mirror image of omitting information, but just as misleading: it presents a false sense of exactness that the underlying measurement never had.

## The governing rule

A calculation's result is never more precise than its least-precise input. Concretely:
- **Sum/difference**: round every addend to the same decimal precision as the least-precise addend *before* combining them; the result carries that same precision.
- **Product/quotient**: round the result to the same number of significant digits as the least-precise factor (when combining unequal-precision factors, round the more-precise one to one extra digit first, to avoid compounding rounding error partway through the calculation, then apply the final rounding at the end).

A number's significant-digit count is not obvious from its face value: "50" (no explicit decimal point, trailing zero) carries only 1 significant digit, while "50.0" carries 3 — the same numeral written two ways represents two very different claims about how well the underlying quantity is actually known.

## Why this is a verification concern, not just a style rule

A published figure computed from a low-precision input but reported with many digits invites a reader to trust it more than the evidence supports — and, worse, the exact reported number can end up **outside the range the honest error bars would have produced**. A published cost-per-transaction figure computed from a stated "$50/hour" input (one significant digit, i.e., an unstated ±$5 uncertainty) should have been reported as a range spanning roughly ±10% of the final result; the originally published exact-looking figure fell entirely outside that legitimate range, meaning the excess precision didn't just look misleading — it was actually wrong in a checkable way once the input's real uncertainty was propagated through.

## Verification action

Before accepting a calculated figure:
1. Identify the least-precise input feeding into it and count its actual significant digits (watch for exact-vs-measured confusion — "$50" as a guessed hourly rate is a measured number with 1 significant digit, not an exact quantity).
2. Recompute the result at that precision, and compare it against the number as published. A mismatch — especially the published figure landing outside the range implied by the least-precise input's real uncertainty — is a specific, checkable defect, not a stylistic quibble.
3. Treat a suspiciously precise-looking derived number (many decimal places, no stated error) as a prompt to ask what its actual inputs were and how precisely they were known, rather than accepting the appearance of rigor as evidence of it.

This complements [numeric sanity checking](numeric-sanity-checking.md), which catches order-of-magnitude and unit errors, and [claim scope calibration](claim-scope-calibration.md), which calibrates a claim's stated *confidence* to its evidence — significant digit discipline calibrates a claim's stated *precision* to its evidence, the numeric-formatting analogue of the same principle.
