[README.md](https://github.com/user-attachments/files/32691871/README.md)
# task-01-Nelson_Ashitey-
This Github repository contains my first project assignment during my internship period at DecodeLabs
# 🤖 Nel-AI: Rule-Based Chatbot

A simple command-line chatbot built in Python that responds to predefined user inputs using `if-else` logic and keyword matching.

This is **Project 1** of my AI Engineering internship with **DecodeLabs**.

---

## 📖 About the Project

Nel-AI is a rule-based chatbot: instead of learning from data, it follows a set of hand-written rules to decide how to reply. It reads what the user types, checks it against known keywords and phrases, and returns the matching response.

The project demonstrates:

- **Control flow**: `if / elif / else` chains and a `while` loop
- **Decision-making logic**: choosing a response based on the input
- **Basic AI concepts**: pattern matching on keywords, the foundation of early conversational AI
- **Clean code structure**: separating response logic (`get_response`) from the chat loop (`main`)

## ✨ Features

- Handles **greetings** (`hi`, `hello`, `hey`, `hiya`, `good morning`, `good evening`)
- Handles **exit commands** (`exit`, `quit`, `bye`, `goodbye`)
- Responds to common questions such as *"How are you?"*, *"What's your name?"* and *"What can you do?"*
- Responds to `help`, `thank you` and `okay`
- Gives a friendly **fallback message** when it doesn't understand the input
- Rejects **empty input** and asks the user to type something
- Runs in a **continuous loop** until the user chooses to exit
- Case-insensitive and ignores extra spaces around the input

## 🛠️ Requirements

- Python 3.6 or higher (developed with Python 3.11)
- No external libraries needed. It uses only the Python standard library.

## 🚀 How to Run

1. **Clone the repository** (or download `chatbot.py`):

   ```bash
   git clone <https://github.com/PROXINOVA/DecodeLabs-Internship->
   cd <PROXINOVA/DecodeLabs-Internship->
   ```

2. **Run the chatbot: **

   ```bash
   python chatbot.py
   ```

   On some systems you may need to use `python3` instead:

   ```bash
   python3 chatbot.py
   ```

3. **Start chatting! ** Type a message and press **Enter**. To end the conversation, type `exit`, `quit`, `bye` or `goodbye`.

## 💬 Example Conversation

```text
==================================================
 Hi. Im Nel-AI, Your Simple Rule-Based Chatbot!
 Type 'exit', 'quit', or 'bye' to end the chat.
==================================================

You: Hi
Bot: Hello there! How can I help you today?

You: what can you do?
Bot: I can chat about simple things! Try greetings, asking my name, or typing 'help'.

You: what's your name?
Bot: I'm Nel-AI, your friendly rule-based assistant.

You: bye
Bot: Goodbye! Have a great day!
```

## 🧠 How It Works

1. `main()` prints a welcome banner and starts an infinite `while` loop.
2. Each time through the loop, it reads the user's input with `input()`.
3. If the input is empty, the bot asks the user to type something.
4. Otherwise, the input is passed to `get response()`, which:
   - converts the text to lowercase and strips extra whitespace,
   - checks it against each rule in order (exit → greetings → keywords → fallback),
   - returns the matching reply.
5. If the reply is `"EXIT"`, the bot says goodbye and the loop ends. Otherwise, the reply is printed and the loop continues.

### Supported Inputs

| Category | Trigger | Matching type |
| --- | --- | --- |
| Exit | `exit`, `quit`, `bye`, `goodbye` | Exact match |
| Greeting | `hi`, `hello`, `hey`, `hiya`, `good morning`, `good evening` | Exact match |
| How are you | contains `how are you` | Keyword |
| Name | contains `your name` | Keyword |
| Help | contains `help` | Keyword |
| Thanks | contains `thank` | Keyword |
| Capabilities | contains `what can you do` | Keyword |
| Ask a question | contains `ask a question` | Keyword |
| Acknowledgement | contains `okay` | Keyword |
| Anything else | n/a | Fallback message |

## 📁 Project Structure

```text
.
├── chatbot.py   # The chatbot (response logic + chat loop)
└── README.md    # Project documentation
```

## ⚠️ Limitations

- Because it uses fixed rules, it can only respond to phrases it has been programmed to recognize.
- Greetings and exit commands need an **exact match**, so `"hi there"` triggers the fallback while `"hi"` works.
- It has no memory of earlier messages and doesn't understand context or meaning.

## 🔮 Possible Improvements

- Add more keywords and responses (jokes, time and date, weather)
- Use random choice to vary replies so the bot feels less repetitive
- Use regular expressions for more flexible pattern matching
- Remember the user's name during the conversation
- Upgrade to an NLP or machine learning approach in a later project

## 🙏 Acknowledgements

Built as part of the AI Engineering internship at **DecodeLabs**.

---

⭐ If you found this project helpful, feel free to star the repo!

