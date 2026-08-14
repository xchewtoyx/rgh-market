---
type: concept
title: Behavior-Oriented Test Naming
description: >
  Name tests as plain-English facts about domain behavior for a non-programmer
  audience — rigid Method_Scenario_Result templates couple names to implementation.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 3"
---

The `[MethodUnderTest]_[Scenario]_[ExpectedResult]` convention is prominent but
least helpful — it encourages focusing on implementation details rather than
behavior. Plain English phrases describe behavior meaningfully to a domain
expert without boxing the author into a rigid structure.

Example progression for "delivery with past date is invalid":

1. `IsDeliveryValid_InvalidDate_ReturnsFalse()` — rigid, unhelpful.
2. `Delivery_with_invalid_date_should_be_considered_invalid()` — plain English but vague.
3. `Delivery_with_past_date_should_be_considered_invalid()` — specific about "invalid."
4. `Delivery_with_past_date_should_be_invalid()` — trims filler.
5. `Delivery_with_past_date_is_invalid()` — state as fact, not wish ("should be").
6. `Delivery_with_a_past_date_is_invalid()` — grammatical fluency.

**Guidelines**:

- No rigid naming policy — complex behavior won't fit a template.
- Name as if describing the scenario to a non-programmer domain expert.
- Separate words with underscores for long test names (not test class names).
- `[ClassName]Tests` is an entry point for a unit of behavior — tests need not
  verify only that class.
- **Do not include the method-under-test name** — you test behavior, not code;
  renaming `IsDeliveryValid` → `IsDeliveryCorrect` should not force test renames.
  Exception: utility code with no business logic may use the method name.

See [test and fake class naming conventions](test-naming-conventions.md),
[black-box versus white-box testing](black-box-vs-white-box-testing.md), and
[aaa test structure](aaa-test-structure.md).

## Parameterized tests

When one unit of behavior has many facets, parameterized tests (e.g. xUnit
`[Theory]` + `[InlineData]`) group similar cases — rename the method generically
since it no longer states one specific fact.

**Trade-off**: less test code but lower readability as parameters multiply.
Mitigation: extract the positive case into its own descriptively named test;
parameterize only negative cases. Keep positive and negative together in one
parameterized method only when input parameters make the case self-evident;
otherwise give each case its own method.

For runtime-computed data, use member-data sources instead of compile-time
inline attributes.

## Fluent assertion libraries

Libraries like Fluent Assertions reorder assertions into plain-English story form
— `[Subject] [action] [object]` (e.g. `result.Should().Be(30)` vs
`Assert.Equal(30, result)`). Additional dependency cost is acceptable for
development-only tooling.
