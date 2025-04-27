# Simple text-based chatbot (no libraries needed)

print("Hello! I'm your chatbot. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()
    
    if user_input == "bye":
        print("Chatbot: Goodbye! Have a nice day!")
        break
    elif "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hello there! How can I help you?")
    elif "how are you" in user_input:
        print("Chatbot: I'm good, thanks for asking!")
    elif "your name" in user_input:
        print("Chatbot: I'm just a simple chatbot.")
    else:
        print("Chatbot: I'm not sure how to respond to that.")





#Hello! I'm your chatbot. Type 'bye' to exit.

#You: hi
#Chatbot: Hello there! How can I help you?
#You: what is your name
#Chatbot: I'm just a simple chatbot.
#You: how are you
#Chatbot: I'm good, thanks for asking!
#You: bye
#Chatbot: Goodbye! Have a nice day!
#PS D:\Desktop\Python programes> 