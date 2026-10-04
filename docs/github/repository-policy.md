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
| Main deletion/force-push | Full active ruleset, no bypass actors |
| PR requirement / resolved threads | Active; zero mandatory approving reviews; resolved threads required |
| Required checks | 📚 Foundation, 📝 OpenSpec and ✅ CI Status active and strict; Android jobs added with the actual build |
| Copilot review | Push-review rule accepted and active; execution/entitlement not yet demonstrated |

The zero required reviewer count supports solo-owner development; **human commit and merge authorization remains mandatory in agent instructions**. GitHub cannot enforce semantic permission for each local commit. No administrative bypass is added.

CI runs for PRs against any base, including stack/integration branches. It contains no release/signing workflow, bot configuration or placeholder Android checks. No `pull_request_target` workflow executes fork code with secrets.

[Applied full ruleset](applied-main-ruleset.json) was read back after the initial publication and green [CI](https://github.com/mandrecode/launcher/actions/runs/37162805759). Every requested rule in the [full payload](full-main-ruleset.json) is active; GitHub also returns default PR parameters. The [bootstrap payload](bootstrap-main-ruleset.json) is retained as historical evidence.
