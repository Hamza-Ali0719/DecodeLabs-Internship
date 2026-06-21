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
 
