## Why

The MVP demonstrated useful behavior but mixes standalone Launcher3 porting, Pixel presentation and Modes integration. Production needs a clean, agent-readable foundation with explicit platform limits and reproducible delivery before engine implementation begins.

## What Changes

- Create the public `mandrecode/launcher` repository and local Phase 0 integration branch without making a commit.
- Capture module boundaries, candidate upstream pins, support/reference policy and permission-sensitive product contracts.
- Add scoped agent instructions, ADRs, feature roadmap, OpenSpec configuration and foundation verification.
- Inspect and configure repository policies, with actual executable check names and explicit bootstrap activation.
- Prepare a human review packet; commit, push and first-main bootstrap remain permission-gated.
- No Android scaffolding, vendor source import, app migration, signing key or dependency installation in this phase.

## Capabilities

### New Capabilities

- `product-foundation`: documented product/platform boundaries, architecture, source provenance and same-release reference policy.
- `agent-delivery`: explicit commit authorization, phase integration/stack workflow, executable foundation checks and staged repository protections.

### Modified Capabilities

None. This is a new repository without accepted capability specs yet.

## Impact

A new public GitHub repository, documentation, local governance tools and CI configuration. The existing MVP remains untouched. Runtime/build work is deferred to `standalone-launcher3-baseline` after Phase 0 review.
