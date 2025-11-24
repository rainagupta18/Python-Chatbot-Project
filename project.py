import random
import qrcode

# Predefined data
greetings = ['hello', 'hi', 'hey']
sad_words = ['i am sad', 'feeling low', 'depressed']
motivational_quotes = [
    "Believe in yourself.",
    "Every day is a second chance.",
    "You are stronger than you think.",
    "Push yourself, because no one else is going to do it for you."
]

# Help menu
def show_help():
    print("\nAvailable Features:")
    print("1. Greet you - Type 'hello', 'hi', or 'hey'")
    print("2. Help Menu - Type 'help' or 'menu'")
    print("3. Exit - Type 'q' or 'bye'")
    print("4. Detect sadness - Try 'I am sad' or 'feeling low'")
    print("5. Show a motivational quote - Type 'quote'")
    print("6. Generate a QR Code - Type 'qr'")

# QR code generator
def generate_qr():
    data = input("Enter the text or URL to generate QR code: ")
    img = qrcode.make(data)
    img.save("qr_code.png")
    print("QR Code has been saved as 'qr_code.png'.")

# Chatbot main function
def chatbot():
    print("Welcome! I am your chatbot. Type 'help' to see the list of features.")

    while True:
        user_input = input("\nYou: ").lower()

        if user_input in greetings:
            print("Bot: Hello. How can I help you?")
        elif user_input in ['help', 'menu']:
            show_help()
        elif user_input in ['q', 'bye']:
            print("Bot: Goodbye.")
            break
        elif any(phrase in user_input for phrase in sad_words):
            print("Bot: I'm sorry to hear that. You're not alone, and things will get better.")
        elif user_input == 'quote':
            print("Bot:", random.choice(motivational_quotes))
        elif user_input == 'qr':
            generate_qr()
        else:
            print("Bot: I didn't understand that. Type 'help' to see what I can do.")

chatbot()
