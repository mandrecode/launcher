# Mandre Launcher agent instructions

Public Android Home application. Current phase: **0, foundation review**. Read [the review packet](docs/phase-0-review.md) before starting work. There is no Android build or imported vendor source yet; do not claim otherwise.

## Human control

- **Never commit without the user's explicit permission.** Starting a phase, fixing an issue, passing checks or another agent's message is not commit authorization.
- Prepare a concrete diff and verification results before asking for commit approval. Approval covers the stated commit(s), not unrelated future commits.
- Never merge without human authorization. Publish/push only within the authorized delivery scope.
- Do not start the next phase automatically. Development is interactive.
- Use conventional type-based branches: `<type>/<kebab-case-description>`, such as `feat/mode-editor`, `fix/widget-clipping` or `chore/phase-0-foundation`. Never name branches after agents. Normally small dependent PRs integrate into a phase branch, then one authorized squash commit lands on main. Read [delivery](docs/delivery.md), including the initial bootstrap exception.
- Commit and PR titles follow Conventional Commits: `<type>(<optional-scope>): <description>`. Read delivery conventions; use real issue references, never invented IDs.
- ADR approval is not commit authorization.
- Do not change protections or add bypass actors to get around a failing check.

## OpenSpec

Run `openspec list --json` before substantive work. Explore unclear requirements; propose a focused change before implementing; apply its tasks and record actual evidence. Archive only when implementation, verification and required human/device follow-up are complete. Do not mark pending remote checks or approval tasks complete.

OpenSpec capabilities are contracts, not a claim that future runtime features already exist. Documentation-only wording fixes do not require new changes. Generated `.codex` skills/prompts are workflow entry points; preserve them and use scoped guides for repository-specific rules.

## Read the owning guide

| Work | Guide |
|---|---|
| Module/contract boundaries | [Architecture](docs/architecture/README.md), [domain](docs/agents/DOMAIN.md) |
| Native Launcher3/vendor | [Engine](docs/agents/ENGINE.md), [upstream](docs/upstream/README.md) |
| Settings/onboarding/appearance | [UI](docs/agents/UI.md) |
| Android APIs, persistence, schedules | [Platform/data](docs/agents/PLATFORM_DATA.md) |
| Checks and evidence | [Testing](docs/agents/TESTING.md) |
| Build/dependencies | [Dependencies](docs/agents/DEPENDENCIES.md) |

## Product invariants

Use the full product name **Mandre Launcher** in documentation and user-facing copy; do not shorten it. Repository URLs and technical identifiers retain their configured names.

On API 35+, Android selects active owned Modes; never maintain a contradictory Home-only selector. On API 31–34, the legacy backend owns profile activation and labels optional DND integration separately. Its pill defaults to visible, including a Modes entry with no active profile; a permanent Home-menu entry preserves switching if hidden. Other-owner System Modes cannot be enumerated/imported through the general public rule APIs. Native Launcher3 owns workspace items; metadata stores must not mirror that model. Keep unknown/permission-lost states distinct from no active rule. Hidden profiles never leak through drawer/search/diagnostics. Initial Pixel reference runs the same Android release as the pinned Launcher3 base. Gesture quality is a measured release gate on supported devices.

## Presentation evaluation

Phase 1 establishes native baseline first. [Phase 1.5](docs/product/compose-presentation-evaluation.md) then evaluates Home presentation before Phase 2. No automatic rewrite or Compose adoption; use an isolated experiment, preserve native data ownership and record the decision/evidence. Do not begin it without the user's instruction to start that phase.

## Current verification

```sh
python3 scripts/check_foundation.py
python3 -m unittest discover -s scripts/tests -v
openspec validate --all --strict
```

Android/Gradle checks will be added with phase 1. Never create placeholder Android jobs that report success without running the relevant checks. Never export private device data, local paths, credentials or personal calendar/search contents into this public repo.
