import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key missed")

client=Groq(api_key=my_api_key)
model="openai/gpt-oss-120b"


system_wife={
    "role":"system",
    "content": "You are my loving wife"
}
system_manager={
    "role":"system",
    "content": "You are my strict line manager"
}
system_company={
    "role":"system",
    "content": "You are a brand manager who suggests the name for food company, name should be one word"
}

user_wife={
    "role" : "user",
    "content" : "i love you babe"
}
user_manager={
    "role" : "user",
    "content" : "i love you baby"
}
user_company={
      "role":"user",
      "content": "suggest me a good brand for my food company"
}

messages_wife=[system_wife,user_wife]
messages_manager=[system_manager,user_manager]
messages_company=[system_company,user_company]

# Temperature by default is 0 meaning safe. range is [0,2]
response_wife=client.chat.completions.create(model=model, messages=messages_wife)
response_manager=client.chat.completions.create(model=model, messages=messages_manager, temperature=1)
response_company=client.chat.completions.create(model=model, messages=messages_company, temperature=2)

# print(response)

print("--------------------")
print(response_wife.choices[0].message.content)
print("--------------------")
print(response_manager.choices[0].message.content)
print("--------------------")
print(response_company.choices[0].message.content)
print("--------------------")
