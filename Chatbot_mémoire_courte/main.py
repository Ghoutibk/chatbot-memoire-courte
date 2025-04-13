from chatbot import ask_gpt

print("💬 Bienvenue dans le chatbot ! (écris 'exit' pour quitter)")

while True:
    user_input = input("Vous : ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 À bientôt !")
        break

    response = ask_gpt(user_input)
    print("Bot :", response)