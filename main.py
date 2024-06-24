import spacy

# Load the English language model for spaCy
nlp = spacy.load('en_core_web_sm')

# Function to process user input
def process_input(input_text):
    doc = nlp(input_text)
    # Perform NLP tasks here if needed
    return doc

print("Hello! I am a simple chatbot. How can I assist you today?")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "bye", "quit"]:
        print("Chatbot: Goodbye! Have a great day!")
        break

    processed_input = process_input(user_input)
    # Add logic to generate responses based on processed input
    print("Chatbot: [Response here]")
