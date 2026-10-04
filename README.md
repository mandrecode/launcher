# Mandre Launcher

A Pixel-like Android launcher with system-driven Modes and quality-of-life features.

**Status: Phase 0 ADRs accepted; foundation published; CI passed and main protections active. Foundation change archived with synced contracts; closing evidence is delivered through a review PR. There is no installable application yet.**

Mandre Launcher will start from a clean AOSP Launcher3 Android 17 non-Quickstep baseline. Native workspace, folders, dock, widgets and launcher transitions stay native. Pixel presentation is added next; Modes, optional drawer themed icons and double-tap sleep follow.

On API 35+, Android remains the authority for Modes activation. API 31–34 uses an owned legacy profile workflow with a Modes pill visible by default; it remains hideable with a permanent Home-menu entry. Public APIs expose our app-owned rules, not every pre-existing System Mode. Proprietary Pixel intelligence, Recents replacement and privileged system-gesture integration are outside the standalone product contract.

## Start here

- [Phase 0 review packet](docs/phase-0-review.md): decisions, evidence and publication steps.
- [Architecture](docs/architecture/README.md) and [ADRs](docs/architecture/decisions/README.md).
- [Product scope and roadmap](docs/product/README.md), [112 capabilities](docs/product/feature-plan.md) and [CSV](docs/product/feature-plan.csv).
- [Support and Pixel reference policy](docs/product/support-and-reference.md).
- [Delivery and PR stacks](docs/delivery.md), [Repository policies](docs/github/repository-policy.md).
- [Upstream strategy](docs/upstream/README.md) and [candidate source pins](docs/upstream/sources.lock.json).
- [Agent instructions](AGENTS.md) and [archived OpenSpec foundation change](openspec/changes/archive/2026-10-04-production-foundation/proposal.md).

## Verify the foundation

Python 3.11+, Node.js 22+ and OpenSpec CLI 1.3.0 are the Phase 0 tools. No Android SDK or Gradle build is required yet.

```sh
python3 scripts/check_foundation.py
python3 -m unittest discover -s scripts/tests -v
npx --yes @fission-ai/openspec@1.3.0 validate --all --strict
```

Never commit without the user's explicit permission. Normal development uses phase integration branches and small stacked PRs; each completed phase is squash-merged to one commit on main with authorization. The initial empty-repository bootstrap is separately described in the review packet.

The [Apache-2.0 license](LICENSE) is accepted under ADR-0010 and published with the foundation. [Third-party notices](THIRD_PARTY_NOTICES.md) preserve the OpenSpec workflow license. Publication followed explicit human approval.
