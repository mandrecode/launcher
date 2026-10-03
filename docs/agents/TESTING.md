# Verification ownership

Phase 0: foundation checker, checker regression tests and strict OpenSpec validation. No Android checks exist yet. Record actual results in the review packet; local checks are not a remote CI pass.

Later: deterministic domain tests (coroutine test clock, Turbine, Truth; useful fakes/MockK), contract/persistence migrations, native instrumented journeys and owned UI tests. Android automation uses reproducible emulators; manual smoke prefers the user's Pixel 7 when compatible. Never run intrusive automated cases on the user's personal device without authorization.

Native motion needs recordings plus frame/input traces. Compose screenshot tests cover relevant owned layout/token regressions but cannot validate app-to-Home gesture handoff. Baselines must be reviewed, never regenerated simply to hide failures. Track real OEM capability evidence and unsupported combinations explicitly.

Do not test unchanged upstream internals for coverage. Gate owned code and changed native contracts; isolate legacy vendor lint baselines. Required checks must actually execute; propagate failures, skipped dependencies and cancellation to the CI aggregate gate.
