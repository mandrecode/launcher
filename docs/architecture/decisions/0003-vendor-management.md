# ADR-0003: Pristine snapshots with ordered patches

Status: Accepted — all ADRs reviewed and approved by the user, 2026-10-04

Date: 2026-10-04

## Context

The MVP has edited vendor snapshots; production needs repeatable imports and updates.

## Decision

Track pristine pinned sources; apply 00-port, 10-hooks and 20-pixel patches into ignored build output. Record SHA/tag/archive hashes/license inventory. No nested editable .git directories.

## Alternatives

Submodules complicate separate-fork pushes/agent checkout; subtree merges are viable but less explicit patch ownership. Neither solves API compatibility automatically.

## Consequences

Requires import/apply/report scripts. A patch that applies textually still needs semantic contract tests.

## Verification / follow-up

Manifest verification, archive hashes, minimal port and update rehearsal are phase 1 gates.
