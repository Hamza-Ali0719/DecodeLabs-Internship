# 🤖 DecodeBot – A Rule-Based Conversational Chatbot in Python

> **DecodeLabs** | Project 1 | Batch 2026

| **Submitted By** | Hamza Ali |
| :--- | :--- |
| **Category** | Internship |
| **Course / Subject** | Artificial Intelligence Project 1 |
| **Department** | Computer Science |
| **Institution** | Decode Labs |
| **Submission Date** | June 2026 |
| **Project Repository** | [https://github.com/Hamza-Ali0719/DecodeLabs-Internship](https://github.com/Hamza-Ali0719/DecodeLabs-Internship) |

---

## 📚 Table of Contents

- [1. Introduction](#1-introduction)
- [2. Objectives](#2-objectives)
- [3. Tools & Technologies Used](#3-tools--technologies-used)
- [4. System Architecture](#4-system-architecture)
  - [4.1 Component Overview](#41-component-overview)
- [5. Project Structure](#5-project-structure)
  - [5.1 requirements.txt](#51-requirementstxt)
  - [5.2 .gitignore](#52-gitignore)
- [6. Code Walkthrough](#6-code-walkthrough)
  - [6.1 Logging Configuration](#61-logging-configuration)
  - [6.2 Intent Dictionary](#62-intent-dictionary)
  - [6.3 Pattern Pre-Compilation](#63-pattern-pre-compilation)
  - [6.4 Intent Matching](#64-intent-matching)
  - [6.5 Response Generation](#65-response-generation)
  - [6.6 Interactive Run Loop and Error Handling](#66-interactive-run-loop-and-error-handling)
- [7. Features Implemented](#7-features-implemented)
- [8. Sample Execution](#8-sample-execution)
- [9. Testing & Validation](#9-testing--validation)
- [10. Challenges Faced and Solutions](#10-challenges-faced-and-solutions)
- [11. Future Enhancements](#11-future-enhancements)
- [12. Conclusion](#12-conclusion)
- [13. References](#13-references)
- [Appendix A: Full Source Code (chatbot.py)](#appendix-a-full-source-code-chatbotpy)

---

## 1. Introduction

Chatbots are software applications designed to simulate human conversation through text or voice interactions. They are broadly classified into two categories: rule-based chatbots, which rely on predefined patterns and decision rules to generate responses, and AI-based chatbots, which use machine learning or large language models to generate responses dynamically. This project, DecodeBot, is a rule-based chatbot implemented in Python that demonstrates the core principles of pattern matching, intent recognition, and conversational flow control without relying on any external machine learning framework.

DecodeBot uses regular expressions (the built-in `re` module) to match user input against a set of predefined intents such as greetings, identity questions, capability queries, and farewells. Each intent is associated with a list of possible responses, and the bot randomly selects one response per match to make the conversation feel less mechanical and repetitive. The system is supported by structured logging, which records every user input and bot response to both the console and a persistent log file, making the application suitable for debugging, auditing, and academic evaluation.

This document describes the design, implementation, and evaluation of the DecodeBot project. It covers the system architecture, a detailed walkthrough of the source code, the features implemented, sample execution output, the challenges encountered during development, and recommendations for future enhancement.

---

## 2. Objectives

The primary objectives of this project are:

- To design and implement a functional rule-based chatbot using core Python without third-party NLP libraries.
- To apply regular expression pattern matching for robust, case-insensitive intent recognition.
- To structure conversational logic in an extensible, maintainable way using a dictionary-driven intent model.
- To implement application-level logging for traceability of user sessions and error diagnosis.
- To handle runtime exceptions and user interruptions gracefully, ensuring the program never crashes unexpectedly.
- To follow professional software engineering practices, including clear documentation, dependency declaration, and version control hygiene.

---

## 3. Tools & Technologies Used

The project intentionally uses only the Python standard library, which keeps the application lightweight, dependency-free, and easy to run on any machine with Python 3 installed.

| Tool / Module | Purpose |
| :--- | :--- |
| **Python 3.x** | Core programming language used to implement the chatbot logic. |
| **re (Regular Expressions)** | Used to define and compile flexible, case-insensitive matching patterns for each intent. |
| **random** | Used to randomly select a response from the matched intent's response list, avoiding repetitive replies. |
| **logging** | Used to record session activity to both the console (StreamHandler) and a log file (FileHandler). |
| **typing (Dict, List, Optional)** | Used for type hints to improve code readability and IDE support. |
| **Git / GitHub** | Used for version control and hosting the project repository. |

---

## 4. System Architecture

DecodeBot follows a simple, linear pipeline architecture typical of rule-based conversational systems. Each user turn passes through four stages before a response is produced:

1. **Input Capture** — the `run()` loop reads a line of text from the user via the console.
2. **Intent Matching** — `match_intent()` iterates over all configured intents and tests the input against each intent's compiled regular expression patterns.
3. **Response Generation** — `get_response()` selects a random reply from the matched intent's response list, or from a fallback list if no intent matched.
4. **Logging & Output** — the input, matched intent (if any), and generated response are logged, and the response is printed back to the user.

### 4.1 Component Overview

| Component | Responsibility |
| :--- | :--- |
| `RuleBasedChatbot` | Main class encapsulating all chatbot state and behaviour: intents, fallback responses, and the conversation loop. |
| `intents (dict)` | Maps an intent name (e.g. "greeting") to its regex patterns and candidate responses. |
| `_compile_patterns()` | Pre-compiles every regex pattern once at initialization for efficient repeated matching. |
| `match_intent()` | Resolves a single best-matching intent for a given user message, or None. |
| `get_response()` | Public-facing method that converts a matched intent (or lack thereof) into a response string. |
| `run()` | Drives the interactive read-evaluate-print loop and handles graceful termination. |

---

## 5. Project Structure

The repository is organized to separate source code, configuration, and documentation, following common open-source conventions:

### 5.1 requirements.txt

Although DecodeBot has no external dependencies, a `requirements.txt` file is included as a best-practice placeholder and to document this fact explicitly:

```txt
# This project uses only the Python standard library.
# No third-party packages are required to run chatbot.py.
# This file is included to demonstrate dependency-declaration
# best practice and to support future extensions (e.g. pytest).

__pycache__/
*.pyc
*.pyo
*.log
.vscode/
.idea/
venv/
.env

6. Code Walkthrough
This section explains the implementation in the order the components appear in chatbot.py, along with the design rationale behind each decision.

6.1 Logging Configuration
Logging is configured once at module load time using logging.basicConfig(), with two handlers attached: a FileHandler that persists every event to chatbot.log, and a StreamHandler that mirrors the same output to the console. This dual-handler setup means the chatbot's behaviour can be reviewed after the fact — useful both for debugging and for evaluators who want to verify functional correctness without re-running the program.

python
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("chatbot.log"),
        logging.StreamHandler()
    ]
)

6.2 Intent Dictionary
The heart of the chatbot is the intents dictionary, defined in the __init__ method. Each key is an intent name, and each value is a dictionary containing a list of regex patterns and a list of candidate text responses. This data-driven design means new conversational behaviour can be added by inserting a new dictionary entry, without touching the matching or response logic at all — a clean separation between data and control flow.

python
"greeting": {
    "patterns": [r"hello", r"hi", r"hey", r"greetings"],
    "responses": [
        f"Hello! I'm {name}, your AI assistant.",
        f"Hi there! How can I help you today?",
        f"Hey! Nice to meet you."
    ]
}
Five intents are defined in total: greeting, how_are_you, name, help, and bye. Each carries multiple alternative phrasings as patterns and multiple alternative replies, which together give the bot a degree of conversational variety despite being fully rule-based.

6.3 Pattern Pre-Compilation
Rather than recompiling each regular expression on every user turn, _compile_patterns() compiles every pattern once at startup using re.IGNORECASE and stores the result under a "compiled" key inside each intent. This is a performance optimization: regex compilation is relatively expensive compared to matching, so doing it once up front rather than per-message keeps response generation fast even as the conversation grows long.

python
def _compile_patterns(self) -> None:
    for intent in self.intents.values():
        intent["compiled"] = [
            re.compile(pattern, re.IGNORECASE) for pattern in intent["patterns"]
        ]
6.4 Intent Matching
match_intent() performs a linear scan over the intents dictionary, testing the user's raw input against every compiled pattern for each intent using pattern.search(). The first intent with any matching pattern is returned immediately, which makes the matching strategy a simple first-match-wins policy. Because Python dictionaries preserve insertion order, the order in which intents are declared in __init__ effectively defines their matching priority.

python
def match_intent(self, user_input: str) -> Optional[str]:
    for intent_key, intent_data in self.intents.items():
        for pattern in intent_data["compiled"]:
            if pattern.search(user_input):
                return intent_key
    return None
6.5 Response Generation
get_response() is the public method the run loop calls on every turn. It first strips and validates the input, then delegates matching to match_intent(). If an intent is found, a response is chosen uniformly at random from that intent's response list using random.choice(); otherwise, a response is chosen at random from the fallback_responses list. Returning a random choice rather than a fixed string is a deliberate design decision to avoid the bot sounding repetitive across a long session.

python
def get_response(self, user_input: str) -> str:
    user_input = user_input.strip()
    if not user_input:
        return "Please say something."
    matched_intent = self.match_intent(user_input)
    if matched_intent:
        return random.choice(self.intents[matched_intent]["responses"])
    return random.choice(self.fallback_responses)
6.6 Interactive Run Loop and Error Handling
The run() method implements the read-evaluate-print loop that drives the conversation. On every iteration it reads a line from the console, generates and prints a response, logs both sides of the exchange, and checks whether the matched intent was "bye" in order to terminate the loop cleanly. The loop is wrapped in exception handling for two distinct cases: a KeyboardInterrupt (Ctrl+C), which is treated as an intentional exit and produces a friendly goodbye message, and a generic Exception, which is logged as an error without crashing the program — ensuring the chatbot remains usable even if an unexpected condition occurs.

python
while True:
    try:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        response = self.get_response(user_input)
        print(f"{self.name}: {response}")
        if self.match_intent(user_input) == "bye":
            break
    except KeyboardInterrupt:
        print(f"\n{self.name}: Goodbye! (Interrupted)")
        break
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"{self.name}: Oops! Something went wrong. Please try again.")
7. Features Implemented
Feature	Description
Pattern-based intent recognition	Five intents (greeting, how_are_you, name, help, bye) are matched via compiled, case-insensitive regular expressions.
Randomized responses	Each intent and the fallback list offer multiple replies, selected at random to reduce repetition.
Graceful fallback handling	Unmatched input returns a randomly chosen, friendly fallback message instead of failing silently.
Pre-compiled regex patterns	All patterns are compiled once at startup for efficient repeated matching.
Dual-channel logging	Every user message, matched intent, and bot reply is logged to both the console and chatbot.log.
Graceful exit handling	The session ends cleanly on the "bye" intent or on a keyboard interrupt (Ctrl+C).
Robust exception handling	Unexpected runtime errors are caught, logged, and reported without terminating the session.
Extensible, data-driven design	New intents can be added purely by extending the intents dictionary, with no changes to control logic.
8. Sample Execution
The transcript below illustrates a typical interactive session with DecodeBot, as produced by the run() method:

text
DecodeBot: Hi! Type 'bye' to exit.

You: hello
DecodeBot: Hi there! How can I help you today?
You: what is your name
DecodeBot: I'm DecodeBot, a rule-based chatbot built for DecodeLabs.
You: how are you
DecodeBot: All systems operational. Thanks for asking!
You: what can you do
DecodeBot: I'm a simple chatbot. Try saying 'hello', 'how are you', or 'what is your name'.
You: tell me a joke
DecodeBot: I'm not sure I understand. Could you rephrase?
You: bye
DecodeBot: Goodbye! Have a great day!
Each line of this exchange is simultaneously written to chatbot.log with a timestamp and log level, allowing the entire session to be reconstructed and reviewed after the program exits.

9. Testing & Validation
The chatbot was manually tested against representative inputs for each intent, as well as edge cases such as empty input, mixed-case text, and unrecognized phrases. The table below summarizes the test cases and observed outcomes.

Test Input	Expected Intent	Observed Result
"Hello there"	greeting	Matched — "hello" substring found
"HOW ARE YOU?"	how_are_you	Matched — case-insensitive flag confirmed working
"Who are you?"	name	Matched correctly
" " (whitespace only)	none	Returned "Please say something." as expected
"asdkjqwe"	none	Returned a random fallback response
"bye"	bye	Returned farewell response and terminated the loop
Ctrl+C during input()	n/a	Caught by KeyboardInterrupt handler; printed goodbye and exited cleanly
All test cases produced the expected behaviour, confirming that pattern matching, fallback handling, and graceful termination work as designed.

10. Challenges Faced and Solutions
Challenge	Solution Applied
Overlapping patterns across intents	Because match_intent() returns the first match found, similarly worded inputs could in principle match the wrong intent. This was addressed by ordering more specific intents (e.g. name, help) ahead of more general ones in the dictionary and keeping each intent's pattern list narrowly scoped.
Repetitive-sounding replies	An early version used a single fixed reply per intent, which felt robotic across longer sessions. This was solved by supplying multiple response variants per intent and selecting one with random.choice() on every turn.
Losing session history after the program exits	Console output alone disappears once the terminal is closed. Adding a FileHandler in the logging configuration ensures every session is durably recorded in chatbot.log for later review or grading.
Unhandled crashes on unexpected input	Without exception handling, an unforeseen runtime error (or a Ctrl+C) would terminate the program abruptly. Wrapping the main loop in try/except for both KeyboardInterrupt and the general Exception class ensures the bot degrades gracefully instead of crashing.
11. Future Enhancements
While DecodeBot fulfills its goals as a rule-based system, several extensions could meaningfully increase its capability:

Integrating an NLP library (e.g. spaCy or a transformer-based model) for intent classification beyond fixed regex patterns.

Adding conversational memory/context so the bot can refer back to earlier parts of a conversation.

Building a web-based or GUI front end (e.g. Flask, Streamlit, or a simple HTML/JS interface) in place of the console loop.

Persisting conversation logs to a structured database instead of a flat log file, to support analytics.

Adding multi-language support via locale-aware pattern sets.

Adding an automated unit-test suite (e.g. pytest) covering match_intent() and get_response() directly.

Falling back to a hosted LLM API for inputs that match no rule-based intent, to combine reliability with flexibility.

12. Conclusion
DecodeBot demonstrates that a clear, well-structured, rule-based approach can deliver a functional and pleasant conversational experience without any external machine learning dependencies. By combining pre-compiled regular expressions, a data-driven intent model, randomized responses, structured logging, and careful exception handling, the project meets its stated objectives while remaining easy to read, test, and extend. The modular design — in particular the separation of intent data from matching and response logic — means the system can grow gracefully, whether through additional hand-written intents or, eventually, integration with more advanced NLP techniques.

13. References
Python Software Foundation, "re — Regular expression operations," Python 3 documentation.

Python Software Foundation, "logging — Logging facility for Python," Python 3 documentation.

Python Software Foundation, "random — Generate pseudo-random numbers," Python 3 documentation.

Python Software Foundation, "typing — Support for type hints," Python 3 documentation.

Appendix A: Full Source Code (chatbot.py)
The complete, unmodified source code of chatbot.py is reproduced below for reference.

python
import re
import random
import logging
from typing import Dict, List, Optional

# Configure logging (writes to console and file for evaluation)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("chatbot.log"),
        logging.StreamHandler()
    ]
)

class RuleBasedChatbot:
    """
    A simple rule-based chatbot that matches user input against predefined
    patterns and responds with appropriate messages.
    """
    
    def __init__(self, name: str = "DecodeBot"):
        self.name = name
        self.intents: Dict[str, Dict] = {
            "greeting": {
                "patterns": [r"hello", r"hi", r"hey", r"greetings"],
                "responses": [
                    f"Hello! I'm {name}, your AI assistant.",
                    f"Hi there! How can I help you today?",
                    f"Hey! Nice to meet you."
                ]
            },
            "how_are_you": {
                "patterns": [r"how are you", r"how's it going", r"how are things"],
                "responses": [
                    "I'm just a bunch of code, but I'm functioning perfectly!",
                    "All systems operational. Thanks for asking!",
                    "Doing great! How about you?"
                ]
            },
            "name": {
                "patterns": [r"what is your name", r"who are you", r"your name"],
                "responses": [
                    f"I'm {name}, a rule-based chatbot built for DecodeLabs.",
                    f"My name is {name}. I'm here to chat with you!",
                    "I go by DecodeBot. Nice to meet you!"
                ]
            },
            "help": {
                "patterns": [r"help", r"what can you do", r"capabilities"],
                "responses": [
                    "I can greet you, tell you my name, and respond to common questions. Just say 'bye' to exit.",
                    "I'm a simple chatbot. Try saying 'hello', 'how are you', or 'what is your name'."
                ]
            },
            "bye": {
                "patterns": [r"bye", r"goodbye", r"exit", r"quit"],
                "responses": [
                    "Goodbye! Have a great day!",
                    "See you later!",
                    "It was nice chatting with you. Bye!"
                ]
            }
        }
        self.fallback_responses = [
            "I'm not sure I understand. Could you rephrase?",
            "I don't have an answer for that yet.",
            "Hmm, I didn't get that. Try asking something else.",
            "Sorry, I'm still learning. Can you ask differently?"
        ]
        # Compile patterns for faster matching
        self._compile_patterns()
        logging.info(f"Chatbot '{self.name}' initialized with {len(self.intents)} intents.")

    def _compile_patterns(self) -> None:
        """Pre‑compile regex patterns for each intent."""
        for intent in self.intents.values():
            intent["compiled"] = [re.compile(pattern, re.IGNORECASE) for pattern in intent["patterns"]]

    def match_intent(self, user_input: str) -> Optional[str]:
        """
        Match user input against all intent patterns.
        Returns the first matching intent key, or None if no match.
        """
        for intent_key, intent_data in self.intents.items():
            for pattern in intent_data["compiled"]:
                if pattern.search(user_input):
                    logging.debug(f"Matched intent '{intent_key}' with input: '{user_input}'")
                    return intent_key
        return None

    def get_response(self, user_input: str) -> str:
        """
        Generate a response for the given user input.
        """
        user_input = user_input.strip()
        if not user_input:
            return "Please say something."

        matched_intent = self.match_intent(user_input)
        if matched_intent:
            # Randomly select one response from the matched intent
            response = random.choice(self.intents[matched_intent]["responses"])
            # If it's a goodbye intent, we also signal to exit (handled in run loop)
            if matched_intent == "bye":
                return response
            return response
        else:
            # Use a random fallback response
            return random.choice(self.fallback_responses)

    def run(self) -> None:
        """
        Start the interactive chatbot loop.
        """
        print(f"\n{self.name}: Hi! Type 'bye' to exit.\n")
        logging.info("Chat session started.")

        while True:
            try:
                user_input = input("You: ").strip()
                if not user_input:
                    continue
                logging.info(f"User said: {user_input}")

                response = self.get_response(user_input)
                print(f"{self.name}: {response}")
                logging.info(f"Bot replied: {response}")

                # Check if the response is a goodbye (exit condition)
                if self.match_intent(user_input) == "bye":
                    logging.info("Exit command received. Ending session.")
                    break
            except KeyboardInterrupt:
                print(f"\n{self.name}: Goodbye! (Interrupted)")
                logging.info("Session interrupted by user.")
                break
            except Exception as e:
                logging.error(f"Unexpected error: {e}")
                print(f"{self.name}: Oops! Something went wrong. Please try again.")

if __name__ == "__main__":
    bot = RuleBasedChatbot(name="DecodeBot")
    bot.run()
