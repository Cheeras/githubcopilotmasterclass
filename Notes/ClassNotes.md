GitHub Copilot for QA Master class

Agenda

Overview

Installation

Concepts and Commands

How to create Skills

STLC

JIRA MCP,Playwright MCP, CLI and AI Agents

Class lab

MCQ practice

don't confuse with copilot.microsoft.com it is very similar to chatGPT, it is not coding assistant

Class link:

[app.thetestingacademy.com/masterclass/copilot](https://app.thetestingacademy.com/masterclass/copilot)

[app.eraser.io/workspace/MavvCD3msYWU33Fp3PN4](https://app.eraser.io/workspace/MavvCD3msYWU33Fp3PN4)

git copilot is AI pair programmer

git copilot is AI coding agent, claude haiku as free model

Donot buy the microsoft copilot

---

you can barrow model from [openrouter.ai - this is website we cab LLM on rent ](https://openrouter.ai/deepseek/deepseek-v4-pro#providers)basis

why we want to use openrouter because we need cheaper models

if you Claude Opus 4.8 my 10$ will complete in 10 mins maximum 10 prompts

Deepseek v4 is amazing

we have free model nemotron is free which is very very slow

======================================

Rich - Github copilot - sonnet 4.6 or above model

Medium Rich - 10$ - Openrouter.ai( add 10% to tha account) - Deepseek V4 Pro

Less Rich - $0 - Openrouter - nemotron -free ( it will be very slow)

==========================================

you can access Git Hub Copilot using the

VS Code GHCP

Github copilot CLI

what is advantage of github copilot CLI ::

     1. The Advantage of github copilot CLI is it will save the token

     2. we can start multiple session using github copilot CLI

tabby.sh for windows

iterm2.com for mac user to connect to mulitple copilot CLI connections

first command in CLI

/models

cli give you more power

be comfirtable with CLI

3 ways to access to Github copilot - Plan mode recommended - Save your token

Donot give power of thinging to LLM, if you don't understand what you are doing

	1. Plan - only research

	2. Ask - if you have source you can ask question about explain the logic of code

        3. Agent - can change and modify the code in code editor

LLM - Brain

AI Agent - Brain + Tool + Memory

An automouse system that perceices,reason,decides and act towards a goal

Skill - Memory (no memory) it can access tools

A skill is Packaged set of instructions, Knowledge, or procedure (ex: skill.md  file with steps + Scripts)

different commands in GHCP:

========================

/compact - compress the all previouse conversation when context window is about to full

let me explain what is compact before that every model has context for example DeepSeek V4 Pro has contex of 1M token - that means it can remember the 1M worth of details what happen when 1M million is finished we have to compact or compress

Lets say example if you have attended any online session for 10 hours you will get exhausted is't it . in the same way LLM also has Limited context window , what will happen when the context window is full, it is will compact the all tha data/coversation saves as summary and this summary will pass on to the next user prompt that is provided by the User

/clear - it will start new chat and archieve the current one

/explain - Explain how the code in your active editor works

/fix - Propose a fix for the problems in the selected code

======================================================

Now i want to save the token how can i save the token usage you can install the caveman in this case

first plug - every one has to install is caveman

[github.com/juliusbrussee/caveman/blob/main/README.md](https://github.com/juliusbrussee/caveman/blob/main/README.md)

Caveman - Skill plugin - it will save the lot of tokens

Copilot-instruction.md file: it contains information about the project or folder that you are working  on it is basically contains information

what is objective

how the folder structure looks like

how to run your source code

which directory contains what

All the necessary information which is important for the AI coding agent co-polit run the project, to execute the project to test the project or for documentation


/init - what exectly init command do
