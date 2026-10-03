# ADR-0004: Owned Android rules and deterministic workspace resolution

Status: Accepted — all ADRs reviewed and approved by the user, 2026-10-04

Date: 2026-10-04

## Context

Only caller-owned AutomaticZenRules are generally observable. System policy, Room and native workspaces cannot form a global transaction.

## Decision

On API 35+, Android effective owned-rule state is authority. On API 31–34, Mandre Launcher owns profile activation and may contribute DND rules separately; requested DND state is not proof of effective system state. Share profile definitions/resolution across these explicitly different backends. Legacy pill is visible by default, including a “Modes” entry when no profile is active; hiding it preserves access through the permanent Home menu entry. Durable ModeId differs from RuleId. User priorities resolve overlaps; keep eligible current workspace on ties, then stable ID order. Unknown reads differ from no active rule. Templates are new owned modes, not imports.

## Alternatives

Aggregate DND cannot reconstruct hidden Mode identity. Fixed Work/Unwind slots and competing Home selectors do not meet the product contract.

## Consequences

Honor user-managed policy/snoozes and platform quotas; no blanket unlimited creation promise. Phase 3 journals operations and reconciles interruption.

## Verification / follow-up

Spike system manual activation, ownership, user-managed updates and public state observation before implementing the final scheduler.
