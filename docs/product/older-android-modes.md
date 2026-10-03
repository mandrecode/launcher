# Older Android Modes feasibility

Research date: 2026-10-04. API 31 minimum and a legacy owned Modes workflow are the selected direction as of 2026-10-04. Actual standalone/backend compatibility remains unverified; no runtime code has been implemented.

Automatic DND rules are older than the unified Android Modes UI: caller-owned rule APIs were added at API 24 and condition updates through `setAutomaticZenRuleState` at API 29. The direct current-state query `getAutomaticZenRuleState` and user-managed-rule capability query arrived at API 35. Older Android therefore has useful DND integration, but less reliable public observation of individual rules after system/user overrides. Rule enabled configuration is not the same as currently active state. [NotificationManager reference](https://developer.android.com/reference/android/app/NotificationManager).

Two viable product tiers to evaluate:

| Tier | Activation authority | Workflow | Limits |
|---|---|---|---|
| Modern, API 35+ public capabilities | Effective owned Android rule state | rules created by Mandre Launcher, system activation, workspace mapping and reconciliation | Only our rules; OEM Modes UI/capabilities differ |
| Legacy, candidate API 31–34 | profile state owned by Mandre Launcher | Owned creation/editor, manual or time/calendar activation, matching workspace/background; optional own DND rule integration | Not a backport of OS Modes or a promise of perfect system override-state synchronization |

A shared pure domain model can describe profile definitions, schedules and workspace mappings. Backends implement capability-aware activation/observation. The legacy local authority is an explicit exception to the modern Android-authority contract. Onboarding describes this difference; optional DND integration never makes the local state proof of system activation.

Local profile selection can be easier because Mandre Launcher controls the state. Overall support adds another lifecycle/backend and older native/API fallbacks. DND contribution still needs policy access and can conflict with other system/user rules; requested state is not proof of effective state. Lowering minSdk does not lower targetSdk or recreate protected device/system effects. [DND targeting changes](https://developer.android.com/about/versions/15/behavior-changes-15#dnd-changes).

Android 12/API 31 is a sensible first compatibility candidate: the Android 17 Launcher3 build declares `min_launcher3_sdk_version = "31"`. This is a source clue, not proof that all selected support modules or our standalone port run there. Phase 1 should compile and smoke-test actual selected source/dependencies on API 31/34/35/37, then evaluate legacy Mode behavior and override recovery before committing to the lower floor. Going below API 31 would be a larger backport. [Pinned build definition](https://android.googlesource.com/platform/packages/apps/Launcher3/+/refs/tags/android-17.0.0_r1/Android.bp).

The selected minimum direction is API 31, retaining target/compile Android 17 and a same-release Pixel reference. Legacy pill defaults to visible: “Modes” when no profile is active, active profile name/icon otherwise. It can be hidden because switching remains available from a permanent Modes entry in the Home long-press menu. The visual pill stays compact while retaining a 48dp touch target. Modern system-backed persistent indicators remain optional.
