# GitHub Copilot Masterclass

This repository contains materials, notes, and custom agent configurations from the **GitHub Copilot for QA Masterclass**.

## 📚 Contents

### Agent & Skill Configuration
- **`.github/AGENTS.md`** — Agent instructions file with workspace conventions, structure, and key information for AI coding agents.
- **`.github/agents/`** — Custom VS Code agent definitions (e.g., `reverse-string.agent.md`).
- **`.github/skills/`** — Custom skill definitions (folder-based SKILL.md format).

### Python Examples
- **`.github/Sourcecode/`** — Python example programs:
  - `Hello.py` — Simple Hello World program.
  - `findlargest.py` — Program to find the largest of two numbers.

### Notes & Reference Guides
- **`Notes/ClassNotes.md`** — Comprehensive raw class notes covering GitHub Copilot concepts, installation, commands, skills, STLC, MCP servers, AI agents, and comparisons between prompts, skills, and AI agents.
- **`Notes/ClassNotesEraser.md`** — Formatted/exported version of class notes (Eraser.io export).
- **`Notes/agentsmdvsCopilotinstruction.md`** — Detailed comparison between `AGENTS.md` and `copilot-instructions.md`, including naming conventions, ecosystem support, discovery behavior, and portability.
- **`Notes/caveman-UserGuide.md`** — Comprehensive guide for the Caveman Skill Suite (token optimization), covering installation, modes, all 20+ skills, and real-world token savings.

## 🚀 Topics Covered

- GitHub Copilot overview and installation
- Copilot concepts and commands
- Creating custom Skills and Agents
- STLC (Software Testing Life Cycle) with Copilot
- JIRA MCP, Playwright MCP, CLI, and AI Agents
- Hands-on class labs and MCQ practice
- Prompt vs Skill vs AI Agent distinctions
- Caveman Skill Suite for token optimization

## 🤖 Custom Agents

| Agent | Description |
|-------|-------------|
| `reverse-string` | Reverses any given string input and returns the reversed result. |

## 🛠️ Custom Skills

| Skill | Description |
|-------|-------------|
| `reverse-string` | Reverses any given string input (folder-based SKILL.md format). |

## 🔧 Usage

This workspace is set up for learning and experimenting with GitHub Copilot's agent customization capabilities. Explore the agent definition files under `.github/agents/` and skill definitions under `.github/skills/` to understand how custom agents and skills are configured.

### Quick Links
- [Agent Instructions](.github/AGENTS.md) — Workspace conventions for AI coding agents
- [Class Notes](Notes/ClassNotes.md) — Full masterclass notes
- [Caveman User Guide](Notes/caveman-UserGuide.md) — Token optimization guide
- [AGENTS.md vs copilot-instructions.md](Notes/agentsmdvsCopilotinstruction.md) — Comparison guide
