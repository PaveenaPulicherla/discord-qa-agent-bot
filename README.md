
# MIT Assignment – Discord QA Agent Bot

This bot simulates an AI QA & Governance agent using simple commands.
It demonstrates test generation, hallucination detection, compliance checks,
and QA reporting inside a Discord server.

## Commands
- !hello
- !testcases <prompt>
- !hallucination <text>
- !compliance <text>
- !qareport

## Setup
1. Install Python 3.10+
2. pip install discord.py
3. Add your bot token to bot.py
4. Run: python bot.py
# Discord QA Agent Bot

This repository contains a lightweight Discord bot designed as part of an MIT assignment to demonstrate agentic AI concepts such as test case generation, hallucination detection, compliance evaluation, and QA reporting.

The bot simulates the behavior of an internal AI QA & Governance agent using simple command-based interactions inside a Discord server.

---

## Features

- **!hello** – Basic greeting  
- **!testcases <prompt>** – Generates structured test cases  
- **!hallucination <text>** – Evaluates hallucination risk  
- **!compliance <text>** – Checks for PII/policy issues  
- **!qareport** – Produces a summary QA report  

---

## Installation

1. Install Python 3.10+
2. Clone this repository:
git clone https://github.com/PaveenaPulicherla/discord-qa-agent-bot.git
3. Install dependencies:
pip install -r requirements.txt
4. Add your Discord bot token to `bot.py`
5. Run the bot:
python bot.py

---

## Repository Structure

discord-qa-agent-bot/
│
├── README.md
├── bot.py
├── requirements.txt
│
├── docs/
│   ├── assignment-writeup.md
│   ├── architecture-diagram.md
│   ├── reflection.md
│   
│
├── src/
│   ├── commands/
│   │   ├── testcases.py
│   │   ├── hallucination.py
│   │   ├── compliance.py
│   │   └── qareport.py
│   
│
└── .gitignore



---

## License

This project is for educational use as part of MIT’s Applied Agentic AI module.
