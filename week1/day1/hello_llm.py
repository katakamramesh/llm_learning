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
role="user"
prompt="Do you know ramesh katakam"

message={
    "role" : role,
    "content" : prompt
}

messages=[message]
# Temperature by default is 0 meaning safe. range is [0,2]
response=client.chat.completions.create(model=model, messages=messages)
# print(response)

print("--------------------")

answer=response.choices[0].message.content
print(answer)

print("--------------------")