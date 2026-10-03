# ADR-0007: Initial SDK proposal and same-release Pixel reference

Status: Accepted — all ADRs reviewed and approved by the user, 2026-10-04

Date: 2026-10-04

## Context

Universal-phone ambition must be separated from tested support and exact API/minor capabilities.

## Decision

Select minSdk 31 as the product direction; verify selected sources/dependencies on API 31 in phase 1. Compile/target latest stable Android 17. API 31–34 gets a Modes workflow owned by Mandre Launcher with the pill visible by default and a permanent alternate menu entry; API 35+ follows effective owned Android rule state. Pixel baseline uses the same Android release as pinned Launcher3 and records exact OS/app/display/nav configuration. Certify devices only with evidence.

## Alternatives

Android 12/API 31 is a compatibility candidate: older Android has automatic DND rules but lacks the API-35 per-rule active-state query. A legacy workflow owned by Mandre Launcher is feasible in principle, with an explicitly different authority contract. See [older Android research](../../product/older-android-modes.md). The lower floor requires a phase-1 port/backend spike; a newer-major Pixel reference invalidates baseline comparisons.

## Consequences

Pixel 7/manual plus deterministic emulator is insufficient for non-Pixel certification. Test Samsung/another OEM before supporting those families.

## Verification / follow-up

Compile/smoke-test the selected standalone port and dependencies on API 31/34/35/37, then verify both Modes backends. Actual reference bundles/device builds are captured during implementation, not fabricated in phase 0. A failed compatibility spike is reported for a support decision, not silently worked around.
