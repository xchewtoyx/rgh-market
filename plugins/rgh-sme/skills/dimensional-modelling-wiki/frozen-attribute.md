---
type: concept
title: Frozen Attribute
description: An attribute whose value is fixed permanently at a specific point in time, such as age at signing — modeled as a computed type 1 attribute, not a new slow-change type.
sources:
  - title: "Star Schema: The Complete Reference"
    resource: "Star Schema: The Complete Reference (Christopher Adamson), ch. 8"
---

Some requirements ask for an attribute to be "frozen" at a point in time — for example, `age_at_signing` on an insurance policy, which should never change no matter how many times the policy or the customer's other attributes are later updated. This can look like it needs a fourth [slowly changing dimension](slowly-changing-dimension.md) response ("do nothing"), but it fits the existing type 1/type 2/type 3 framework once the attribute is defined carefully, rather than requiring a new technique.

Most frozen attributes are really [type 1](slowly-changing-dimension-type-1.md) attributes whose value is *computed* from another, more fundamental source at the moment the row is created — not a value that is copied in and then must resist being overwritten. `age_at_signing`, for instance, is the difference between the policy's effective date and the customer's birth date, computed once during ETL when that dimension row is built; there is nothing to "freeze," because the attribute was never wired up to change in the first place. This is often paired with a genuinely type 1 `current_age` and a type 2 `historic_age`, both sourced from the same underlying birth-date fact, to serve the different questions "how old is this customer today" versus "how old were they at each point in the past."

In statutory-reporting contexts, an attribute that looks frozen can instead be exhibiting real type 1/type 2 hybrid behavior (see [slowly changing dimension type 6](slowly-changing-dimension-type-6.md)): updatable like an ordinary type 1 attribute up until the value has been externally reported, after which any further change must generate a new dimension row (type 2) rather than silently overwrite a figure that has already been submitted externally.
