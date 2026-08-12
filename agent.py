print("Welcome to Student Assistant Agent")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Agent: Hello! How can I help you?")

    elif user_input == "study":
        print("Agent: Make a study plan and practice regularly.")

    elif user_input == "python":
        print("Agent: Python is useful for AI and Machine Learning.")

    elif user_input == "bye":
        print("Agent: Goodbye! Keep learning.")
        break

    else:
        print("Agent: Sorry, I don't understand your request.")
