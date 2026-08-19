# Plugin per-platform defaults (issue #327)

Layer 1 of the four-layer resolver (`scripts/bundle_registry.py::resolve_bundle_config`,
see `repos/README.md` "Resolution order"): the lowest-precedence layer, shipped
inside the plugin tree itself and packaged verbatim by
`scripts/build-plugin.py` (`plan_tree()`, `PLATFORM_DEFAULTS_SRC`).

One file per `platform` enum value in
[`schemas/rgh-mms-config.schema.json`](../schemas/rgh-mms-config.schema.json)
(`github`, `ado`, `bitbucket`), each a bundle-config *fragment* validated
against that same schema. The resolver picks a file by the `platform` an
operator/committed/local layer declares (or `github` when none do), loads it
first, then overlays the three higher-precedence layers on top.

These mirror the `default` values `schemas/repo-registry.schema.json`
already documented for the equivalent `delivery.*` fields in the legacy
per-bundle registry manifest — carried forward here as the platform-wide
baseline rather than re-derived. `pr_body_closes` (GitHub's `Closes #{issue}`
keyword) is GitHub-specific and deliberately omitted from `ado.json` /
`bitbucket.json`: neither platform's PR mechanism recognizes that keyword,
and ADO-backed bundles close work items via `delivery.work_item_states`
instead (`scripts/transition-work-item-state.py`).
