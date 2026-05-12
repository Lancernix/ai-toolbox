---
name: skill-creator
description: Create or update Agent Skills. Use when designing, structuring, or managing skills with scripts, references, and assets.
---

# Skill Creator

This skill provides guidance for creating effective skills that extend an Agent's capabilities.

## About Skills

Skills are modular, self-contained packages that provide specialized knowledge, workflows, and tools. They transform a general-purpose Agent into a specialized one equipped with procedural knowledge and reusable assets.

### Anatomy of a Skill

Every skill consists of a required `SKILL.md` file and optional bundled resources:

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter metadata (required)
│   │   ├── name: (required)
│   │   └── description: (required)
│   └── Markdown instructions (required)
└── Bundled Resources (optional)
    ├── scripts/          - Executable code (Python/Bash/etc.)
    ├── references/       - Documentation to be loaded as needed
    └── assets/           - Files used in output (templates, etc.)
```

## Core Principles

### 1. Concise is Key
The context window is a limited resource. Only add information the Agent doesn't already have. Prefer concise examples over verbose explanations.

### 2. Actionable Triggering
The `description` in the frontmatter is the only thing the Agent reads to determine if a skill should be used. It must be clear, specific, and include triggers.

### 3. Use References for Detail
Keep `SKILL.md` lean. Move detailed schemas, API docs, or long examples to the `references/` directory.

## Design Patterns & Best Practices

### Learn Proven Design Patterns
For a comprehensive guide on authoring high-quality skills, consult:
- **Best Practices (Online - Priority)**: Always try to fetch the latest guidelines from [Claude Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md) first. Note: Filter out platform-specific (e.g., Claude Code) details to keep skills generic.
- **Best Practices (Local - Fallback)**: If offline, use `references/skill-create-best-practice.md` which contains a cleaned, platform-agnostic version of the core principles.

### Multi-step Processes
When a task is fragile or requires a specific sequence, use low-freedom scripts or detailed pseudocode.

## Workflow

### Step 1: Identify Reusable Patterns
If you find yourself repeatedly writing the same code or explaining the same complex process, it's time to create a skill.

### Step 2: Initialize the Skill
Use the provided script to scaffold a new skill:
```bash
python scripts/init_skill.py my-skill --path ./workspace/skills --resources scripts,references
```

### Step 3: Develop and Validate
- **Scripts**: Place executable logic in `scripts/`. Test them thoroughly.
- **References**: Move detailed documentation to `references/`.
- **Validation**: Use `scripts/quick_validate.py` to check for metadata errors and structural issues.

### Step 4: Iterate
Use the skill in real scenarios, notice inefficiencies, and refine the `SKILL.md` or resources accordingly.
