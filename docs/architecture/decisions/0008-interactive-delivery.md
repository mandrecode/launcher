# ADR-0008: Human-gated phase integration and stacks

Status: Accepted — all ADRs reviewed and approved by the user, 2026-10-04

Date: 2026-10-04

## Context

User requires explicit commit permission, interactive phases, small PRs and a coherent phase commit. Empty GitHub repositories have no PR base.

## Decision

No commit without human permission; no merge without authorization. Branches use conventional work-type prefixes, never agent names. Commit/PR titles use Conventional Commits. Small stacked PRs integrate on a phase branch; final authorized squash yields one main commit. For phase 0, use the accepted bootstrap approach of one expressly approved initial commit to main, then activate full rules after real CI.

## Alternatives

Squashing each package straight to main creates multiple main commits per phase. Adding an unapproved seed commit violates the explicit constraint.

## Consequences

First publication cannot use a PR against nonexistent main. User can instead choose an authorized seed plus PR if they prefer. No bypass actor is needed.

## Verification / follow-up

ADR and bootstrap approach accepted; explicit commit/push authorization remains required; read back full protection after first CI.
