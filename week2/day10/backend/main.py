from fastapi import FastAPI
from pypdf import PdfReader
from pathlib import Path

app = FastAPI()

@app.get("/")
def home():
    resume_text = read_pdf(Path("ramesh_katakam.pdf"))
    return {
        "message" : "Hello World!!"
    }

def read_pdf(file_path: Path):
    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"
    return text
