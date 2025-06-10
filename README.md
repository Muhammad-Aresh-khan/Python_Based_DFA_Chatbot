
# 🤖 Advanced DFA Chatbot System

A Python-based smart chatbot system that uses **Deterministic Finite Automata (DFA)** for pattern matching, with support for **fuzzy logic**, **learning new patterns**, and **conversation analytics**.

## 📚 Table of Contents

* Features
* TOA Concept
* Tech Stack
* How It Works
* Settings & Personalization
* Usage
* Commands
* Exported Files
* Demo

---

## 🚀 Features

* ✅ DFA-based pattern matching with trace visualization
* ✅ Fuzzy string matching (typo-tolerant)
* ✅ Learns new patterns from user input
* ✅ Real-time response generation
* ✅ Custom settings (e.g., auto-save, response delay)
* ✅ Imports and exports patterns and conversations

---

## 🔄 TOA Concept

This chatbot uses **Deterministic Finite Automata (DFA)** to match user input with defined patterns. Here's how:

* Each pattern is stored as DFA states and transitions
* Each character from user input is processed step-by-step
* If final state is reached, the input is accepted as a match

### 🧠 DFA in Python:

```python
{
  'start': {'h': 'q1'},
  'q1': {'e': 'q2'},
  'q2': {'l': 'q3'},
  'q3': {'l': 'q4'},
  'q4': {'o': 'final'}
}
```

Patterns are stored using **nested dictionaries**, making the system scalable and flexible.

---

## 🛠️ Tech Stack

* **Language**: Python 3
* **Libraries**:

  * `json` – Load/store DFA states and custom patterns
  * `time`, `datetime` – Response delay and timestamp logging
  * `random` – Random response variation
  * `os` – File path and system handling
  * `difflib (SequenceMatcher)` – Fuzzy matching
* **UI**: CLI-based interface
* **File Handling**:

  * `.json` – For storing DFA transitions and learned patterns
  * `.txt` – For exporting conversation history

---

## 🧠 How It Works

1. User inputs a message.
2. The bot tries to match it using DFA-based transitions.
3. If no exact match is found, fuzzy matching is applied.
4. The bot replies with a corresponding response.
5. If learning mode is enabled, it will ask for a response to store.

---

## ⚙️ Settings & Personalization

You can configure runtime settings by using the `settings` command.

### Default Settings:

```
• show_traces: True
• fuzzy_matching: True
• learning_mode: True
• auto_save: True
• response_delay: 0.5
```

Change them easily in the terminal by entering the setting name and a new value.

---

## 💻 Usage

### ▶️ Run the Bot

```bash
python Advanced_DFA_ChatBot.py
```

You will enter an interactive mode where you can start chatting with the bot and use the available commands.

---

## 🧾 Commands

| Command                 | Description                           |
| ----------------------- | ------------------------------------- |
| `help`                  | List all available commands           |
| `stats`                 | Show conversation statistics          |
| `patterns`              | List all learned or stored patterns   |
| `learn`                 | Enable learning mode                  |
| `export`                | Export conversation history to `.txt` |
| `settings`              | Modify runtime settings               |
| `clear`                 | Clear conversation history            |
| `exit` / `quit` / `bye` | End the chat                          |

---

## 📁 Exported Files

* `patterns.json` – Stores learned patterns
* `conversation.txt` – Stores full chat history with timestamps

## Demo

![image](https://github.com/user-attachments/assets/23a5a00d-8d7e-45ed-83ac-e6369ae2725f)

![image](https://github.com/user-attachments/assets/05b30597-c861-4679-8663-71799d4e0452)

![image](https://github.com/user-attachments/assets/d62ed8b5-03a6-432f-bc01-34c40772f390)



