# AGENTS.md vs copilot-instructions.md — Detailed Comparison

## 📋 Overview

Both `AGENTS.md` and `copilot-instructions.md` are **agent instruction files** that provide always-on context to AI coding agents. They tell the agent about project structure, conventions, build commands, architecture, and other essential knowledge needed to be productive in the codebase.

However, they differ in **naming convention, ecosystem support, discovery behavior, and portability**.

---

## 🆚 Side-by-Side Comparison

| Aspect | `AGENTS.md` | `copilot-instructions.md` |
|--------|------------|---------------------------|
| **Full Name** | AGENTS.md | copilot-instructions.md |
| **Location** | `.github/AGENTS.md` or root `AGENTS.md` | `.github/copilot-instructions.md` |
| **Ecosystem** | Cross-platform standard (30+ AI agents) | GitHub Copilot specific |
| **Primary Purpose** | Provide project context to any AI coding agent | Provide project context specifically to GitHub Copilot |
| **Discovery** | Auto-detected by many AI tools by filename | Auto-detected only by GitHub Copilot |
| **Portability** | ✅ Works across Claude Code, Codex, Gemini, Cursor, Windsurf, Cline, Copilot, etc. | ❌ Works only with GitHub Copilot |
| **Origin** | Community-driven standard (popularized by Claude Code / Anthropic) | GitHub / VS Code official standard |
| **Recognition** | Recognized by name in many agent configs | Recognized only by GitHub Copilot's VS Code extension |
| **Fallback behavior** | Some agents check multiple locations (root, `.github/`, etc.) | Copilot checks `.github/copilot-instructions.md` specifically |
| **File format** | Plain Markdown (no frontmatter needed) | Plain Markdown (no frontmatter needed) |
| **When to use** | Multi-tool workflows, future-proofing | Copilot-only projects |

---

## 🎯 Core Purpose

### AGENTS.md
- **Purpose**: Provide project-level instructions to **any AI coding agent** that supports it
- **Philosophy**: "Write once, use everywhere" — one file that works across Claude Code, Codex CLI, Gemini CLI, Cursor, Windsurf, Cline, GitHub Copilot, and 25+ other agents
- **Best for**: Teams using multiple AI coding tools, or wanting future-proof instructions

### copilot-instructions.md
- **Purpose**: Provide project-level instructions specifically to **GitHub Copilot** in VS Code
- **Philosophy**: "Copilot-native" — follows GitHub's official convention for Copilot customization
- **Best for**: Teams that only use GitHub Copilot and want the official supported path

---

## 🔍 How Each Agent Discovers These Files

| AI Agent | Looks for `AGENTS.md`? | Looks for `copilot-instructions.md`? |
|----------|----------------------|-------------------------------------|
| **GitHub Copilot** | ✅ `.github/AGENTS.md` | ✅ `.github/copilot-instructions.md` |
| **Claude Code** | ✅ Root `AGENTS.md` or `CLAUDE.md` | ❌ No |
| **OpenAI Codex CLI** | ✅ Root `AGENTS.md` | ❌ No |
| **Gemini CLI** | ✅ Root `AGENTS.md` or `GEMINI.md` | ❌ No |
| **Cursor** | ✅ `.cursorrules` or root `AGENTS.md` | ❌ No |
| **Windsurf** | ✅ `.windsurfrules` or root `AGENTS.md` | ❌ No |
| **Cline** | ✅ `.clinerules/` or root `AGENTS.md` | ❌ No |
| **Aider** | ✅ Root `AGENTS.md` or `CONVENTIONS.md` | ❌ No |

---

## 📁 Location Rules

### AGENTS.md
```
# Preferred locations (checked in order by most agents):
./AGENTS.md                          # Root level
.github/AGENTS.md                    # .github folder (Copilot reads this)

# Also commonly checked:
CLAUDE.md                            # Claude Code primary
GEMINI.md                            # Gemini CLI primary
.cursorrules                         # Cursor primary
.windsurfrules                       # Windsurf primary
.clinerules/                         # Cline folder-based
```

### copilot-instructions.md
```
# Only location checked by GitHub Copilot:
.github/copilot-instructions.md      # Must be exactly this path
```

---

## 📝 Content Comparison

Both files contain similar types of information:

| Content Type | AGENTS.md | copilot-instructions.md |
|-------------|-----------|------------------------|
| Project overview & purpose | ✅ | ✅ |
| Folder structure | ✅ | ✅ |
| Build/test commands | ✅ | ✅ |
| Coding conventions | ✅ | ✅ |
| Architecture decisions | ✅ | ✅ |
| Environment setup | ✅ | ✅ |
| Common pitfalls | ✅ | ✅ |
| Key file locations | ✅ | ✅ |

The **content is identical** in nature — only the **file name and discovery mechanism** differ.

---

## ⚖️ Pros and Cons

### AGENTS.md

| ✅ Pros | ❌ Cons |
|---------|---------|
| Works across 30+ AI agents | Less official / standardized naming |
| Future-proof — switch tools without rewriting instructions | Some agents may not auto-detect it from `.github/` folder |
| Community standard — widely recognized | May need symlinks or copies for full cross-agent support |
| Single file to maintain | |

### copilot-instructions.md

| ✅ Pros | ❌ Cons |
|---------|---------|
| Official GitHub Copilot standard | Only works with GitHub Copilot |
| Guaranteed to be auto-detected by Copilot | If you switch to Claude Code/Codex, instructions won't be picked up |
| Clear naming — obvious purpose | Need separate files for other agents |

---

## 🏆 Recommendation

| Scenario | Use |
|----------|-----|
| **Only use GitHub Copilot** | `copilot-instructions.md` (official path) |
| **Use multiple AI agents** | `AGENTS.md` (cross-platform) |
| **Want maximum compatibility** | **Both** — create `AGENTS.md` for cross-agent use AND `copilot-instructions.md` for Copilot-specific instructions |
| **Future-proofing** | `AGENTS.md` — works today with Copilot, works tomorrow with any agent |

---

## 🔗 Real-World Example: This Workspace

This workspace uses `.github/AGENTS.md` because:

1. **GitHub Copilot reads it** from `.github/AGENTS.md` natively
2. **Caveman skills** are installed globally and work across agents
3. **Future-proof** — if you later use Claude Code or Codex CLI, the same instructions apply
4. **Single file to maintain** — no duplication

---

## 📌 Key Takeaway

> **Same purpose, different audience.**
>
> - `AGENTS.md` = "Instructions for any AI agent"
> - `copilot-instructions.md` = "Instructions for GitHub Copilot specifically"
>
> Both tell the AI how to understand and work with your project. Choose based on which tools you use — or use both for maximum compatibility.