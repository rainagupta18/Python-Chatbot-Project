import random
import sys
import time
import re
from pathlib import Path

APP_NAME = "BuddyBot"
DATA_DIR = Path("buddybot_outputs")
DATA_DIR.mkdir(exist_ok=True)

GREETINGS = {"hello", "hi", "hey"}
SAD_KEYPHRASES = [
    "i am sad", "i'm sad", "i feel sad",
    "feeling low", "feeling down",
    "depressed", "i am depressed", "i'm depressed"
]

MOTIVATIONAL_QUOTES = [
    "Believe in yourself.",
    "Every day is a second chance.",
    "You are stronger than you think.",
    "Keep going.",
    "Small steps every day add up to big changes."
]

def slow_print(text):
    for ch in str(text):
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(random.uniform(0.002, 0.009))
    print()

def safe_input(prompt="> "):
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        slow_print("Bot: Goodbye")
        sys.exit(0)

def sanitize_filename(text):
    text = text.strip().lower()
    text = re.sub(r"\s+", "_", text)
    text = re.sub(r"[^a-z0-9_\-]", "", text)
    return text[:40] or "output"

def show_help():
    slow_print("")
    slow_print("Commands:")
    slow_print("  hello / hi / hey")
    slow_print("  help / menu")
    slow_print("  quote")
    slow_print("  codeart")
    slow_print("  bye / quit / q")
    slow_print("  about")
    slow_print("")

def generate_code_art():
    user_text = safe_input("Enter text for code-art: ")
    if not user_text:
        slow_print("Bot: Empty input.")
        return

    size = max(8, min(32, len(user_text) * 2))
    pattern = []

    for r in range(size):
        row = []
        for c in range(size):
            ch = user_text[(r + c) % len(user_text)]
            val = (ord(ch) + r * 3 + c * 2) % 100

            if val < 40:
                row.append("#")
            elif val < 70:
                row.append("o")
            elif val < 85:
                row.append("+")
            else:
                row.append(" ")
        pattern.append("".join(row))

    name = sanitize_filename(user_text)
    filename = DATA_DIR / f"codeart_{name}_{int(time.time())}.txt"

    with filename.open("w", encoding="utf-8") as f:
        for line in pattern:
            f.write(line + "\n")

    slow_print("Bot: File saved as: " + str(filename))
    slow_print("Preview:")
    for line in pattern[:10]:
        slow_print(line)

def chatbot():
    slow_print("Hello. I am " + APP_NAME + ". Type 'help' for commands.\n")

    while True:
        msg = safe_input("You: ").lower()

        if not msg:
            slow_print("Bot: Say something.")
            continue

        if msg in GREETINGS:
            slow_print(random.choice([
                "Hey, how can I help?",
                "Hi, what do you need?",
                "Hello, what can I do for you?"
            ]))
        elif msg in {"help", "menu"}:
            show_help()
        elif msg == "quote":
            slow_print(random.choice(MOTIVATIONAL_QUOTES))
        elif msg in {"q", "quit", "bye", "exit"}:
            slow_print("Bot: Goodbye")
            break
        elif msg == "about":
            slow_print(APP_NAME + " is a simple Python chatbot.")
        elif msg == "codeart":
            generate_code_art()
        elif any(p in msg for p in SAD_KEYPHRASES):
            slow_print(random.choice([
                "I am sorry you feel that way.",
                "I understand. Things will get better.",
                "I am here if you want to talk."
            ]))
        else:
            slow_print("Bot: I did not understand that. Type 'help'.")

if __name__ == "__main__":
    try:
        chatbot()
    except Exception as e:
        slow_print("Bot: Error: " + str(e))
        sys.exit(1)
