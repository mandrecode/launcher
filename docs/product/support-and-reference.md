# Support and reference policy

## Initial support proposal

Minimum Android 12/API 31 is the agreed product direction; compile/target latest stable Android 17 SDK at phase-1 implementation. Actual standalone source/dependency compatibility and device behavior still require verification before certification. API 31–34 uses the owned legacy Modes backend; API 35+ uses observed owned Android rule state where supported. Minor SDK additions are independently capability-gated; API 37 alone does not imply APIs introduced at 37.2.

No phone family is certified yet. Pixel 7 can be a manual comparison device when running the matching release; use a same-release emulator for deterministic checks. Before non-Pixel beta support, test Samsung and another OEM plus a lower-performance phone. Foldable/tablet support follows explicit native/adaptive validation. All phones is the product direction, not today's support claim.

## Modes entry policy

On API 31–34, show the Modes pill by default, below Search when present and safely above navigation insets. When no profile is active, retain a compact “Modes” entry; when a profile is active, show its name/icon. Tapping opens the owned switcher. The pill remains optional: a permanent Modes entry in the Home long-press menu keeps switching reachable if the pill is hidden. Use a small visual capsule with a 48dp touch target and integrate its space/motion with the native layout.

On API 35+, preserve the system-backed activation contract and optional persistent active-mode indicator. Pill actions request rule changes and the workspace follows observed effective state. Document backend differences during onboarding; do not describe legacy profile selection as observed system activation.

## Accepted reference rule

Pixel comparison MUST run the same Android release as the selected Launcher3 baseline. Record the AOSP tag/SHA and Pixel OS build; component build identities are not interchangeable. Refresh references explicitly for maintenance/quarterly changes; never silently compare against a newer Android major release.

Every bundle records device/model, OS build/API/minor version, Pixel Launcher and Google app versions, density, font scale, grid, navigation mode, refresh rate, wallpaper/palette, locale, permissions and recordings. Freeze variable clocks/weather for visual comparisons where possible. Distinguish supported reference behavior from current Google help pages describing later model/locale rollouts.

## Gesture gate

Begin in phase 1 with stock and port-only measurements; improve in phase 2; repeat OEM qualification before beta. Test warm/cold app-to-Home, repeated/interrupted gestures, app launches, drawer/cancellation, IME and pending Mode switches. Record frame traces, visual discontinuities and input readiness.

Launcher-caused black/blank wallpaper, stale workspace flashes, clipped widgets, duplicate transitions or lost input readiness block release. Numeric budgets follow measured native baseline and display refresh rate. An unacceptable system handoff blocks certification of that device/OS/navigation combination. Do not promise privileged Quickstep parity.

## Versioned bundle template

Copy [the reference template](reference-bundle.template.json) for each actual capture. A template containing nulls is not validation evidence. Personal captures remain outside Git until privacy review; use anonymized fixtures for public artifacts.
