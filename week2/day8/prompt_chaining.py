import os
from pathlib import Path
from time import sleep
from xmlrpc import client
from dotenv import load_dotenv
from groq import Groq

model = os.getenv("MODEL")
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_llm(system_prompt, user_prompt):
    sys_msg={
        "role": "system",
        "content": system_prompt
    }
    user_msg={
        "role": "user",
        "content": user_prompt
    }
    messages=[sys_msg, user_msg]
    response = client.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content

def run_agent(prompt):

