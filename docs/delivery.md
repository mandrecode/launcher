# Interactive delivery and phase integration

Never commit without explicit human permission; never merge without authorization. Starting a phase is not commit approval. Prepare reviewed content, verification and a specific commit/push plan. Keep development interactive and do not start another phase automatically.

Normal flow:

1. Create `chore/phase-N-name` from main.
2. Divide work into small OpenSpec-backed packages on conventional type-based branches such as `feat/mode-editor` or `fix/widget-clipping`. Branch names describe the work, never an agent. After authorized commits, PRs target the phase branch or preceding stack branch.
3. Review/verify each package, integrate bottom-up and retarget/restack dependent PRs carefully. Each child requires its own checks. No unauthorized history rewriting or forced pushes.
4. The final phase PR targets main and reports all exit gates, decisions, changes and remaining limits.
5. Authorized squash merge produces one identifiable phase commit on main. Intermediate reviews remain in package PR history.

CI runs for PRs against all branches, including integration/stack bases. Stable required check names come from actual executable jobs. Main requires PRs, up-to-date checks and resolved review threads; no routine bypass. Copilot review is advisory, never a substitute for human commit/merge authorization.

## Initial repository bootstrap (completed)

The empty-repository exception was completed on 2026-10-04 with explicit human authorization. The reviewed foundation was published directly to `main` as [`b151c36`](https://github.com/mandrecode/launcher/commit/b151c36b280d5583dbc80e41ed95c9efdac4819e), without a separate seed commit. Main became the default branch, [its first CI run passed](https://github.com/mandrecode/launcher/actions/runs/37162805759), and the full main ruleset was activated and read back with no bypass actors. See [repository policies](github/repository-policy.md) for the verified configuration.

Before that initial publication, only deletion/force-push prevention was active; PR and required-check rules were deliberately deferred until main and its checks existed. This is historical bootstrap sequencing, not the current protection state or authorization for another direct push to main.

The [Phase 0 closeout PR](https://github.com/mandrecode/launcher/pull/2) delivers the archive and publication evidence under the active protections. It remains subject to human merge authorization. Future phases follow the normal PR/integration workflow above; this bootstrap exception is exhausted.

Completed publication order: privacy/content review → human commit/push approval → initial main commit → first CI → full protections/readback → OpenSpec completion/review evidence. No signing keys or release workflow were introduced in this phase.

## Conventional naming

Branches use `<type>/<kebab-case-description>`; phase integration branches use `chore/phase-<N>-<slug>`. Work packages use the appropriate type: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore` or `revert`. No agent-name prefixes. `.codex` workflow files are tooling paths and do not define branch names.

Commit and PR titles follow Conventional Commits: `<type>(<optional-scope>): <description>`. Use `!` and a `BREAKING CHANGE:` footer for breaking changes where appropriate. Examples: `feat(modes): add calendar conditions`, `fix(widgets): preserve resize state`, and `chore(phase-0): establish Mandre Launcher foundation`. Reference real issues in the body/footer; never invent IDs. The final integration PR title supplies the squash commit title.
