import os
from pathlib import Path
from pyexpat.errors import messages
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=my_api_key)
model = os.getenv("MODEL")

def llm_answer(prompt):
    message = {
        "role": "user",
        "content": prompt
    }
    messages = [message]

    response = client.chat.completions.create(model=model, messages=messages)
    answer = response.choices[0].message.content
    return answer

bad_prompts = """
This is a user complaint:
My laptop is not working
classify this
"""

print(llm_answer(bad_prompts))