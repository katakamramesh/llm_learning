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

bad_prompt = """
This is a user complaint:
My laptop is not working classify this
"""

bad_prompt1 = """

#Role: You are a Support Assistant for a laptop company 
#Task: You have to classify the user complaint in a catogory
#Constraint: you have to classify the user complaint in one of the following categories: Hardware, Software, Network
#Output: You answer should be in the one word and above mentioned constraints only

This is a user complaint:
My girlfirend has left me classify this
"""

good_prompt1 = """

#Role: You are a Support Assistant for a laptop company 
#Task: You have to classify the user complaint in a catogory
#Constraint: you have to classify the user complaint in one of the following categories: Hardware, Software, Network
#Output: You answer should be in the one word and above mentioned constraints only

This is a user complaint:
My Laptop is not working classify this
"""

print(llm_answer(good_prompt1))


print(llm_answer(bad_prompt1))