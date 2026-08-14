---
type: concept
title: Name and Address Parsing, Standardization, and Verification
description: >
  Why loading names and addresses into elemental parsed fields instead of
  generic catch-all columns is a prerequisite for both segmentation
  analytics and basic data quality.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 8"
---

Source systems frequently store names and addresses in a handful of generic
catch-all columns (`Name-1` through `Name-3`, `Address-1` through
`Address-6`) rather than structured fields. Loading that structure as-is is
close to worthless for analysis — there's no way to isolate a salutation,
first name, or suffix; multiple entities sometimes end up packed into one
name field; descriptive junk ("Confidential," "Trustee") gets mixed into
name fields; and inconsistent abbreviations defeat any downstream matching
against postal or geocoding reference data.

The load-time fix has three distinct steps, usually run during extraction
rather than left for later transformation:

1. **Parse** each field into as many elemental parts as the source data
   actually supports (salutation, first/middle/last name, street number,
   street name, unit, city, region, postal code).
2. **Standardize** the parsed values against a consistent form (`Rd` →
   `Road`, `Ste` → `Suite`) so the same real-world value isn't scattered
   across multiple spellings.
3. **Verify** the standardized result against reference data (e.g., that a
   ZIP/postal code and state/region combination is actually valid).

Purpose-built commercial cleansing/scrubbing tools generally outperform
hand-rolled parsing logic for this, the same way [deduplication and
survivorship](deduplication-and-survivorship.md) recommends specialized
matching tools once volume and ambiguity get high enough. Which parsed
elements are worth keeping is a business call, not a purely technical one —
loop in whoever owns data governance for the entity being parsed rather than
keeping every technically extractable fragment by default.

**International data adds a hard requirement, not just more parsing rules**:
end-to-end Unicode support, not just at the database layer but through every
hop a name or address value passes through — capture screen, ETL tooling,
storage, and every downstream rendering surface (report writer, browser).
A pipeline that's Unicode-clean in the database but truncates or mangles
non-ASCII characters somewhere in transit has a latent data quality bug that
a purely-English test dataset will never surface; validate it directly by
pushing a non-ASCII value through the full path from capture to final
output rather than trusting each component's stated compliance in
isolation.
