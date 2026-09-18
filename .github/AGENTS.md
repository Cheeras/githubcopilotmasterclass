# GitHub Copilot Masterclass — Agent Instructions

## Project Overview

This is a **learning/educational workspace** for the **GitHub Copilot for QA Masterclass**. It contains class notes, reference materials, and custom agent/skill configurations. There is **no source code** to build, run, or test.

## Workspace Structure

```
.github/
├── agents/              # Custom VS Code agent definitions (*.agent.md)
│   └── reverse-string.agent.md
└── skills/              # Custom skill definitions (folder-based SKILL.md)
    └── reverse-string/
        └── SKILL.md
Notes/                   # Class notes and reference guides
├── caveman-UserGuide.md # Caveman skill suite usage guide
├── ClassNotes.md        # Raw class notes
└── ClassNotesEraser.md  # Formatted class notes (Eraser.io export)
README.md                # Project overview
```

## Key Conventions

### Agent Definition Format
- **Location**: `.github/agents/<name>.agent.md`
- **Format**: YAML frontmatter (`name`, `description`, `argument-hint`, optional `tools`) + Markdown behavioral instructions
- **Usage**: Agents are invoked by name and can have restricted tool sets

### Skill Definition Format
- **Location**: `.github/skills/<name>/SKILL.md`
- **Format**: YAML frontmatter (`name`, `description`, `argument-hint`, `user-invocable`) + Markdown instructions
- **Folder skills** (AgentSkill.io format) can include `scripts/`, `references/`, `assets/`, `templates/` subfolders
- Skills marked `user-invocable: true` can be triggered directly by users

### Caveman Skill Suite (Installed Globally)
- **Location**: `~\.agents\skills\caveman\` (20 skills installed)
- **Purpose**: Ultra-compressed communication mode — drops filler words, articles, pleasantries, hedging while keeping all technical content exact
- **Activation**: Say `/caveman` in chat to activate caveman mode
- **Modes**: `/caveman lite|full|ultra|wenyan-lite|wenyan-full|wenyan-ultra|off`
- **Token savings**: 50-77% fewer output tokens per response
- **Related skills**: `caveman-commit`, `caveman-review`, `caveman-compress`, `caveman-explore`, `caveman-stats`, `caveman-help`, `caveman-learn`, `cavecrew` (investigator/builder/reviewer subagents)
- **Reference**: See `Notes/caveman-UserGuide.md` for full usage details

## Commands

| Command | Description |
|---------|-------------|
| `/explain` | Explain how code in the active editor works |
| `/fix` | Propose a fix for problems in selected code |
| `/clear` | Start a new chat session |
| `/compact` | Compress conversation history |
| `/init` | Create or update chat customization files |

## Important Notes for AI Agents

1. **No build/test commands exist** — this is a documentation-only workspace
2. **All files are Markdown** — no source code, no config files, no package.json
3. **Caveman is installed globally** — prefer using caveman-compressed responses to save tokens
4. **Existing customizations** are under `.github/agents/` and `.github/skills/`
5. **New customizations** should follow the existing patterns (YAML frontmatter + Markdown body)
6. **Class notes** in `Notes/` contain masterclass learnings — reference them when answering questions about Copilot concepts