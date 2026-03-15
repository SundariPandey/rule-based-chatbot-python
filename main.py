#________Rule Based AI ChatBot_________

import datetime
import time

name = input("Welcome ,Enter your name: ")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good Morningg!, ",name)
elif 11 <= presentHour <= 17:
    print("Good Afternoon, ",name)
elif 17 <= presentHour <= 20:
    print("Good Evening!, ",name)
else:
    print("Good night, ",name)


print("Namaste! Welcome to my rule-based chatbot. I am here to answer your basic questions.")
print("You can type your message to start chatting. If you want to end the conversation, type 'bye'.")

#ChatBot Memory creation [dictionary of responses]


responses = {
    "hello": "Namaste! Nice to meet you. How can I help you today?",
    "hi": "Hello! I am happy to chat with you.",
    "hey": "Hey there! What would you like to talk about?",
    "how are you": "I am doing great as a chatbot. How are you today?",
    "what is your name": "My name is a rule-based chatbot created using Python.",
    "who created you": "I was created by a Python learner as a mini project.",
    "what can you do": "I can answer basic questions and greetings.",
    "help": "You can say hello, ask my name, or have a simple conversation with me.",
    "thank you": "You are welcome! I am glad I could help.",
    "thanks": "No problem! Happy to help.",
    "good morning": "Good morning! I hope you have a wonderful day.",
    "good afternoon": "Good afternoon! How is your day going?",
    "good evening": "Good evening! How can I assist you?",
    "where are you from": "I live inside a Python program.",
    "are you human": "No, I am just a chatbot created using Python.",
    "what is python": "Python is a popular programming language used for many applications.",
    "what is ai": "Artificial Intelligence is technology that allows machines to simulate human intelligence.",
    "tell me a joke": "Why did the computer go to the doctor? Because it caught a virus!",
    "what is your purpose": "My purpose is to answer simple questions and demonstrate a rule-based chatbot.",
    "do you like coding": "Yes! Coding is fun and powerful.",
    "what is your favourite language": "I like Python because it is simple and powerful.",
    "who are you": "I am a simple rule-based chatbot.",
    "nice": "I am glad you think so!",
    "bye": "Goodbye! Thank you for chatting with me. Have a great day!"
}

#Method/Function to get response of chatbot

def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    default_response = "Sorry, I don't understand that yet. Please try asking something else."
    return default_response

def typingEffect(text):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.02)
    print()

#...Count = how many questions asked user...
count = 0
while True:
    userInput = input("Please ask your question:")
    count += 1
    
    # Time feature
    if "time" in userInput.lower():
        print("Bot Response:", datetime.datetime.now().strftime("%H:%M:%S"))
        continue

    # Date feature
    if "date" in userInput.lower():
        print("Bot Response:", datetime.datetime.now().strftime("%d-%m-%Y"))
        continue

     # Calculator feature
    try:
        result = eval(userInput)
        print("Bot Response:", result)
        continue
    except:
        pass


   
    reply = getResponseOfBot(userInput)
    
    print("Bot is thinking.......")
    time.sleep(1)   #  (1 second wait karega aur soch ke reply dega)
    print("Bot Response:", end=" ")
    typingEffect(reply)

    if "bye" in userInput.lower():
     print("You asked", count, "questions in this chat.")
     break 
