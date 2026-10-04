# Repository policies

Repository settings inspected on 2026-10-04 through GitHub REST API. [Readback snapshot](settings-snapshot.json) records actual configuration, including the active main-branch rules.

| Policy | Verified configuration |
|---|---|
| Visibility | Public |
| Merge strategy | Squash only; PR title; blank commit body |
| Delete merged branch | Enabled |
| Auto merge / update branch | Disabled |
| Workflow tokens | Read; cannot approve PR reviews |
| Allowed Actions | All; our workflow uses verified immutable action SHAs |
| Fork approval | First-time contributors new to GitHub |
| Main deletion/force-push | Full active ruleset, no bypass actors |
| PR requirement / resolved threads | Active; zero mandatory approving reviews; resolved threads required |
| Required checks | 📚 Foundation, 📝 OpenSpec and ✅ CI Status active and strict; Android jobs added with the actual build |
| Copilot review | Push-review rule active; execution verified on PR #2 before and after a follow-up push |

The zero required reviewer count supports solo-owner development; **human commit and merge authorization remains mandatory in agent instructions**. GitHub cannot enforce semantic permission for each local commit. No administrative bypass is added.

CI runs for PRs against any base, including stack/integration branches. It contains no release/signing workflow, bot configuration or placeholder Android checks. No `pull_request_target` workflow executes fork code with secrets.

[Applied full ruleset](applied-main-ruleset.json) was read back after the initial publication and green [CI](https://github.com/mandrecode/launcher/actions/runs/37162805759). Every requested rule in the [full payload](full-main-ruleset.json) is active; GitHub also returns default PR parameters. The [bootstrap payload](bootstrap-main-ruleset.json) is retained as historical evidence.

## Copilot execution evidence

Copilot submitted a [review of the closeout commit](https://github.com/mandrecode/launcher/pull/2#pullrequestreview-5404732735) (`bfb495b`) and a [review after the follow-up push](https://github.com/mandrecode/launcher/pull/2#pullrequestreview-5404773338) (`81d5dde`) on 2026-10-04. This demonstrates review execution for this repository and PR; it does not guarantee future availability or entitlement. The initial activation evidence in the Phase 0 review packet predates these reviews.
