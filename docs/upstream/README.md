# Launcher3 source and update policy

No vendor source is imported in Phase 0. [Candidate pins](sources.lock.json) record the researched Android 17 revisions; phase 1 must resolve the release manifest and verify archives/checksums/licenses before import.

Launcher3 is a platform app, not a Maven engine SDK. Non-Quickstep is the selected Home variant; the device retains its own Recents/gesture provider. Untouched non-Quickstep sources can still need platform dependencies: the public-SDK port is owned maintenance work. Reusable SystemUI icon/animation libraries do not confer privileged SystemUI authority.

Preferred representation: pristine tracked snapshots plus ordered patches; generated patched output ignored by Git. No editable nested `.git` repositories. Keep optional fetch mirrors outside the source tree. Pin Launcher3 and required support revisions together.

Patch lanes: `00-port` build/platform adaptation; `10-hooks` neutral engine extension seams; `20-pixel` unavoidable native presentation. Prefer configuration/resources over source changes. Modes business logic remains owned Kotlin outside vendor.

Before adding product features, build a port-only variant and rehearse a source update. If no suitable newer revision exists, replay the complete import and patches from scratch and document the weaker evidence; that is not proof of future conflict-free upgrades.

Each import records remote, immutable SHA/tag, archive digest, licenses/NOTICE and support dependencies. Each patch records purpose, affected contract, upstream context and verification. Review schemas, Dagger wiring, native flags, resources and lifecycle changes even when textual patches apply cleanly.

Sources: [Android 17 Launcher3](https://android.googlesource.com/platform/packages/apps/Launcher3/+/refs/tags/android-17.0.0_r1), [SystemUI support libraries](https://android.googlesource.com/platform/frameworks/libs/systemui/), [AOSP release guidance](https://source.android.com/docs/setup/about/faqs).
