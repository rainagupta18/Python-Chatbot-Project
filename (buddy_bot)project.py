import random
import time
import sys
from pathlib import Path

# Predefined data
GREETINGS = ['hello', 'hi', 'hey']
SAD_KEYPHRASES = ['i am sad', 'feeling low', 'depressed', 'i feel sad', 'i am feeling low']
MOTIVATIONAL_QUOTES = [
    "Believe in yourself.",
    "Every day is a second chance.",
    "You are stronger than you think.",
    "Push yourself, because no one else is going to do it for you.",
    "Small steps every day add up to big changes."
]

APP_NAME = "BuddyBot"
DATA_DIR = Path(".") / "buddybot_outputs"
DATA_DIR.mkdir(exist_ok=True)



def slow_print(text, min_delay=0.01, max_delay=0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(random.uniform(min_delay, max_delay))
    print() 


def safe_input(prompt="> "):
    """Wrap input to handle Ctrl-D/Ctrl-C gracefully."""
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        slow_print("\nBot: Looks like you want to quit. Goodbye 👋")
        sys.exit(0)

def show_help():
    slow_print("\nAvailable Features:")
    slow_print("  1. Greet me — Type 'hello', 'hi', or 'hey'")
    slow_print("  2. Help/Menu — Type 'help' or 'menu'")
    slow_print("  3. Exit — Type 'q', 'quit', or 'bye'")
    slow_print("  4. Detect sadness — Say something like 'I am sad' or 'feeling low'")
    slow_print("  5. Get a motivational quote — Type 'quote'")
    slow_print("  6. Generate simple code-art — Type 'codeart' (replaces QR)")
    slow_print("  7. About the bot — Type 'about'\n")

def generate_code_art():
    text = safe_input("Enter text to convert into code-art (short works better): ").strip()
    if not text:
        slow_print("Bot: You didn't enter anything — returning to main menu.")
        return

    base_size = max(8, min(32, len(text) * 2)) 
    rows = cols = base_size

    pattern = []
    for r in range(rows):
        row_chars = []
        for c in range(cols):
            ch = text[(r + c) % len(text)]
            val = (ord(ch) + r * c + r + c) % 100
                row_chars.append("#")
            elif val % 5 == 0:
                row_chars.append("o")
            else:
                row_chars.append(" ")
        pattern.append("".join(row_chars))

    safe_name = "_".join(text.split())[:20] or "code"
    filename = DATA_DIR / f"codeart_{safe_name}_{int(time.time())}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Input: {text}\n\n")
        for line in pattern:
            f.write(line + "\n")

    slow_print(f"Bot: Your code-art has been created and saved as '{filename}'.")
    slow_print("Bot: Preview (first 7 lines):")
    for line in pattern[:7]:
        slow_print(line)
    slow_print("Bot: You can open the file to see the full pattern.")

def chatbot():
    slow_print(f"Hello — I'm {APP_NAME}! Type 'help' to see what I can do.")
    slow_print("Tip: You can press Ctrl+C any time to exit.\n")

    while True:
        user_input = safe_input("You: ").strip()
        if not user_input:
            slow_print("Bot: I didn't catch that — say 'help' to see commands.")
            continue
        user_lower = user_input.lower()
        if user_lower in GREETINGS:
            replies = [
                "Hey there! What can I do for you?",
                "Hi! How's your day going?",
                "Hello! Need something?"
            ]
            slow_print("Bot: " + random.choice(replies))

        elif user_lower in ['help', 'menu']:
            show_help()
          
        elif user_lower in ['q', 'quit', 'bye', 'exit']:
            slow_print("Bot: Goodbye — take care! 👋")
            break

        elif any(phrase in user_lower for phrase in SAD_KEYPHRASES):
            empathic_responses = [
                "I'm really sorry you're feeling that way. If you want to talk, I'm here.",
                "That sounds tough. You're not alone — would you like a motivational quote?",
                "I hear you. Consider reaching out to someone you trust, and if it's urgent, please seek professional help."
            ]
            slow_print("Bot: " + random.choice(empathic_responses))
     elif user_lower == 'quote':
            slow_print("Bot: " + random.choice(MOTIVATIONAL_QUOTES))

        elif user_lower == 'codeart':
            generate_code_art()

        elif user_lower == 'about':
            slow_print(f"Bot: {APP_NAME} v1.0 — a tiny friendly chatbot demo. Built to help you learn Python.")

        else:
            slow_print("Bot: I didn't understand that.")
            slow_print("Bot: Try typing 'help' to see the list of commands, or 'quote' for a quick pick-me-up.")


if __name__ == "__main__":
    chatbot()
