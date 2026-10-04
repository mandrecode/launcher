# product-foundation Specification

## Purpose
Define Mandre Launcher’s standalone engine ownership, platform and Modes boundaries, source provenance, same-release Pixel reference policy, gesture quality gates and presentation evaluation before implementation.

## Requirements
### Requirement: Standalone engine ownership
The product foundation SHALL document a non-Quickstep Launcher3 baseline, a single pure Kotlin domain module and one native adapter boundary without claiming privileged system integration.

#### Scenario: Agent prepares native implementation
- **WHEN** an agent reads the architecture and engine guides
- **THEN** the guides identify which module owns native access and preserve Launcher3's native workspace/model ownership

### Requirement: Same-release Pixel reference
Pixel fidelity evidence MUST use the same Android release as the pinned Launcher3 baseline and record device, OS/app versions and display/navigation configuration.

#### Scenario: A comparison targets a different release
- **WHEN** a proposed reference runs a newer Android major release than the baseline
- **THEN** it is not accepted as that baseline's fidelity evidence

### Requirement: Honest capability and source status
Foundation artifacts SHALL distinguish planned features and candidate pins from implemented behavior and verified imports; other-owner Modes discovery SHALL NOT be promised.

#### Scenario: Candidate source pins are recorded
- **WHEN** Phase 0 records upstream revisions without importing source archives
- **THEN** the lock identifies them as candidate-not-imported and does not fabricate archive checksums

#### Scenario: Existing Android Modes are discussed
- **WHEN** the product describes setup for rules owned by another app or the system
- **THEN** it offers explanation/templates rather than unsupported enumeration or automatic policy import

### Requirement: Gesture quality gates
The reference policy SHALL require native visual/timing evidence for app-to-Home and interrupted gestures before device certification.

#### Scenario: Home return has a launcher-caused wallpaper flash
- **WHEN** a supported qualification journey exposes a blank or black wallpaper frame caused by Mandre Launcher
- **THEN** the defect blocks qualification instead of being declared an unavoidable smoothness limitation

### Requirement: Capability-aware Modes access
The product foundation SHALL select API 31 as the minimum-support direction subject to standalone verification, distinguish legacy owned profile activation from modern effective system-rule activation, and define a default-visible legacy pill with a permanent alternate Home-menu entry.

#### Scenario: Legacy user has no active profile
- **WHEN** the user runs the legacy backend on API 31–34 with the default indicator preference
- **THEN** the documented workflow retains a compact Modes entry that opens the owned switcher even when no profile is active

#### Scenario: Legacy user hides the pill
- **WHEN** a legacy user disables the persistent pill
- **THEN** the documented Home long-press menu still provides a permanent Modes entry

#### Scenario: Modern backend receives a toggle request
- **WHEN** the modern backend requests an owned rule change
- **THEN** workspace selection follows observed effective Android state rather than the requested UI state

### Requirement: Presentation decision before Pixel parity
The foundation SHALL schedule a bounded native/hybrid/Compose Home presentation evaluation after the verified Phase 1 engine baseline and before Phase 2, with a comparison report and explicit presentation ADR rather than automatic adoption.

#### Scenario: Native baseline is not ready
- **WHEN** Phase 1 has not established the required standalone engine baseline
- **THEN** the evaluation is not treated as ready to begin

#### Scenario: Presentation evidence is inconclusive
- **WHEN** the bounded experiment does not justify a presentation change
- **THEN** native presentation remains the default unless the user explicitly approves an extension or different decision

