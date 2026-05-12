# Skill Authoring Best Practices

Learn how to write effective Agent Skills that can be discovered and used successfully.

---

Good Skills are concise, well-structured, and tested with real usage. This guide provides practical authoring decisions to help you write Skills that an Agent can discover and use effectively.

## Core Principles

### Concise is Key
The context window is a limited resource. Your Skill shares the context window with the system prompt, conversation history, and other Skills.
- Keep `SKILL.md` focused and brief.
- Use `references/` for detailed documentation that doesn't need to be in the prompt by default.
- Minimize redundant information across metadata and instructions.

### Actionable Names
Skill names should clearly imply what they do.
- Use verb-noun pairs: `create-user`, `list-files`, `validate-input`.
- Avoid vague names like `manager`, `tool`, or `helper`.

### Clear Descriptions
The description in the metadata is the primary way an Agent decides to use your Skill.
- Start with a clear verb.
- Describe the primary outcome.
- Be specific about what the Skill *cannot* do if there's potential for confusion.

## Structural Best Practices

### The SKILL.md File
This is the heart of your Skill. It should contain:
- **Purpose**: A high-level overview.
- **Usage Patterns**: Examples of how to trigger and use the Skill.
- **Constraints**: Critical "do"s and "don't"s.

### Using References
Detailed documentation, API specs, or complex examples should reside in the `references/` directory.
- Use `references/*.md` for context that is only needed when performing specific, complex tasks.
- Mention these references in `SKILL.md` so the Agent knows to read them when necessary.

### Scripts and Tools
- Keep scripts modular and focused.
- Ensure all scripts have clear help messages and follow consistent exit code conventions.
- Use `requirements.txt` or similar for dependency management if applicable.

## Optimization Strategies

### Prompt Engineering for Skills
- Use clear, imperative language in the `SKILL.md`.
- Provide concrete examples for complex logic.
- Use standard Markdown formatting (headers, lists, code blocks).

### Testing and Validation
- Regularly validate your Skill's metadata and structure.
- Test the Skill with various edge cases to ensure reliability.
- Monitor execution logs to identify common failure patterns.
