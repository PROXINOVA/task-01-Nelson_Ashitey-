"""
Simple Rule-Based Chatbot
--------------------------
A basic chatbot that uses if-else logic to respond to predefined
user inputs. Demonstrates control flow, decision-making logic,
and basic AI concepts (pattern matching on keywords).
"""

def get_response(user_input):
    """Determine chatbot response based on simple keyword matching."""
    text = user_input.lower().strip()

    # --- Exit commands ---
    if text in ("exit", "quit", "bye", "goodbye"):
        return "EXIT"

    # --- Greetings ---
    elif text in ("hi", "hello", "hey", "hiya", "good morning", "good evening"):
        return "Hello there! How can I help you today?"

    # --- How are you ---
    elif "how are you" in text:
        return "I'm just a program, but I'm running smoothly. Thanks for asking!"

    # --- Name questions ---
    elif "your name" in text:
        return "I'm Nel-AI, your friendly rule-based assistant."
 
    # --- Help ---
    elif "help" in text:
        return "You can say hi, ask my name, ask how I am, or type 'exit' to quit."

    # --- Thanks ---
    elif "thank" in text:
        return "You're welcome!"

    # --- What can you do ---
    elif "what can you do" in text:
        return "I can chat about simple things! Try greetings, asking my name, or typing 'help'."

    # --- Asking questions ---
    elif "ask a question" in text:
        return "Sure. What would you like to know?."
    # ---Okay response ---
    elif "okay" in text:
        return "Alright, Is there something else I can help with?."

    # --- Default fallback ---
    else:
        return "I'm sorry, I didn't understand that. Type 'help' to see what I can do."


def main():
    print("=" * 50)
    print(" Hi. Im Nel-AI, Your Simple Rule-Based Chatbot!")
    print(" Type 'exit', 'quit', or 'bye' to end the chat.")
    print("=" * 50)

    while True:
        user_input = input("\nYou: ")

        if not user_input.strip():
            print("Bot: Please type something.")
            continue

        response = get_response(user_input)

        if response == "EXIT":
            print("Bot: Goodbye! Have a great day!")
            break
        else:
            print(f"Bot: {response}")


if __name__ == "__main__":
    main()
