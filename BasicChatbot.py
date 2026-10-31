def get_reply(msg):
    msg = msg.lower().strip()

    # greetings
    if "hello" in msg or "hi" == msg or "hey" in msg:
        return "Hi! Nice to meet you."
    elif "good morning" in msg:
        return "Good morning! Hope you have a great day."
    elif "good night" in msg:
        return "Good night! Sleep well."

    # feelings
    elif "how are you" in msg:
        return "I'm fine, thanks! How about you?"
    elif "i am fine" in msg or "i'm fine" in msg or "good" == msg:
        return "That's great to hear!"
    elif "sad" in msg or "tired" in msg:
        return "Sorry to hear that. Take some rest, things will get better."
    elif "happy" in msg:
        return "Wonderful! Keep smiling."

    # about the bot
    elif "your name" in msg:
        return "I'm CodeBot, a simple chatbot made with Python."
    elif "who made you" in msg or "who created you" in msg:
        return "I was created by a student as an internship project."
    elif "what can you do" in msg or "help" in msg:
        return "I can chat, tell the time, tell a joke and share a fun fact."

    # time and date
    elif "time" in msg:
        from datetime import datetime
        return "The time is " + datetime.now().strftime("%I:%M %p")
    elif "date" in msg or "today" in msg:
        from datetime import datetime
        return "Today is " + datetime.now().strftime("%d %B %Y")

    # fun
    elif "joke" in msg:
        return "Why do programmers prefer dark mode? Because light attracts bugs!"
    elif "fun fact" in msg or "fact" in msg:
        return "Sri Lanka is famous for its cinnamon and tea."
    elif "favourite food" in msg or "favorite food" in msg:
        return "I love rice and curry, but I can only eat code!"
    elif "weather" in msg:
        return "I can't check the weather, but I hope it's sunny!"

    # study and python
    elif "python" in msg:
        return "Python is a popular and beginner friendly language."
    elif "study" in msg or "exam" in msg:
        return "Good luck! Study a little every day."

    # thanks and goodbye
    elif "thank" in msg:
        return "You're welcome!"
    elif "bye" in msg or "exit" in msg:
        return "Goodbye! Have a nice day."

    # anything else
    else:
        return "Sorry, I don't understand. Type 'help' to see what I can do."


print("=== CodeBot ===")
print("Type 'bye' to exit.\n")

while True:
    user_text = input("You: ")
    answer = get_reply(user_text)
    print("Bot:", answer)

    if "bye" in user_text.lower() or "exit" in user_text.lower():
        break