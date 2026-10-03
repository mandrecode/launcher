# ADR-0006: Public widgets and explicit provider fallbacks

Status: Accepted — all ADRs reviewed and approved by the user, 2026-10-04

Date: 2026-10-04

## Context

Google widgets expose public hosting/configuration, not all Pixel services or a fused local-search result API.

## Decision

Use actual Search/At a Glance widgets where available, requested-on by default. Preserve binding/configuration state. Own local app input with consistent geometry/tokens; integrate supported actions or neutral fallback without coordinate/glyph extraction assumptions.

## Alternatives

Private Smartspace/search result service and undocumented secure provider keys are not portable APIs. Google widget query interception is not an assumed contract.

## Consequences

Provider appearance can change. Default-search roles are version/capability-specific; unavailable actions remain clearly unavailable.

## Verification / follow-up

Compare provider-host/local-input arrangements in phase 2 before selecting permanent drawer design.
