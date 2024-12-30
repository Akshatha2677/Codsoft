
def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").strip().lower()
        
      
        if user_input == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there! How can I help you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bot, but I'm doing great! How about you?")
        elif "your name" in user_input:
            print("Chatbot: I'm called Chatbot. What's your name?")
        elif "your age" in user_input:
            print("Chatbot: my age has not be mentioned")
        elif"your work" in user_input:
            print("Chatbot: I help the people to solve the questions")
        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%I:%M %p")
            print(f"Chatbot: The current time is {current_time}.")
        elif "national fruit" in user_input:
           print("Chatbot:the national fruit is MANGO")
        elif "weather" in user_input:
            print("Chatbot: I can't provide real-time weather updates")
        else:    
            print("Chatbot: I'm sorry, I don't understand that. Can you rephrase?")


chatbot()
