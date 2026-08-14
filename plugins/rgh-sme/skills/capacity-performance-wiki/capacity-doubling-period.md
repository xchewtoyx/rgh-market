---
type: concept
title: Capacity Doubling Period
description: Fitting an exponential trend to periodic utilization measurements to forecast how soon consumed capacity will double, for demand that grows faster than linear procurement cycles can track.
sources:
  - title: "Guerrilla Capacity Planning"
    resource: "Guerrilla Capacity Planning (Neil J. Gunther), ch. 1"
---

For rapidly growing services (a viral consumer product, a high-growth internal platform), linear or ad hoc capacity forecasting understates how soon a resource runs out, because growth in that regime is exponential, not linear. The **capacity doubling period** is a single forecasting number — the time until currently-consumed processing capacity doubles — computed by fitting an exponential trend to periodic utilization samples.

## Method

Measure a resource's utilization $\rho$ at regular intervals (e.g. weekly) and fit:

$$\rho_W = \rho_0 \cdot e^{\Lambda W}$$

where $W$ is elapsed time (e.g. weeks) and $\Lambda$ is the fitted growth rate (any standard trendline/regression tool can fit this after taking logs, per [significant digits in capacity calculations](significant-digits-in-capacity-calculations.md) for keeping the fit's precision honest). The doubling time follows directly:

$$\tau_2 = \frac{\ln 2}{\Lambda}$$

## Why It Matters for Procurement

Doubling periods for high-growth web-scale services can run as short as 6 months — an order of magnitude faster than typical enterprise data-center growth and several times faster than Moore's Law. A demand curve doubling every 6 months means that treating a procurement decision as "we'll reassess in a year" risks discovering the shortfall only after it has already compounded 4x past the last plan. Because provisioning has lead time (ordering, delivery, install, validation), a short doubling period forces genuinely forward-looking [capacity headroom](capacity-headroom-safety-margin.md) planning rather than reactive provisioning — newly added capacity for fast-growing demand can be consumed by latent pent-up demand almost immediately if the forecast lagged reality even briefly.

## Extrapolating to a Different Configuration

The doubling-period trend is fit against the *current* hardware/software configuration's utilization curve. To translate that trend into a procurement decision for a *different* configuration (a bigger box, more nodes), the trend must be combined with a scalability model — see [the Universal Scalability Law](universal-scalability-law.md) — that translates measured utilization growth on today's platform into projected capacity requirements on the platform being considered.
