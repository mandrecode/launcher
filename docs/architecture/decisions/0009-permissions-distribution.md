# ADR-0009: Feature-scoped consent and graceful recovery

Status: Accepted — all ADRs reviewed and approved by the user, 2026-10-04

Date: 2026-10-04

## Context

Modes/widgets/notification dots/calendar/precise schedules/lock gesture have distinct grants and failure states.

## Decision

Onboarding explains limits and requests access only for chosen features. Setup is resumable; recheck grants on resume. Double-tap lock uses a narrow opt-in AccessibilityService with disclosure, no content scraping; notifications requested only when actually used.

## Alternatives

A blanket permission wall makes optional functionality appear mandatory. DeviceAdmin lock is not the default fallback.

## Consequences

Accessibility distribution needs Play review/declaration; calendar/private data never enter public diagnostics. Permission loss preserves layouts.

## Verification / follow-up

Permission matrix and denial/resume journeys specified in onboarding phase; verify store requirements before beta.
