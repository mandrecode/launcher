# Native engine and vendor ownership

Only engine:launcher3-adapter may access native Launcher3 internals from owned code. Runtime must not import feature/application business implementations. Keep native workspace/model/widget host authoritative. Public integration API exports neutral values and acknowledgements, not Context, views or database handles.

Read the upstream guide before edits. Never mutate pristine snapshots, add nested Git repositories, patch generated output as the source of truth, or enable dormant flags merely because they exist. Keep port/hooks/presentation lanes separate. Add contract-focused native journey evidence for changes affecting binding, gestures, model schemas, profiles or widget lifecycle.

Non-Quickstep is mandatory for the standalone baseline. Reusable support libraries are audited individually; importing privileged Quickstep/SystemUI code does not grant its permissions.
