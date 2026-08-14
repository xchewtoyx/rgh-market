---
type: concept
title: "The Three D's: Infrastructure Failure Troubleshooting Framework"
description: A checklist of three likely root causes — drift, dependencies, and environment differences — to investigate systematically when an infrastructure change fails unexpectedly.
sources:
  - title: Infrastructure as Code Patterns and Practices
    resource: "Infrastructure as Code, Patterns and Practices (Rosemary Wang), ch. 11"
---

When an infrastructure change fails in production despite passing everywhere it was tested, three categories of root cause cover most real cases:

- **Drift** — the running system no longer matches what's declared in version control, usually because of an unremediated [out-of-band change](out-of-band-change-remediation.md) made directly against the cloud console during a past incident. Check for exactly this before assuming the newly-applied code itself is at fault.
- **Dependencies** — an unmapped or broken implicit dependency: IAM service account roles, subnet routes, sidecar proxies, or an external SaaS provider that the failing change touches indirectly but that isn't visible in its own code.
- **Differences in environments** — configuration divergence between the environment the change was tested in and production: mismatched SDK versions, a missing proxy binary, or different IAM permissions that only show up once the change reaches an environment the test suite didn't actually cover.

Once a specific cause is identified, [roll-forward remediation](roll-forward-remediation.md) restores availability, and reconciliation closes the gap that caused the failure: fold any drift-causing manual fix back into version control (see [out-of-band change remediation](out-of-band-change-remediation.md)), bring the divergent environment back into alignment with production so future tests there are trustworthy, and then re-apply the original intended change incrementally — for example widening a permission grant one narrow step at a time (`cloudsql.client` before `cloudsql.admin`) rather than jumping straight back to the change that just failed — testing thoroughly in the now-reconciled environment before promoting to production again.

This framework is a practical complement to [failure scenario mapping](failure-scenario-mapping.md): failure scenario mapping is proactive, brainstorming what could go wrong ahead of time, while the three D's are reactive, giving a fast first pass at diagnosing what actually did go wrong.
