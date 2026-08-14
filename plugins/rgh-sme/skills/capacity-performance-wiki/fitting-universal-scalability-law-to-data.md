---
type: concept
title: Fitting the Universal Scalability Law to Data
description: How to estimate the contention and coherency parameters of the Universal Scalability Law from a handful of throughput measurements using ordinary linear regression, and the caveats that apply with sparse data.
sources:
  - title: "Guerrilla Capacity Planning"
    resource: "Guerrilla Capacity Planning (Neil J. Gunther), ch. 5, ch. 6"
---

[The Universal Scalability Law](universal-scalability-law.md) is a rational function (a ratio of polynomials), which most spreadsheet and regression tools can't fit directly — there's no built-in "rational function" trendline type. It must be algebraically transformed into an ordinary polynomial first.

## The Linearization

Starting from the USL, $C(p) = p / [1 + \sigma(p-1) + \kappa p(p-1)]$, divide both sides by $p$ to get processor/worker **efficiency**, then invert:

$$\frac{p}{C(p)} = 1 + \sigma(p-1) + \kappa p(p-1)$$

This is a plain quadratic in $p$: $y = ax^2 + bx + c$. Defining $Y = p/C(p) - 1$ and $X = p - 1$ gives:

$$Y = \kappa X^2 + (\sigma + \kappa) X$$

which matches the general quadratic with the intercept forced to zero ($c=0$) — exactly the constraint needed to reduce three polynomial coefficients down to the USL's two physical parameters.

## Fitting and Recovering the Parameters

1.  Measure throughput $X(p)$ at several concurrency levels, always including (or estimating) $p=1$ as the normalization point.
2.  Compute $C(p) = X(p)/X(1)$ for each measured point.
3.  Compute the transformed variables $X = p-1$ and $Y = p/C(p) - 1$.
4.  Fit a quadratic through the origin, $Y = aX^2 + bX$, via ordinary least-squares regression.
5.  Recover the physical parameters: $\kappa = a$, $\sigma = b - a$.
6.  Compute the capacity-maximizing concurrency directly from the regression coefficients: $p^* = \lfloor (1+a-b)/a \rfloor$ (equivalent to the $p^*$ formula in [the Universal Scalability Law](universal-scalability-law.md), useful as a cross-check).

**Validity checks the regression itself doesn't enforce:** for $\sigma, \kappa$ to be physically meaningful they must both be non-negative, which requires the fitted coefficients satisfy $a, b \ge 0$ and $b > a$. If a fit produces a negative coefficient or violates $b > a$, that's a sign of a data or normalization problem (see below), not a valid alternative parameterization.

**Rule of thumb for the fit quality:** an $R^2$ (coefficient of determination) between roughly 0.7 and 1.0 indicates a good fit; use at least 4 data points, since 3 points can always be fit exactly by *some* parabola regardless of whether the model is actually appropriate.

## Working With Sparse or Incomplete Data

Real capacity data is rarely the full sweep the ideal recipe wants. Two situations come up often:

*   **Few, unevenly-placed measurements.** Fitting to only a handful of small-concurrency points can produce wildly different $\sigma, \kappa$ estimates than a fit using the full range — smaller-range fits are prone to attributing throughput ceilings to the wrong term (e.g., inflating the coherency estimate by an order of magnitude relative to a fit over the full range) because they can't see recovery or continued growth that only appears at higher concurrency. This isn't a flaw in the method — it correctly reflects that predictions are sensitive to which data is and isn't available, which is itself a reason to report error/residuals alongside any fitted projection rather than treating it as exact.
*   **Missing the $p=1$ normalization point.** If single-unit throughput was never measured (common when data wasn't originally collected with this analysis in mind), estimate it from the smallest available measured point $p_0$: $\hat{X}(1) = X(p_0)/p_0$. This likely *underestimates* true $X(1)$ because it assumes linear scaling all the way down to $p=1$, which can even push the fitted curvature negative (violating the $a \ge 0$ validity check above) — if that happens, nudge the estimate upward manually until the fit becomes physically valid again.

## Watch Excel-Class Tools' Precision on the Coherency Term

The coherency coefficient $\kappa$ is often very small in absolute terms (e.g. $10^{-5}$–$10^{-6}$), and the capacity-maximizing point $p^*$ depends on it through a square root in the denominator ($p^* = \sqrt{(1-\sigma)/\kappa}$) — a tool with limited floating-point precision in its regression engine can underestimate a small $\kappa$ by a large relative margin, which then propagates into a substantially *overestimated* $p^*$ (a documented case showed roughly a 2x error in the fitted $\kappa$ translating into a ~50% overestimate of $p^*$). If $\kappa$ comes out very small relative to $\sigma$, cross-check the fit in a tool with better numerical precision (or one that can fit the rational function directly rather than requiring the linearization above) before trusting the projected capacity ceiling.

## Why This Matters Operationally

This regression method turns a small set of cheap, small-scale measurements into a projection across the full concurrency range — including concurrency levels that would be expensive, impractical, or licensing-constrained to measure directly. See [virtual load testing via a scalability model](virtual-load-testing-via-scalability-model.md) for using this projection in place of exhaustive real load testing.
