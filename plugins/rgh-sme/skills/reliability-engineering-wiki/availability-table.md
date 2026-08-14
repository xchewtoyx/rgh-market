---
type: concept
title: Availability Table
description: A reference mapping availability percentages to allowable downtime durations across different time windows.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), appendices"
---

The availability table maps target availability percentages to the exact cumulative downtime permitted within various time windows. This mapping provides the mathematical foundation for calculating [error budget](error-budget.md) size.

## Allowable Downtime Reference Table

| Availability Target | Allowable Downtime (Annual) | Allowable Downtime (Monthly - 30 Days) | Allowable Downtime (Weekly) | Allowable Downtime (Daily) |
| :--- | :--- | :--- | :--- | :--- |
| **90%** ("one nine") | 36.5 days | 72 hours | 16.8 hours | 2.4 hours |
| **99%** ("two nines") | 3.65 days | 7.2 hours | 1.68 hours | 14.4 minutes |
| **99.9%** ("three nines") | 8.76 hours | 43.8 minutes | 10.1 minutes | 1.44 minutes |
| **99.99%** ("four nines") | 52.6 minutes | 4.38 minutes | 1.01 minutes | 8.64 seconds |
| **99.999%** ("five nines") | 5.26 minutes | 25.9 seconds | 6.05 seconds | 0.86 seconds |

## Application in Service-Level Management

*   **Target Selection**: The table highlights the non-linear relationship between targets. Moving from three nines (99.9%) to four nines (99.99%) reduces allowable monthly downtime from 43.8 minutes to just 4.38 minutes, illustrating the steep increase in [cost of nines](cost-of-nines.md).
*   **Time-Budget Conversations**: Non-technical stakeholders often find time-based targets (e.g., "we can tolerate ~10 minutes of weekly downtime") easier to reason about than raw percentages. See [nines vs time-budget framing](nines-vs-time-budget-framing.md).
*   **Availability Framing**: The math assumes a binary uptime/downtime model (time-based availability). If the service uses request-based availability, the percentages represent the allowed fraction of failed requests, though the downtime minutes remain a useful framing metaphor. See [time-based vs request-based availability](time-based-vs-request-based-availability.md).
