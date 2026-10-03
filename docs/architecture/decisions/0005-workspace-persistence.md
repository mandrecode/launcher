# ADR-0005: Native workspace ownership and operation recovery

Status: Accepted — all ADRs reviewed and approved by the user, 2026-10-04

Date: 2026-10-04

## Context

Independent screens must survive native model binding, process death and widget/provider changes.

## Decision

Room stores metadata/mappings/journal; Launcher3 stores native items. Adapter serializes switches with generation acknowledgements. Delete widget IDs/assets only when unreferenced across all screens. Restore recreates/remaps rules and requires widget consent.

## Alternatives

A Room mirror of all native favorites introduces two authorities; an unjournaled database switch risks partial state.

## Consequences

Multiple stores need idempotent recovery and versioned migration/rollback tooling. Native schema compatibility is an upstream risk.

## Verification / follow-up

Define native store/binding contract after phase-1 source inspection; test process death at every operation boundary in phase 3.
