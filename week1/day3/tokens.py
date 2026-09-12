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
role = "user"

prompt1 = "hi"
prompt2 = "explain time travel in detail"
prompt3 = "write  1000 words essay on machine learning"

prompts = [prompt1,prompt2,prompt3]
messages = []

for prompt in prompts:
    message={
        "role": "user",
        "content": prompt
    }

    messages=[message]

    response = client.chat.completions.create(
    model=model, 
    messages=messages
    )

    usage = response.usage

    print(f"Prompt: {prompt} -->your tokens: {usage.prompt_tokens} completion_tokens: {usage.completion_tokens} total tokens: {usage.total_tokens}  Finish Reason: {response.choices[0].finish_reason}")
    print("user tokens : " , usage.prompt_tokens)
    print(f"machine tokens : {usage.completion_tokens}") # modern formatting - f string