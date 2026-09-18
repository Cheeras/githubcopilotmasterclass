---
name: reverse-string
description: 'Reverse any given string input. Use when the user asks to reverse a word, name, sentence, or any text string — e.g., "reverse hello", "reverse Shankar", "reverse this string".'
argument-hint: 'A string to reverse, e.g., "hello" or "Shankar"'
user-invocable: true
---

# Reverse String Skill

## When to Use
- User asks to reverse a word, name, or text string
- User says "reverse this string", "reverse &lt;text&gt;", or "turn &lt;text&gt; around"
- User provides a string and expects the reversed version as output

## Core Behavior
- Accepts a single string input from the user.
- Reverses the character order of the input string.
- Returns only the reversed string as output (no extra commentary unless needed).

## Constraints
- Input must be a plain text string. Non-string inputs (numbers, objects, etc.) should be converted to string first.
- Preserves the original casing — only the order of characters changes.
- Spaces, punctuation, and special characters are treated as regular characters and reversed along with letters.

## Procedure
1. Receive the input string from the user.
2. Convert the input to a string if it isn't already.
3. Reverse the string by iterating from the last character to the first.
4. Return the reversed string as the final output.

## Examples
| Input | Output |
|-------|--------|
| `"hello"` | `"olleh"` |
| `"Shankar"` | `"raknahS"` |
| `"12345"` | `"54321"` |
| `"Jeyadev"` | `"vedayeJ"` |
| `"Hello World"` | `"dlroW olleH"` |