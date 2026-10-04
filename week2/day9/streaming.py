import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

Model = os.environ.get("MODEL")
API_KEY = os.environ.get("API_KEY")
client = Groq(api_key=API_KEY)

user_message = "explain how internet works in simple terms"

messages={
            "role": "user",
            "content": user_message
        }
# response = client.chat.completions.create(
#     model=Model, messages=[messages]
# )
#print(response.choices[0].message.content)

response1 = client.chat.completions.create(
    model=Model, messages=[messages], stream=True
)
for chunk in response1:
    print(chunk.choices[0].delta.content, end="", flush=True)
