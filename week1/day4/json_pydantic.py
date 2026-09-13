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
from pydantic import BaseModel
class Ticket(BaseModel):
    name:"str"
    email:"str"
    issue:"str"

schema=Ticket.model_json_schema()

response_format={
    "type":"json_object"
}

system_prompt=f"""
extract the personal information striclty based on schema and give me json format.
{schema}
"""

message_system={
    "role" : "system",
    "content" : system_prompt
}


text="Hi, my name is ramesh, i have brought pixel phone and it is not working, " \
"please help to fix it, my email is abc@gmail.com and phone is 123123123 and i am from odisha, india"
prompt=f"""
this is a customer ticket, please extract the personal inforamtion from {text}
"""

message={
    "role" : role,
    "content" : prompt
}

messages=[message_system, message]
# Temperature by default is 0 meaning safe. range is [0,2]
response=client.chat.completions.create(model=model, messages=messages, response_format=response_format)
# print(response)

print("--------------------")

answer=response.choices[0].message.content
print(answer)

print("--------------------")

#how to read it
import json
raw_json = answer
data_file=json.loads(raw_json)
ticket =Ticket(**data_file)

#this can be forwarded to the other components
print(ticket.email)
print(ticket.name)
print(ticket.issue)

#Homework

# take resume in pdf or word
# have hr give you a list of things like skill, experience, projects
# extract these from resume 
# match against the hr list
# generate a percentage of matching or not