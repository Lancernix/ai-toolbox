#!/usr/bin/env python3
"""
Skill Initializer - Creates a new skill from template

Usage:
    init_skill.py <skill-name> --path <path> [--resources scripts,references,assets] [--examples]

Examples:
    init_skill.py my-new-skill --path skills/public
    init_skill.py my-new-skill --path skills/public --resources scripts,references
    init_skill.py my-api-helper --path skills/private --resources scripts --examples
"""

import argparse
import re
import sys
from pathlib import Path

MAX_SKILL_NAME_LENGTH = 64
ALLOWED_RESOURCES = {"scripts", "references", "assets"}

SKILL_TEMPLATE = """---
name: {skill_name}
description: [TODO: Complete and informative explanation of what the skill does and when to use it. Include WHEN to use this skill - specific scenarios, file types, or tasks that trigger it.]
---

# {skill_title}

## Overview

[TODO: 1-2 sentences explaining what this skill enables]

## Best Practices
- Keep this skill concise. Use `references/` for detailed docs if necessary.
- [TODO: Add specific constraints or guidelines for this skill.]

## Workflow

[TODO: Define the primary workflow or tasks here.]

## Resources (optional)

### scripts/
Executable code (Python/Bash/etc.) that performs automation or data processing.

### references/
In-depth documentation, API references, or detailed guides that the Agent should reference while working.

### assets/
Templates, boilerplate code, or files used in the final output.
"""

def normalize_skill_name(name):
    """Normalize skill name to hyphen-case."""
    name = name.lower()
    name = re.sub(r"[^a-z0-9]+", "-", name)
    name = name.strip("-")
    return name

def title_case_skill_name(name):
    """Convert hyphen-case name to Title Case."""
    words = name.split("-")
    return " ".join(word.capitalize() for word in words)

def parse_resources(resources_str):
    """Parse comma-separated resource list."""
    if not resources_str:
        return set()
    resources = {r.strip() for r in resources_str.split(",")}
    invalid = resources - ALLOWED_RESOURCES
    if invalid:
        print(f"[ERROR] Invalid resources: {', '.join(invalid)}")
        sys.exit(1)
    return resources

def create_resource_dirs(skill_dir, skill_name, skill_title, resources, include_examples):
    """Create resource directories and optional examples."""
    for resource in resources:
        resource_dir = skill_dir / resource
        resource_dir.mkdir(exist_ok=True)
        print(f"[OK] Created {resource}/")
        
        if include_examples:
            if resource == "scripts":
                (resource_dir / "example_script.py").write_text("#!/usr/bin/env python3\nprint('Hello from script')\n")
            elif resource == "references":
                (resource_dir / "api_reference.md").write_text("# API Reference\nDetails here.")
            elif resource == "assets":
                (resource_dir / "example_asset.txt").write_text("Example asset content.")

def init_skill(skill_name, path, resources, include_examples):
    """Initialize a new skill directory."""
    skill_dir = Path(path).resolve() / skill_name

    if skill_dir.exists():
        print(f"[ERROR] Skill directory already exists: {skill_dir}")
        return None

    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
        print(f"[OK] Created skill directory: {skill_dir}")
    except Exception as e:
        print(f"[ERROR] Error creating directory: {e}")
        return None

    skill_title = title_case_skill_name(skill_name)
    skill_content = SKILL_TEMPLATE.format(skill_name=skill_name, skill_title=skill_title)

    try:
        (skill_dir / "SKILL.md").write_text(skill_content)
        print("[OK] Created SKILL.md")
    except Exception as e:
        print(f"[ERROR] Error creating SKILL.md: {e}")
        return None

    # Create resource directories if requested
    if resources:
        create_resource_dirs(skill_dir, skill_name, skill_title, resources, include_examples)

    print(f"\n[OK] Skill '{skill_name}' initialized successfully.")
    return skill_dir

def main():
    parser = argparse.ArgumentParser(description="Create a new skill directory.")
    parser.add_argument("skill_name", help="Skill name")
    parser.add_argument("--path", required=True, help="Output directory")
    parser.add_argument("--resources", default="", help="Comma-separated: scripts,references,assets")
    parser.add_argument("--examples", action="store_true", help="Create example files")
    args = parser.parse_args()

    skill_name = normalize_skill_name(args.skill_name)
    resources = parse_resources(args.resources)
    
    init_skill(skill_name, args.path, resources, args.examples)

if __name__ == "__main__":
    main()
