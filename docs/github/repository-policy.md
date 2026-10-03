# Repository policies

Repository settings inspected on 2026-10-04 through GitHub REST API. [Readback snapshot](settings-snapshot.json) records actual configuration separately from the staged main-branch rules.

| Policy | Current configuration / planned activation |
|---|---|
| Visibility | Public |
| Merge strategy | Squash only; PR title; blank commit body |
| Delete merged branch | Enabled |
| Auto merge / update branch | Disabled |
| Workflow tokens | Read; cannot approve PR reviews |
| Allowed Actions | All; our workflow uses verified immutable action SHAs |
| Fork approval | First-time contributors new to GitHub |
| Main deletion/force-push | Applied bootstrap-safe ruleset, no bypass actors |
| PR requirement / resolved threads | Prepared; zero mandatory approving reviews; activate after first main/CI |
| Required checks | Foundation, OpenSpec and CI Status prepared; Android jobs added with the actual build |
| Copilot review | Push-review rule prepared; availability verified on activation |

The zero required reviewer count supports solo-owner development; **human commit and merge authorization remains mandatory in agent instructions**. GitHub cannot enforce semantic permission for each local commit. No administrative bypass is added.

CI runs for PRs against any base, including stack/integration branches. It contains no release/signing workflow, bot configuration or placeholder Android checks. No `pull_request_target` workflow executes fork code with secrets.

[Applied bootstrap ruleset](applied-main-ruleset.json) prevents deletion/force pushes but does not yet require PRs or checks. [Full payload](full-main-ruleset.json) is staged for application after approved initial publication and real green CI. Read back final rules rather than claiming they are already active.
