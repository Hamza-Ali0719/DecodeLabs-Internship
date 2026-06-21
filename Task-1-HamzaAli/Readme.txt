# 🤖 Rule-Based AI Chatbot – Project 1

**Batch:** 2026 | **Powered by DecodeLabs**

A simple yet robust rule‑based chatbot built in Python, demonstrating core AI concepts: control flow, decision‑making logic, and deterministic response generation. This project serves as the foundational milestone for the DecodeLabs Artificial Intelligence internship.

---

## 📚 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Sample Interaction](#sample-interaction)
- [Requirements](#requirements)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

## 📖 Overview

This chatbot uses a **dictionary‑based intent mapping** with regular expression patterns to match user inputs and generate predefined responses. It runs in an infinite loop, sanitizes input, and provides a graceful exit. The project emphasises **traceability** and **deterministic logic** – the hallmarks of a well‑architected rule‑based system.

---

## ✨ Features

- ✅ **Multi‑intent support** – handles greetings, name inquiries, help requests, and farewells.
- ✅ **Regex pattern matching** – accepts synonyms and variations (e.g., “hi”, “hey”, “hello”).
- ✅ **Randomised responses** – adds personality and avoids repetition.
- ✅ **Continuous loop** – keeps the conversation alive until the exit command.
- ✅ **Input sanitisation** – strips whitespace and handles empty input.
- ✅ **Fallback responses** – provides meaningful replies for unrecognised inputs.
- ✅ **Logging** – records all interactions for debugging and evaluation.
- ✅ **Error handling** – robust against unexpected user input or system interrupts.
- ✅ **Modular design** – easy to extend with new intents or response variations.

---

## 🛠 Installation

1. **Clone the repository** (or create a new folder for your project):
   ```bash
   git clone https://github.com/yourusername/rule-based-chatbot.git
   cd rule-based-chatbot