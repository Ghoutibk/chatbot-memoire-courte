import os
import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Charge les variables depuis le fichier .env

openai.api_key = os.getenv("OPENAI_API_KEY")

print("Clé API chargée :", openai.api_key[:10], "...")

def ask_gpt(user_input):
    messages = [
        {"role": "system", "content": "Tu es un assistant amical et concis."},
        {"role": "user", "content": user_input}
    ]

    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return response.choices[0].message.content

