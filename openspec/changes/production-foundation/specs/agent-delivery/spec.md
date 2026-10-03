## ADDED Requirements

### Requirement: Explicit human commit authorization
Agents MUST obtain explicit human permission before creating any commit, including foundation and intermediate stack commits, and MUST NOT treat starting a phase as authorization to commit.

#### Scenario: Preparation is complete but permission is absent
- **WHEN** files and local checks are ready and the user has not authorized a commit
- **THEN** the agent presents the concrete review packet and leaves changes uncommitted

### Requirement: Phase integration delivery
Normal delivery SHALL use small reviewable PRs against a phase integration branch or preceding stack branch and one authorized squash commit per completed phase on main.

#### Scenario: A dependent work package is reviewed
- **WHEN** a child stack PR targets its parent branch
- **THEN** its own CI runs and its dependencies/base are documented

### Requirement: Initial repository bootstrap
An empty repository SHALL remain without commits until the user approves the stated bootstrap exception; full main protections SHALL be activated only after the base branch and real check contexts exist.

#### Scenario: No main branch exists
- **WHEN** Phase 0 is prepared in the empty repository
- **THEN** publication/protection activation remains an explicit pending step and no base commit is created automatically

### Requirement: Executable foundation verification
CI SHALL run foundation validation, checker regression tests and strict OpenSpec validation for PRs against all bases and aggregate their real outcomes.

#### Scenario: A required foundation check fails
- **WHEN** a required dependency job fails, is cancelled or is unexpectedly skipped
- **THEN** the aggregate CI status fails instead of reporting green

### Requirement: Evidence-backed repository policies
Repository policies SHALL identify actual repository settings and pending protections separately without requiring unavailable Android check names.

#### Scenario: Runtime build is absent
- **WHEN** Phase 0 defines required checks before Android scaffolding exists
- **THEN** it requires executable foundation checks and defers Android checks to the phase introducing them

### Requirement: Conventional work naming
Branches SHALL use conventional work-type prefixes rather than agent names, and commit/PR titles SHALL use Conventional Commits.

#### Scenario: Foundation branch is prepared
- **WHEN** a phase integration branch is named for foundation work
- **THEN** its name describes the work, such as chore/phase-0-foundation, without an agent prefix

#### Scenario: An accepted ADR is ready for publication
- **WHEN** the user accepts an ADR but has not authorized a commit
- **THEN** the agent records acceptance without creating a commit
