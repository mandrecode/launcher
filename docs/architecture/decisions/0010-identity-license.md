# ADR-0010: Production identity, coexistence and source license

Status: Accepted — all ADRs reviewed and approved by the user, 2026-10-04

Date: 2026-10-04

## Context

Production is a new public repo; the MVP already uses com.mandrecode.launcher. A production install could otherwise replace it.

## Decision

Use com.mandrecode.launcher as the store ID; use .dev/.beta suffixes for development/beta to coexist with MVP. No identity migration now. Use Apache-2.0 for owned code, retaining third-party notices and Google Sans Flex OFL at import.

## Alternatives

A different production ID avoids the later collision but fragments intended naming. Copying signing keys/asset licensing from another project is inappropriate.

## Consequences

Final production install over the MVP requires explicit later data/identity planning. Public visibility is not a license grant; no LICENSE is published before this decision.

## Verification / follow-up

ID/license accepted by the user. Phase 1 adds configured variants; signing/store account/release work is deferred.
