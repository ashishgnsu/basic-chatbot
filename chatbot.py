import random

def chatbot():
    print("Chatbot: Hello! I’m your virtual assistant. Type 'bye' anytime to exit.")

    greetings = ["hello", "hi", "hey", "good morning", "good evening"]
    responses_greeting = ["Hello there!", "Hi", "Hey! How’s it going?", "Nice to see you!"]

    how_are_you = ["how are you", "how are you?"]
    responses_how = ["I’m doing great, thanks for asking!", "I’m fine. How about you?", "Pretty good!"]

    goodbyes = ["bye", "goodbye", "exit", "see you"]
    responses_bye = ["Goodbye", "See you soon!", "Take care!", "Bye! Have a great day!"]

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in greetings:
            print("Chatbot:", random.choice(responses_greeting))

        elif user_input in how_are_you:
            print("Chatbot:", random.choice(responses_how))

        elif user_input in ["i am fine", "i'm fine", "good", "great"]:
            print("Chatbot: That’s awesome to hear!")

        elif user_input in ["what is your name", "who are you"]:
            print("Chatbot: I’m a simple chatbot created in Python .")

        elif user_input in ["what can you do", "help"]:
            print("Chatbot: I can chat with you, respond to greetings, and say goodbye.")

        elif user_input in goodbyes:
            print("Chatbot:", random.choice(responses_bye))
            break

        else:
            print("Chatbot: Hmm I’m not sure how to respond to that.")

# Run the chatbot
chatbot()
