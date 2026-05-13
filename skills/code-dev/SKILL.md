---
name: code-dev
description: Standardized development protocol including planning, branching, and PR-based workflows.
---

# Code Development Protocol (code-dev)

This skill defines the standard operating procedure for all code-related tasks. It emphasizes architectural alignment, deliberate execution, and high-quality deliverables.

## Core Principles

1. **Plan First**: Never touch code without a technical strategy.
2. **Branch-PR Flow**: Use feature branches and Pull Requests for all changes.
3. **Step-by-Step (步步为营)**: Break complex tasks into manageable checkpoints.

## Procedure

### Phase 1: Planning (Architectural Alignment)
1. Create a `.ai/` directory in the repository root (ensure it's in `.gitignore`).
2. Create `.ai/PLAN.md` with the following structure:
   - **Task List**: Granular steps with checkboxes.
   - **Checkpoints**: Defined moments for user review.
3. Present the plan to the user and wait for alignment.

### Phase 2: Execution (Branching & Coding)
1. **Sync**: Ensure local `master` is up to date with `upstream`.
2. **Branch**: Create a feature branch: `feat/<desc>` or `fix/<desc>`.
3. **Implement**: 
   - Follow the plan step-by-step.
   - Run tests/linting frequently (e.g., `npm run lint`, `cargo check`).
   - Use atomic commits with clear messages.

### Phase 3: Review & Delivery
1. **Verify**: Perform a final self-review and run the full test suite.
2. **Push & PR**: 
   - Push the branch to GitHub.
   - Create a PR using `gh pr create --title "..." --body "..."`.
3. **Notify**: Inform the user that the PR is ready for review.

## Guidelines & Standards

- **Checkpoints**: Follow the alignment protocol in `references/checkpoints.md`.
- **Tooling**: Adhere to the ecosystem standards in `references/tooling.md`.

---

*Note: This skill absorbs and replaces `pr-feature-workflow`.*
