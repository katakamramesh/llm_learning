import json
import os

from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel
from fastapi import FastAPI
from pypdf import PdfReader
from pathlib import Path

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = os.getenv("GROQ_MODEL")

app = FastAPI()

@app.get("/")
def home():
    resume_text = read_pdf(Path("ramesh_katakam.pdf"))
    print(resume_text)
    return {
        "message" : "resume parsed successfully"
    }

def read_pdf(file_path: Path):
    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"
    return text
