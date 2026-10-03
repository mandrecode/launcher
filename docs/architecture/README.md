# Architecture boundary proposal

Architectural direction accepted by the user on 2026-10-04. Runtime implementation and compatibility still require the documented gates. See [ADRs](decisions/README.md).

```text
app                         APK composition root, entry points and owned navigation
build-logic                 Convention plugins and dependency constraints
engine:api                  Pure Kotlin native integration contracts
engine:launcher3-runtime    Patched native engine, no feature/app imports
engine:launcher3-adapter    Only owned module accessing Launcher3 internals
domain                      One pure Kotlin module: modes/, workspace/, appearance/
core:designsystem           Shared owned Compose components and semantic tokens
core:persistence            Room metadata and DataStore implementations
features:*                  MVI presentation modules
platform                    Public Android gateway implementations
benchmark                   Native journeys and baseline profiles
```

This is a target structure, not a set of pre-created empty Gradle modules. Introduce modules as their vertical slices begin. Do not add a `modes-domain` alongside `domain`.

Business ports/models reside in domain. Engine API contracts describe native operations and acknowledgements. Adapter maps between them and owns binding/lifecycle synchronization. Neither API exports Context, Launcher, ItemInfo, Cursor, RemoteViews or database handles. Domain has no Android, Compose or persistence dependencies.

Feature UI depends on domain/design system; platform, persistence and the adapter implement domain ports; the app composes those implementations. Runtime cannot import app/features/domain business implementations. Avoid feature-to-feature presentation dependencies. Shared values move into domain only when genuinely shared.

Keep upstream Dagger intact. Verify a narrow bridge before adopting Hilt for owned UI. Room stores metadata/operation journals; Launcher3 keeps native items/schema. Cross-service operations require idempotent reconciliation, not an assumed global transaction.

Native Home continues using Launcher3's state machine and Views. Owned settings/onboarding use immutable Contract UiState/UiEvent/UiEffect, thin ViewModels and Screen/Content separation. Do not run competing native and Compose Home state machines over the same workspace. The isolated Phase 1.5 evaluation may investigate a candidate presentation with one authoritative engine and one active presentation per run.

The initial native Home choice can be revisited through a reviewed experiment and superseding ADR. [ADR-0001](decisions/0001-standalone-non-quickstep.md) preserves Compose presentation, an owned engine, system-integrated Quickstep and a supported-public-API transition layer as deferred directions with evidence gates. Rendering-independent domain contracts support exploration, but do not make native engine replacement automatic.

Before Phase 2, [Phase 1.5](../product/compose-presentation-evaluation.md) measures native versus hybrid/Compose presentation and records the selected approach in a presentation ADR. The listed native presentation remains the production default until that decision; the module graph is reviewed if evidence justifies a change.
