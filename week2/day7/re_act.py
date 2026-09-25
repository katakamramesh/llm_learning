import os
from pathlib import Path
from time import sleep
from dotenv import load_dotenv
from groq import Groq

import re

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

cli = Groq(api_key=my_api_key)
model = os.getenv("MODEL")

def get_prodcut_price(product):
    if product == "laptop":
        return 1000
    elif product == "phone":
        return 500
    elif product == "tablet":
        return 300
    else:
        return "Product not found"

def calculator(expression):
    try:
        result = eval(expression)
        return result
    except:
        return "Invalid expression"

tools = {
    "get_product_price": get_prodcut_price,
    "calculator": calculator
}

system_prompt = """
you are a shopping assistant. You have access to the following tools:
1. get_product_price(product): This tool takes a product name as input and returns the price of the product. The available products are: laptop, phone, tablet.
2. calculator(expression): This tool takes a mathematical expression as input and returns the result of the expression.

Important: 
call tools exactly like these examples:

Action: get_product_price("phone")
Action: calculator("2000 - 500")

Never write:
get_product_price(product = "phone")\

Never write:
calculator(expression = "2000 - 500")\

Follow these rules:

1. Decide what you need to do next.
2. Call Only one tool at a time.
3. After writing an action, stop immediately
4. Never guess or invent a tool result.
5. wait until you receive an obervation.
6. If you have all the information you need, provide the final answer to the user.

Format

Thought: what you need to do
Action: tool_name("input")

when finished, provide the final answer in the following format:

Final Answer: your final answer here
"""

def run_agent(question):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question}
    ]

    while True:

        print("\nAssistant is thinking...")
        response = cli.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.2
        )

        assistant_message = response.choices[0].message.content

        print(f"Assistant: {assistant_message}")

        # Check if the assistant has provided a final answer
        if "Final Answer:" in assistant_message:
            break

        # Extract the action from the assistant's message
        action_match = re.search(r'Action:\s*(\w+)\("([^"]+)"\)', assistant_message)

        if action_match:
            tool_name = action_match.group(1)
            tool_input = action_match.group(2)
            tool_input = tool_input.strip()  # Remove leading/trailing whitespace
            tool_input = tool_input.strip('"')  # Remove surrounding quotes if present

            # Call the appropriate tool
            if tool_name in tools:
                observation = tools[tool_name](tool_input)
                print(f"Observation: {observation}")
                messages.append({"role": "assistant", "content": assistant_message})
                messages.append({"role": "user", "content": f"Observation: {observation}"})
            else:
                print(f"Error: Tool '{tool_name}' not found.")
                break
        else:
            print("Error: No valid action found in the assistant's message.")
            break

prompt = """i have 5000rs with me.
What is the price of a laptop and how much money will be left after buying it?
"""

run_agent(prompt)