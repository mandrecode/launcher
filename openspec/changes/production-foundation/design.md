## Context

A public empty repository now exists; the local phase branch has no commits. Repository settings were inspected and configured with recorded readback. Phase 0 creates contracts/governance only. Required human decisions and publication gates remain visible.

## Goals / Non-Goals

**Goals:** agent-readable ownership; same-release reference policy; realistic Modes/gesture boundaries; reviewed ADRs; reproducible documentation checks; staged protections and phase delivery.

**Non-Goals:** importing vendor source, choosing unchecked latest dependencies, building an APK, migrating MVP data, signing/releasing or committing without permission.

## Decisions

Use one pure Kotlin domain module and feature presentation modules; preserve native Launcher3 behind a narrow adapter. Vendor inputs remain candidate pins until phase-1 manifest/archive verification. API 31 is the minimum-support direction pending compatibility verification. Legacy API 31–34 owns profile activation with a default-visible pill and permanent alternate Home-menu entry; modern API 35+ observes owned Android rules. Both use durable identity and operation recovery, not fixed slots. Phase integration/stack workflow is accepted; initial-main publication requires a separately approved bootstrap exception.

Documentation checker verifies local links, roadmap IDs, source pin format, reference release agreement and absence of forbidden artifacts. CI runs on all PR bases, not just main. Foundation/OpenSpec checks exist now; Android checks enter only with executable build tasks. Use squash-only merging and read-only workflow tokens; require only executable checks available in the current phase.

## Risks / Trade-offs

- Empty repo has no PR base → prepare complete local content and request initial commit/push authorization.
- Applying required PR checks too early blocks bootstrap → apply deletion/force-push prevention first, then full rules after actual main CI.
- Proposed ADRs mistaken for accepted decisions → explicit status and review packet.
- Public import leaks private evidence → only portable researched metadata; no MVP captures, logs, local paths or signing assets.
- Domain/module plan overbuilt before native port → target structure only; create modules with real slices.

## Migration Plan

No existing application/data migration. After approval, publish Phase 0 initial main, run real CI, activate full rules and verify readback. Keep the OpenSpec change active until review/publication/protection tasks are complete. Later phases use integration PRs. Never disable protection to mask failed checks.

## Open Questions

All ten ADRs are accepted, including module boundary, vendor representation, SDK direction, DI spike, license/application identity and bootstrap approach. Initial-bootstrap commit/push authorization was received on 2026-10-04; actual publication and remote gates remain pending. Branches describe conventional work types; commit and PR titles use Conventional Commits. No routine bypass actor proposed.
