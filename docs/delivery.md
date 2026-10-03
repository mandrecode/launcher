# Interactive delivery and phase integration

Never commit without explicit human permission; never merge without authorization. Starting a phase is not commit approval. Prepare reviewed content, verification and a specific commit/push plan. Keep development interactive and do not start another phase automatically.

Normal flow:

1. Create `chore/phase-N-name` from main.
2. Divide work into small OpenSpec-backed packages on conventional type-based branches such as `feat/mode-editor` or `fix/widget-clipping`. Branch names describe the work, never an agent. After authorized commits, PRs target the phase branch or preceding stack branch.
3. Review/verify each package, integrate bottom-up and retarget/restack dependent PRs carefully. Each child requires its own checks. No unauthorized history rewriting or forced pushes.
4. The final phase PR targets main and reports all exit gates, decisions, changes and remaining limits.
5. Authorized squash merge produces one identifiable phase commit on main. Intermediate reviews remain in package PR history.

CI runs for PRs against all branches, including integration/stack bases. Stable required check names come from actual executable jobs. Main requires PRs, up-to-date checks and resolved review threads; no routine bypass. Copilot review is advisory, never a substitute for human commit/merge authorization.

## Initial repository bootstrap

An empty repository has no base commit for a PR. Current local branch is `chore/phase-0-foundation` with no commits. Accepted bootstrap approach, still requiring explicit commit/push authorization: after reviewing the complete Phase 0 content and expressly authorizing commit/push, create its single initial commit and push that commit to remote main. Do not invent an empty/bootstrap commit before approval. Select main as default, verify its real CI run, then activate the full main ruleset without bypass actors. Future phases use the normal PR/integration workflow.

Only deletion/force-push prevention is applied before bootstrap; required PR/status-check enforcement is staged until main and its checks exist. Report this temporary state explicitly. If the user prefers a minimal seed commit plus a Phase 0 PR instead, that requires separate authorization and changes the one-initial-commit history preference.

Publication order: privacy/content review → human commit/push approval → initial main commit → first CI → full protections/readback → OpenSpec completion/review evidence. No signing keys or release workflow in this phase.

## Conventional naming

Branches use `<type>/<kebab-case-description>`; phase integration branches use `chore/phase-<N>-<slug>`. Work packages use the appropriate type: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore` or `revert`. No agent-name prefixes. `.codex` workflow files are tooling paths and do not define branch names.

Commit and PR titles follow Conventional Commits: `<type>(<optional-scope>): <description>`. Use `!` and a `BREAKING CHANGE:` footer for breaking changes where appropriate. Examples: `feat(modes): add calendar conditions`, `fix(widgets): preserve resize state`, and `chore(phase-0): establish Mandre Launcher foundation`. Reference real issues in the body/footer; never invent IDs. The final integration PR title supplies the squash commit title.
