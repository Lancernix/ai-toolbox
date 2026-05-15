# Tooling Standards

Follow these standards to maintain consistency across projects.

## Git & GitHub
- **Branching**: `feat/` for features, `fix/` for bugs, `refactor/` for code improvements.
- **Commits**: Use [Conventional Commits](https://www.conventionalcommits.org/).
- **GitHub CLI**: Always use `gh` for PR management. Remember to `export GH_CONFIG_DIR` as noted in `MEMORY.md`.

## Node.js / TypeScript
- **Package Manager**: `npm` (unless `pnpm` or `yarn` is already present).
- **Style**: Use [Biome](https://biomejs.dev/) for linting and formatting if available; otherwise, fall back to Prettier/ESLint.

## Rust
- **Toolchain**: `cargo`.
- **Validation**: Always run `cargo check` and `cargo test`.

## Python
- **Environment**: Use `uv` or `venv` for isolated environments.
- **Formatting**: Use `ruff` if available.
