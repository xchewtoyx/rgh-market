---
type: concept
title: Blame Suppresses Reporting and Learning
description: >
  Punishing individuals after failure teaches everyone else to hide mistakes,
  cutting off the information flow that safety learning depends on — without
  removing a single error trap.
sources:
  - title: The Field Guide to Understanding 'Human Error'
    resource: "The Field Guide to Understanding 'Human Error' (Dekker), ch. 1"
  - title: The DevOps Handbook
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 4"
  - title: The Fearless Organization
    resource: "The Fearless Organization (Edmondson), ch. 4"
---

The most reliable effect of firing, prosecuting, or disciplining a
practitioner after a failure is not deterrence of error — errors are not
chosen — but deterrence of *disclosure*. Terminating "Bad Apples" signals
others to hide mistakes and evidence; the underlying error traps remain,
now invisible. After the ValuJet 592 mechanics were criminally prosecuted,
reporting was stifled while the supply-chain defects that caused the fire
went unfixed (see [authority–responsibility
mismatch](authority-responsibility-mismatch.md)).

The mechanism matters because almost everything an organisation can learn
about its real risks arrives voluntarily: near-miss reports, workaround
descriptions, "this procedure doesn't work" complaints, bad news carried
upward. Blame prices honesty out of the market, which:

- blinds leadership to [drift](drift-into-failure.md) and [normalised
  deviance](normalization-of-deviance.md), since those show up only in candid
  accounts of normal work;
- defeats [chronic unease](chronic-unease.md) — there is no bad news to hear
  if bearing it is punished;
- degrades reports that do arrive: formal reporting under blame pressure
  strips out the contextual detail that makes reports useful (see
  [just culture](just-culture.md) on confidential vs formal reporting).

The software-operations version of the pattern: after a customer-affecting
incident, management attributes the root cause to human error and
"names, blames, and shames" the responsible person, then adds process and
approvals — combining the [quick fix](fallacy-of-the-quick-fix.md) with the
reporting freeze. The inversion is stated crisply by Bethany Macri (Etsy):
"By removing blame, you remove fear; by removing fear, you enable honesty;
and honesty enables prevention."

The remedy is structural, not exhortative: a [restorative just
culture](just-culture.md) in which giving an honest account is safe, and in
which the organisation's response to failure is visibly aimed at fixing
*what*, not punishing *who* — the messenger-handling row that separates
generative from pathological cultures in the [Westrum
typology](westrum-typology.md). See [dangerous silence in high-risk
systems](dangerous-silence-in-high-risk-systems.md) for cases where people
felt literally unable to speak up — Columbia, Tenerife, Dana-Farber, Fukushima
— and why exhorting individual courage fails as a strategy.
