---
type: concept
title: Percentage Base Ambiguity
description: A percentage change depends entirely on which value is used as the denominator, and the same underlying numbers can support very different percentages depending on that choice.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 5"
---
# Percentage Base Ambiguity

A percentage change is only meaningful once its base (denominator) is specified, and the same two raw numbers can be truthfully described with very different percentages depending on which value is chosen as the base.

## Worked Example
A value dropping from $19,211 to $12,609 can be described as either a **34% loss** (the drop relative to the higher starting value) or a **52% overvaluation** (the size of the original figure relative to the lower ending value). Both are arithmetically correct; convention favors reporting relative to the starting value for "loss" framing and relative to the ending value for "overvaluation" framing, meaning the same event can be reported as substantially different-sounding percentages purely by choosing which framing to lead with.

## Verification Action
When a draft states a percentage change, confirm which value is being used as the base, and check whether that base was chosen because it's the conventional/appropriate one for the type of claim being made, or because it produces the more dramatic-sounding number. Restate the underlying raw values alongside the percentage where the base choice materially affects the reader's impression.

## See Also
- [Numeric Sanity Checking](numeric-sanity-checking.md)
