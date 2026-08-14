---
type: concept
title: Configuration Injection
description: >
  Environment-specific values (URLs, credentials, feature flags, resource
  limits) must be supplied to a binary at deploy time or runtime rather than
  baked in at build time, so application code stays environment-agnostic.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 2"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 16"
---

# Configuration Injection

Because [build once, deploy everywhere](build-once-deploy-everywhere.md)
forbids rebuilding a binary per environment, environment-specific
configuration (IP addresses, database URLs, feature flags, API keys, memory
settings) has to reach the running application some other way. Three options,
in order of preference:

1. **Deployment-time injection** (preferred): the deployment script writes
   environment configuration files or sets environment variables as part of
   installing the artifact into a specific environment.
2. **Runtime lookup**: the application reads configuration from a centralized
   configuration service, environment variable, or external file at startup.
3. **Build-time packaging** (anti-pattern): baking environment-specific config
   files into the binary itself. This violates build-once-deploy-everywhere
   because it forces a separate build per environment.

A template engine (ERB, Jinja, or similar string interpolation) is commonly
used to merge environment-specific property files with configuration
templates during deployment-time injection.

## Corollary: eliminate environment-conditional code

If configuration is properly externalized, application code never needs to
branch on which environment it's running in (`if (env == "PROD")`). Any such
conditional is a signal that some value that should be injected configuration
has instead been hardcoded per environment inside the binary.

Secrets are a special case of this problem with additional constraints — see
[secrets management in pipelines](secrets-management-in-pipelines.md).

## Configuration needs to be hermetic to roll back reliably

Whatever mechanism supplies configuration, it has to be replayable: rolling
back a configuration change (or rolling forward to redeploy it later) only
works if applying the same version-controlled configuration again produces
the same result every time — the same [hermetic build](hermetic-builds.md)
property, applied to configuration instead of the build step. A
configuration value that references live, independently-mutable external
state (e.g. reading a value off a shared network filesystem at apply time
rather than storing it directly in version control) breaks this: replaying
an old configuration version doesn't reproduce the old behavior, because the
external state it silently depended on has since moved on.
