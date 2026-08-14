---
type: concept
title: Absurdity Test for Range Estimation
description: Building an uncertainty range by starting from an impossibly wide bound and narrowing toward plausibility avoids the anchoring trap of starting from a single point-estimate and padding it.
sources:
  - title: "How to Measure Anything: Finding the Value of Intangibles in Business"
    resource: "How to Measure Anything, 3rd ed. (Douglas W. Hubbard), ch. 5"
---
# Absurdity Test for Range Estimation

Building a confidence range by starting from a single point-estimate and adding/subtracting a margin tends to **anchor** the range too narrowly around that first number — the point estimate exerts a pull that the padding rarely escapes. The absurdity test reverses the direction: start from a range you know is impossibly wide (e.g., "this factory cost between $1,000 and $10 billion") and narrow it by successively rejecting values you're confident are implausible in each direction, until you reach the edge of genuine plausibility. This reframes the task from "what do I think this value is" to "what do I know is ridiculous" — a question people can usually answer confidently even when they insist they have "no idea" about the value itself.

## Testing Each Bound Independently
A companion technique: treat each end of a 90% confidence interval as its own separate yes/no question. For the upper bound, ask "am I 95% sure the true value is below this?" (a 90% CI leaves 5% probability in each tail, so each bound is a 95%-confidence question on its own). Evaluating the two bounds independently, rather than as a single "give me a range" task, further resists the tendency to anchor both bounds too close together around an implicit central guess.

## Worked Example
A participant who initially said she had "no idea" about a Boeing 747's wingspan had, on questioning, actually given an unreflectively narrow 100-120 ft range. Successive absurdity-test questions ("could it be 20 ft? 500 ft? 300 ft?") walked her to a genuinely-felt 90% CI of 50-250 ft — demonstrating that "no idea" respondents typically hold usable bounds once the anchoring point-estimate framing is removed from the elicitation.

## Verification Action
When eliciting or evaluating a subjective range from a source (an expert's estimate, a stakeholder's forecast), be suspicious of a narrow range produced by directly asking "give me your estimate and error bars" — this framing invites anchoring. Prefer or request a range built by first identifying implausible extremes and narrowing inward, and check the upper and lower bounds as independent claims rather than as a single symmetric interval around a guess.

## See Also
- [Calibrated Probability Assessment](calibrated-probability-assessment.md)
- [Equivalent Bet Calibration Test](equivalent-bet-calibration-test.md)
