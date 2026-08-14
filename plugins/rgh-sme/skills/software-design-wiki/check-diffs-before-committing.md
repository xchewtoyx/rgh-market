---
type: concept
title: Check the Diff Before Committing
description: >
  A quick review of the full diff before committing, checking that
  documentation was updated to match every code change, is a cheap habit
  that also tends to catch leftover debugging code and unaddressed TODOs.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 16"
---

Before committing, spend a few minutes reviewing the full diff of the change
and confirm that [comments](keeping-comments-current.md) have been updated to
match every code change in it. The same pre-commit review pass tends to catch
other loose ends too — leftover debugging code, unaddressed TODOs — making it
a small, cheap discipline with a payoff broader than just comment accuracy.
