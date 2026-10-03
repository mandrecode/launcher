# Phase 1.5: Home presentation evaluation

Planned decision gate after the clean standalone Launcher3 phase and before Pixel-parity implementation. This schedules an evaluation, not adoption of Compose or authorization to begin it now. Non-Quickstep remains the system-integration boundary for every standalone candidate.

## Why this point

Phase 1 provides a working native engine, verified API-31 compatibility direction, baseline journeys/performance and a reproducible port/update process. Comparing before that risks blaming Compose or native Views for port defects. Comparing after extensive Pixel UI work risks sunk-cost decisions. Evaluate the presentation boundary while it is still inexpensive to choose.

## Hypotheses

- A Compose Home presentation can offer worthwhile ownership/adaptability benefits while retaining native workspace persistence and supported widget hosting.
- A hybrid approach may retain difficult native interactions with less coupling than either a complete rendering rewrite or widespread native presentation patches.
- Native Views may remain the best choice if coupling or regression costs exceed the benefits. Keeping them is a valid outcome of the experiment.

These hypotheses concern presentation, not a fully owned launcher engine or privileged task-window control.

## Bounded prototype

Provisional timebox: 5–10 engineering working days, reviewed after Phase 1 measurements. If the prototype cannot reach its agreed representative journeys within that budget, report what prevented it and decide whether to extend; do not quietly turn it into an unbounded rewrite.

Use an isolated experimental variant/source set on a phase integration branch. Production still selects native Home. Preserve one authoritative workspace writer and one active presentation per run; test with disposable fixtures, not a user's primary Home data. Commit/push/merge approvals follow the existing interactive delivery policy.

Implement only enough to evaluate risky seams:

- A representative Home grid and dock, icon launch/move, page motion and opening/interacting with a folder.
- A real hosted widget with touch interaction and resize, checking clipping and gesture arbitration rather than a static placeholder.
- Swipe-up drawer, cancellation, local app input/IME and return to Home.
- Process recreation and persistence through the native model; no separate Compose favorites database.
- Keyboard/focus/TalkBack, large text and two relevant window sizes. Verify available work/private profile isolation; explicit unsupported gaps block adoption rather than becoming hidden certification claims.

No Modes automation, rich search, premium features or full Pixel polish in this experiment. A test screen/background selection can exercise adapter binding, but does not implement Android Modes.

## Compare evidence

Run equivalent fixtures/journeys on native baseline and candidate using the same hardware, Android release, build mode, navigation mode, palette and refresh rate. Cover API 31 and the Android 17 reference; include available non-Pixel hardware and a lower-performance device before adopting a broader support claim. Missing hardware coverage is a recorded gap, not a passing result.

Measure frame timing/jank, app-to-Home readiness, startup/memory and gesture discontinuities; record widget/drag/folder/input/accessibility correctness. Capture native APIs/hooks still required, patch surface, migration/recovery work and maintenance burden. A short prototype cannot establish long-term reliability or future rebasing cost; distinguish observations from forecasts.

Numeric budgets come from Phase 1 and are agreed before implementing the comparison. Improved visual control alone does not outweigh data, widget, profile or accessibility regressions. Compose does not itself overcome the system gesture/Quickstep privilege boundary.

## Decision and exit gate

Deliver a comparison report, recordings/traces, known gaps and a presentation ADR before Phase 2 begins. Choose explicitly:

1. **Native:** retain native Home and pursue configuration/resources/minimal presentation patches.
2. **Hybrid:** define exactly which surfaces and interaction owners remain native versus Compose, with measurable integration cost.
3. **Compose presentation:** adopt incrementally over the retained engine only if the prototype justifies it; create the needed implementation/migration tasks rather than declaring the prototype production-ready.

If evidence is inconclusive, native remains the default unless the user approves an extension. No silent technology switch. A fully owned engine or system-integrated Quickstep edition requires a separate feasibility decision.

Record the outcome in a new ADR, linking [ADR-0001](../architecture/decisions/0001-standalone-non-quickstep.md). If presentation changes, supersede only that part of the original decision; the non-Quickstep system-integration choice remains valid unless independently revisited. Follow normal small PR/stack review and one authorized phase-integration squash commit on main.
