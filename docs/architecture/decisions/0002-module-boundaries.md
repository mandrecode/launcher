# ADR-0002: One domain module and feature-oriented adapters

Status: Accepted — all ADRs reviewed and approved by the user, 2026-10-04

Date: 2026-10-04

## Context

MVI product UI and native Launcher3 need different lifecycles; native coupling must not spread.

## Decision

Use one pure Kotlin :domain with modes/workspace/appearance packages. Feature UI uses MVI; platform/persistence implement its ports. One engine adapter owns native access. engine:api remains neutral. Create real modules only with their slices.

## Alternatives

One giant app module weakens boundaries; a domain module per feature is premature. Native engine stays native rather than a second Compose state machine.

## Consequences

Some domain capabilities share a compilation boundary; split only with evidence. Keep platform types outside public contracts.

## Verification / follow-up

Enforce the graph/import rules when actual Gradle modules are introduced.
