# 🪨 Caveman Skill Suite — User Guide for GitHub Copilot

> **"Why use many token when few do trick"**
>
> Caveman is a skill plugin by [Julius Brussee](https://github.com/JuliusBrussee/caveman) that makes your AI agent talk like a caveman — cutting filler, articles, pleasantries, and hedging — while keeping **all technical substance intact**. It saves tokens on every response, which means lower costs and longer usable context windows.

---

## 📋 Table of Contents

1. [What is Caveman?](#-what-is-caveman)
2. [How Tokens Are Saved](#-how-tokens-are-saved)
3. [Installation](#-installation)
4. [Caveman Modes (Intensity Levels)](#-caveman-modes-intensity-levels)
5. [All Caveman Skills Reference](#-all-caveman-skills-reference)
6. [Real-World Examples & Token Savings](#-real-world-examples--token-savings)
7. [When to Use / When to Skip](#-when-to-use--when-to-skip)
8. [Tips & Best Practices](#-tips--best-practices)

---

## 🗿 What is Caveman?

Caveman is a **communication compression skill** for AI coding agents. It installs a set of rules that tell the agent to:

- **Drop** filler words (just, really, basically, actually, simply)
- **Drop** articles (a, an, the) where safe
- **Drop** pleasantries (sure, certainly, of course, happy to)
- **Drop** hedging (it might be worth, you could consider)
- **Use** short synonyms (fix not "implement a solution for")
- **Skip** tool-call narration, decorative tables/emoji
- **Keep** ALL technical content: code, commands, error messages, file paths, API names, numbers, units — exactly as-is

### What Caveman NEVER does:
- ❌ Shorten your code
- ❌ Paraphrase error messages
- ❌ Grunt through security warnings (auto-switches to full sentences for dangerous ops)
- ❌ Change your prompts — only the agent's replies are compressed

---

## 💰 How Tokens Are Saved

### The Token Math

A token ≈ ¾ of a word in English. AI providers bill by the token — both **input** (what you send) and **output** (what the agent writes).

Caveman attacks **output tokens** (what the agent says back to you).

### Real Token Comparison

| Scenario | Normal Agent | Caveman Agent | Savings |
|----------|-------------|---------------|---------|
| "Why React re-render?" | 69 tokens | 19 tokens | **72% fewer** |
| Explain DB connection pooling | 85 tokens | 32 tokens | **62% fewer** |
| Code review comment | 120 tokens | 28 tokens | **77% fewer** |
| Commit message | 55 tokens | 18 tokens | **67% fewer** |

### How Savings Add Up

- **Per response**: 50-75% fewer output tokens
- **Per session**: If you have 50 exchanges, saving ~50 tokens each = **2,500+ tokens saved per session**
- **Per day**: Multiple sessions = **10,000+ tokens saved daily**
- **Per month**: At API pricing (~$3/M input tokens, $15/M output tokens), this translates to **real money saved**

### The Hidden Win: Context Window

Every token the agent writes stays in the conversation context. By writing less, Caveman **frees up context window space** for more useful content — code, error details, file contents. This means you can have **longer, more productive sessions** before hitting context limits.

---

## ⚡ Installation

Caveman is already installed in this workspace. To install it elsewhere:

```bash
npx skills add JuliusBrussee/caveman -g
```

This installs **20 skills** under `~\.agents\skills\` for GitHub Copilot, Codex, Command Code, and 12+ other agents.

---

## 🎚️ Caveman Modes (Intensity Levels)

Caveman has 6 intensity levels. You switch between them mid-conversation:

| Mode | Trigger | What Changes | Example: "Why React re-render?" |
|------|---------|-------------|-------------------------------|
| **Lite** | `/caveman lite` | Drop filler/hedging. Keep articles + full sentences. Professional but tight. | "Your component re-renders because you create a new object reference each render. Wrap it in `useMemo`." |
| **Full** (default) | `/caveman` or `/caveman full` | Drop articles, fragments OK, short synonyms. No tool-call narration. | "New object ref each render. Inline object prop = new ref = re-render. Wrap in `useMemo`." |
| **Ultra** | `/caveman ultra` | Strip conjunctions. One word when one word enough. State each fact once. | "Inline obj prop, new ref, re-render. `useMemo`." |
| **Wenyan-Lite** | `/caveman wenyan-lite` | Semi-classical Chinese. Drop filler, keep grammar structure. | "組件頻重繪，以每繪新生對象參照故。以 useMemo 包之。" |
| **Wenyan-Full** | `/caveman wenyan` | Full 文言文. Maximum classical terseness. | "每繪新生對象參照，故重繪；以 useMemo 包之則免。" |
| **Wenyan-Ultra** | `/caveman wenyan-ultra` | Extreme classical abbreviation. | "新參照則重繪。useMemo 包之。" |
| **Off** | `stop caveman` or `normal mode` | Revert to normal prose. | Normal English. |

> **Default mode is `full`.** Mode persists for the entire session until changed.

---

## 🧰 All Caveman Skills Reference

### 1. 🗣️ **caveman** (Main Skill)
- **Trigger**: `/caveman` or "caveman mode" or "talk like caveman"
- **What it does**: Makes ALL agent responses ultra-compressed. Drops filler, articles, pleasantries, hedging. Keeps technical content exact.
- **Token saving**: 50-75% fewer output tokens per response

### 2. 📝 **caveman-commit**
- **Trigger**: `/caveman-commit` or "write a commit" or `/commit`
- **What it does**: Writes Conventional Commits messages compressed to intent only. Format: `<type>(<scope>): <imperative summary>`.
- **Token saving**: ~67% fewer tokens in commit messages
- **Example**:
  - ❌ Normal: "feat: add a new endpoint to get user profile information from the database"
  - ✅ Caveman: `feat(api): add GET /users/:id/profile`

### 3. 👁️ **caveman-review**
- **Trigger**: `/caveman-review` or "review this PR" or "review the diff"
- **What it does**: One-line code review comments. Format: `L<line>: <problem>. <fix>.`
- **Token saving**: ~77% fewer tokens per review comment
- **Example**:
  - ❌ Normal: "I noticed that on line 42 you're not checking if the user object is null before accessing the email property. This could potentially cause a crash..."
  - ✅ Caveman: `L42: 🔴 bug: user can be null after .find(). Add guard before .email.`

### 4. 📦 **caveman-compress**
- **Trigger**: `/caveman-compress <filepath>`
- **What it does**: Compresses memory files (CLAUDE.md, todos, preferences) into caveman format. Saves ~46% input tokens. Original backed up automatically.
- **Token saving**: ~46% fewer input tokens from compressed files
- **Example**:
  - Original: "You should always make sure to run the test suite before pushing any changes to the main branch. This is important because it helps catch bugs early..."
  - Compressed: "Run tests before push to main. Catch bugs early, prevent broken prod deploys."

### 5. 🔍 **caveman-explore**
- **Trigger**: Delegated by the agent when it needs to find code
- **What it does**: Fast, read-only code explorer. Returns compact `path:line` citations. Uses Haiku model (cheaper).
- **Token saving**: Subagent output is ~⅓ the size of vanilla Explore — saves ~1,300 tokens per delegation

### 6. 📊 **caveman-stats**
- **Trigger**: `/caveman-stats`
- **What it does**: Shows recorded output and cache-read token usage for the current session.
- **Token saving**: Visibility tool — helps you understand where tokens go

### 7. ❓ **caveman-help**
- **Trigger**: `/caveman-help` or "caveman help"
- **What it does**: Quick-reference card for all caveman modes, skills, and commands.

### 8. 🧠 **caveman-learn**
- **Trigger**: When asked to lower token costs or analyze token usage
- **What it does**: Reads caveman learn reports and applies consent-gated fixes to reduce token consumption.
- **Key feature**: Identifies "token sinks" — heavy CLAUDE.md files, recurring context blocks, repeated procedures — and offers fixes.

### 9. 👥 **cavecrew** (Subagent Delegation)
- **Trigger**: Agent delegates to `cavecrew-investigator`, `cavecrew-builder`, or `cavecrew-reviewer`
- **What it does**: Three subagent presets that emit caveman-compressed output instead of verbose prose.
- **Token saving**: Subagent output is ~⅓ the size of vanilla agents

| Subagent | Task | Output Format |
|----------|------|--------------|
| `cavecrew-investigator` | Find where code lives | `path:line — symbol — short note` |
| `cavecrew-builder` | Surgical 1-2 file edits | `path:line-range — change ≤10 words` |
| `cavecrew-reviewer` | Review diff for bugs | `path:line: 🔴 bug: problem. fix.` |

### 10. 🛠️ Other Utility Skills

| Skill | Purpose |
|-------|---------|
| **caveman-discover** | Find & label every LLM workflow in the repo |
| **caveman-evidence-review** | Read-only review of Caveman Cloud cost data |
| **caveman-manage** | Inspect Caveman Cloud experiment lifecycle |
| **caveman-optimize** | Turn optimization observations into candidates |
| **caveman-setup** | Wire repo through Caveman Cloud gateway |
| **investigate-first** | Diagnose failures before editing |
| **lean-build** | Build feature work with scope control |
| **migration** | Implement reversible compatibility-safe transitions |
| **safe-refactor** | Restructure code while preserving behavior |
| **surgical-patch** | Fix bugs at narrowest responsible layer |
| **verify-and-stop** | Prove work meets acceptance conditions |

---

## 🎯 Real-World Examples & Token Savings

### Example 1: Debugging a React Bug

**Your prompt**: "Why is my component re-rendering infinitely?"

**Normal agent response** (69 tokens):
> "Sure! I'd be happy to help you with that. The issue you're experiencing is likely caused by an inline object or function reference being created on every render. When you pass an inline object as a prop, it creates a new reference each time, which triggers a re-render in the child component. You can fix this by wrapping your object in useMemo or by defining it outside the component."

**Caveman agent response** (19 tokens):
> "New object ref each render. Inline object prop = new ref = re-render. Wrap in `useMemo`."

**Savings: 50 tokens (72% fewer)**

### Example 2: Code Review

**Your prompt**: "Review this PR diff"

**Normal agent** (120 tokens):
> "I noticed that on line 42 you're not checking if the user object is null before accessing the email property. This could potentially cause a crash if the user is not found in the database. You might want to add a null check here."

**Caveman agent** (28 tokens):
> "L42: 🔴 bug: user can be null after .find(). Add guard before .email."

**Savings: 92 tokens (77% fewer)**

### Example 3: Commit Message

**Normal commit message** (55 tokens):
> "feat: add a new endpoint to get user profile information from the database so that the mobile client can display user profiles without needing to load the full user payload"

**Caveman commit** (18 tokens):
```
feat(api): add GET /users/:id/profile

Mobile client needs profile data without full user payload.
Closes #128
```

**Savings: 37 tokens (67% fewer)**

### Example 4: Explaining Database Connection Pooling

**Normal agent** (85 tokens):
> "Connection pooling is a technique that reuses open database connections instead of creating new ones for each request. This avoids the repeated handshake overhead that comes with establishing a new connection every time. It's a common practice in production applications to improve performance."

**Caveman agent** (32 tokens):
> "Pool reuse open DB connections. No new connection per request. Skip handshake overhead."

**Savings: 53 tokens (62% fewer)**

### Example 5: Full Session Simulation

A typical 30-minute coding session with 40 exchanges:

| Metric | Normal Agent | Caveman Agent |
|--------|-------------|---------------|
| Avg tokens per response | 80 | 28 |
| Total output tokens (40 exchanges) | 3,200 | 1,120 |
| Input tokens (prompts + context) | ~15,000 | ~15,000 |
| **Total session tokens** | **18,200** | **16,120** |
| **Token savings** | — | **2,080 (11.4%)** |
| At $15/M output tokens | $0.048 | $0.017 |
| At $3/M input tokens | $0.045 | $0.045 |
| **Total cost** | **$0.093** | **$0.062** |

> **Note**: On GitHub Copilot (premium requests model), shorter answers save the same request count — the savings are in **context window space**, not direct billing. On API-based agents (Claude Code, Codex CLI), the savings are **directly monetary**.

---

## 🧭 When to Use / When to Skip

### ✅ Good fit for Caveman:
- **Long coding sessions** where context window fills up — caveman keeps more room for code
- **Debugging sessions** — you want the fix, not the explanation
- **Code review** — one-line findings are faster to scan
- **Commit messages** — conventional commits are already terse
- **API-based agents** (Claude Code, Codex CLI) — you pay per token
- **Reading agent answers** more than pasting them elsewhere

### ❌ Skip Caveman when:
- **GitHub Copilot premium requests** — billed per request, not per token (same cost either way)
- **Writing documentation** — output goes to humans who need full sentences
- **Pair programming with non-technical stakeholders** — they need the prose
- **Security-critical code** — caveman auto-expands for security warnings anyway
- **Teaching/learning scenarios** — you want the explanations

---

## 💡 Tips & Best Practices

### 1. **Start with `/caveman lite`** if you're new
Lite mode keeps full sentences while dropping filler. It's the gentlest introduction.

### 2. **Use `/caveman ultra` for debugging**
When you're deep in a bug hunt, you don't need pleasantries — you need the fix. Ultra mode gives maximum compression.

### 3. **Combine with `/caveman-compress` for memory files**
Compress your `copilot-instructions.md` or `AGENTS.md` files to save input tokens on every session start.

### 4. **Use `/caveman-commit` before git commits**
Saves tokens and produces cleaner, more professional commit messages.

### 5. **Use `/caveman-review` before PR submissions**
Get a quick bug check without spending tokens on verbose commentary.

### 6. **Say "stop caveman" for human-facing output**
When writing docs, emails, or comments, switch back to normal mode so the output is readable by others.

### 7. **Caveman is sticky per session**
Once activated, it stays on until you say "stop caveman" or "normal mode". You don't need to re-activate it.

### 8. **The proxy (big rock) saves even more**
Beyond the skill (which compresses what the agent *says*), the Caveman proxy compresses what the agent *reads* — logs, test output, JSON, diffs. Install with:
```bash
npm install -g @caveman-ai/cli && caveman setup --install
```

---

## 🔢 Quick Command Reference

| What to Say | What Happens |
|-------------|-------------|
| `/caveman` | Activate full caveman mode (default) |
| `/caveman lite` | Lite mode — tight but polite |
| `/caveman ultra` | Ultra mode — maximum compression |
| `/caveman wenyan` | Classical Chinese mode |
| `/caveman off` | Deactivate caveman |
| `stop caveman` | Deactivate caveman |
| `normal mode` | Deactivate caveman |
| `/caveman-commit` | Write a compressed commit message |
| `/caveman-review` | Compressed code review |
| `/caveman-compress <file>` | Compress a memory file |
| `/caveman-help` | Show this reference card |
| `/caveman-stats` | Show token usage stats |

---

## 📚 Learn More

- **GitHub Repo**: [github.com/JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)
- **Install Guide**: [INSTALL.md](https://github.com/JuliusBrussee/caveman/blob/main/INSTALL.md)
- **Honest Numbers**: [docs/HONEST-NUMBERS.md](https://github.com/JuliusBrussee/caveman/blob/main/docs/HONEST-NUMBERS.md)
- **Research**: Cited in Adobe Research paper [CAVEWOMAN (arXiv 2606.24083)](https://arxiv.org/abs/2606.24083)
- **Tested by**: JetBrains on 86 real coding tasks — "costs you nothing measurable in quality"

---

> **Bottom line**: Caveman save token. Token save money. Money buy more mammoth. 🪨