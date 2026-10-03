# ADR-0001: Standalone non-Quickstep foundation

Status: Accepted — all ADRs reviewed and approved by the user, 2026-10-04

Date: 2026-10-04

## Context

Mandre Launcher is a normally installed Home app across manufacturers; it cannot assume platform trust or control Recents.

## Decision

Use Android 17 non-Quickstep Launcher3. Preserve native Home; leave system navigation/Recents with the device. Reuse compatible support libraries, not privileged system implementations.

## Alternatives

These alternatives are **deferred, not permanently rejected**. The accepted decision applies to the initial standalone product. A future change in evidence or distribution can justify a superseding ADR; preserve this record and link that decision rather than silently rewriting its history.

| Path | Potential benefit | Main cost or constraint | Evidence that would justify reconsideration |
|---|---|---|---|
| Compose Home presentation with native behavior retained where practical | Greater control of owned UI, adaptability and motion; more unified presentation tooling | Native model, view/state machinery and widget hosting are coupled; rendering replacement needs explicit integration work | A bounded prototype demonstrates widget interaction, drag/drop, folders, accessibility and gesture performance at least as reliable as the native baseline, with lower measured maintenance cost |
| Fully owned launcher engine and Compose Home | Greater independence from native presentation internals and control of product behavior | Reimplementing workspace/model lifecycle, migration, widgets, profiles, input/accessibility and motion greatly expands reliability work | Native upgrade costs repeatedly exceed a quantified owned-engine budget, and an incremental replacement plan preserves behavior/data with acceptable performance |
| System-integrated Quickstep edition | Access to the intended Recents/navigation/task-animation integration | Compiling Quickstep does not grant system trust, permissions or binding; ordinary installation is insufficient | An OEM/custom-ROM integration with the necessary platform cooperation, or supported public APIs enabling the required capabilities |
| Owned transition layer through supported public APIs | Improve achievable standalone Home motion without adopting the privileged Quickstep stack | Cannot assume control of system gesture recognition or task-window handoff; may add OEM-sensitive lifecycle behavior | A targeted prototype closes a measured defect on supported devices, improves frame/input traces and does not introduce hidden-API or privileged dependencies |

A Compose presentation experiment is distinct from replacing the entire launcher engine. Either can improve owned motion, but changing UI technology does not itself grant Quickstep/SystemUI authority. These are research directions, not promised roadmap features or authorization to start a rewrite.

## Consequences

Gesture gap is an explicit measured workstream from the clean-engine phase. Only tested combinations are certified.

## Verification / follow-up

Resolve/pin manifest inputs and demonstrate standalone build in phase 1. Then run the planned [Phase 1.5 presentation evaluation](../../product/compose-presentation-evaluation.md) before Phase 2 Pixel presentation work. The outcome selects native, hybrid or Compose presentation on evidence; it does not automatically change the non-Quickstep system boundary.

## Revisit protocol

1. Record the concrete problem: repeated upstream port cost, inadequate adaptability, persistent gesture defects or a new system-integration opportunity. Establish baseline evidence before proposing a technology change.
2. Propose a separately reviewed OpenSpec experiment with bounded scope, hypotheses, comparison journeys and stop/go criteria. No experiment is started automatically by this ADR.
3. For Compose presentation, include real hosted widget input/resize, icon/folder drag, process recreation, work/private profile isolation, keyboard/IME/accessibility and low-end frame/memory measurements. For system integration, first verify actual permission/binding feasibility.
4. Compare the experiment against both the standalone native baseline and same-release Pixel reference. Assess maintenance, migration and recovery costs as well as visual fidelity.
5. If successful, create a superseding ADR and incremental delivery plan. Preserve ADR-0001 as the historical initial decision.

Keep domain and platform contracts independent of Home rendering so researched alternatives can reuse business logic. This does not promise a drop-in engine swap: native model/presentation coupling must be assessed and adapted explicitly. Candidate branches or prototypes must preserve data and remain outside the production path until accepted.
