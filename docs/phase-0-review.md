# Phase 0 review packet

Prepublication snapshot, 2026-10-04. **All ADRs accepted; initial commit/push authorized by the user. Remote CI and final protections remain pending at this snapshot.**

## Prepared outcome

Public empty repository `mandrecode/launcher`; local unborn `chore/phase-0-foundation` branch. Working tree contains architecture/ADRs, 112 planned capabilities, 40 public Modes icon source references, candidate upstream pins, reference policy, agent guides, OpenSpec change and foundation tooling. No Android build/vendor source or private MVP captures imported.

[Repository](https://github.com/mandrecode/launcher), [architecture](architecture/README.md), [ADRs](architecture/decisions/README.md), [roadmap](product/feature-plan.md), [support/reference](product/support-and-reference.md), [upstream](upstream/README.md), [delivery](delivery.md), [repository policies](github/repository-policy.md).

## Accepted decisions

- One pure Kotlin domain module with capability packages, native engine adapter and feature MVI UI; module creation follows actual slices.
- Pristine snapshot/ordered patch representation, with phase-1 manifest/hash/license verification.
- MinSdk direction is now **31**, with [an owned legacy Modes workflow](product/older-android-modes.md) and pill visible by default on API 31–34. Actual port/backend compatibility remains a phase-1 gate. Same-release Pixel reference remains required.
- Preserve native workspace model; Room owns metadata/journal only. The exact binding/store implementation follows native inspection.
- Keep upstream Dagger; prove the DI bridge before selecting Hilt for owned modules.
- Accepted stable application ID `com.mandrecode.launcher`, .dev/.beta coexistence variants; no MVP identity change now.
- Accepted [Apache-2.0 license](../LICENSE) for owned code, with [OpenSpec MIT notice](../THIRD_PARTY_NOTICES.md); neither has been published.

Non-Quickstep, API 31 minimum direction, legacy Modes access by default, interactive commit permission, same-release references, phase integration branches and gesture-quality priority reflect existing user decisions. The pill remains hideable with a permanent alternate Home-menu entry. All ten ADRs have been reviewed and accepted; compatibility spikes and runtime evidence remain future gates.

## Planned presentation decision gate

After Phase 1 supplies a verified native baseline, [Phase 1.5](product/compose-presentation-evaluation.md) evaluates native, hybrid and Compose Home presentation before Phase 2. It has a provisional 5–10-day timebox, representative real widget/drag/folder/input journeys, measured evidence and a presentation ADR. It does not authorize a rewrite or alter the non-Quickstep privilege boundary.

## Verification

Executed locally on 2026-10-04:

- `python3 scripts/check_foundation.py`: passed local links, capability IDs/status, source/reference agreement and baseline public-content guard.
- `python3 -W error::ResourceWarning -m unittest discover -s scripts/tests -v`: five tests passed without resource warnings.
- `openspec validate --all --strict`: one foundation change passed.
- Actionlint 1.7.12: workflow passed; temporary tool archive verified against upstream release checksum.
- Owned-text whitespace/public-content review: passed. No vendor Git nesting or remote branch/commit exists.
- GitHub configuration readback captured in the settings snapshot.

Remote CI cannot run until approved publication. Candidate source pins and reference templates are not runtime/device evidence. The baseline privacy guard is not a complete security scanner; public content was also reviewed for sensitive artifacts.

## Remote state

Squash-only merging, branch cleanup and read-only Actions/fork policies are configured and verified. Main deletion/force-push protection applied. Full PR/check/Copilot payload staged but not active; see repository policies. No main commit or bypass actors exist.

## Proposed commit/publication scope

The decisions and bootstrap approach are accepted. On 2026-10-04 the user authorized this reviewed scope (“You're allowed to continue now.”): create the single initial Phase 0 commit (`chore(phase-0): establish Mandre Launcher foundation`) from reviewed content, push it to main, set/verify default branch, run actual CI, activate/read back full protections and report the outcome. Do not use an unauthorized seed commit. Later phases use small stacked PRs on integration branches.

Publication/review/protection follow-up stays pending in the [task list](../openspec/changes/archive/2026-10-04-production-foundation/tasks.md). The change is not archived while those gates are open. Any follow-up edits/commits require authorization and their placement in phase history will be agreed interactively.

## Publication evidence (2026-10-04)

- Approved initial commit: [`b151c36`](https://github.com/mandrecode/launcher/commit/b151c36b280d5583dbc80e41ed95c9efdac4819e), published to `main`; GitHub default branch verified as `main`.
- [CI run 37162805759](https://github.com/mandrecode/launcher/actions/runs/37162805759): Foundation, OpenSpec and CI Status all succeeded for the published revision.
- Full ruleset `24433922` activated after CI and read back: strict three-check requirement, PRs, resolved review threads, squash-only merging, deletion/force-push prevention and Copilot review on push. No bypass actors. GitHub accepted the Copilot rule; this does not prove a review has executed or account entitlement.
- [Applied ruleset readback](github/applied-main-ruleset.json) records server defaults as well as every requested parameter. Visibility remains public; squash-only merge and merged-branch cleanup settings were verified.
- On 2026-10-04 the user authorized archival and the closing evidence commit/PR (“Go”). All 16 tasks are complete; the two capability specs are synced and the change is archived as `2026-10-04-production-foundation`. These records are delivered through the closeout PR; merge still requires human authorization. Phase 1 has not started.

The earlier sections are the initial prepublication snapshot retained for provenance; this evidence supersedes their pending remote-state descriptions.
