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

"""