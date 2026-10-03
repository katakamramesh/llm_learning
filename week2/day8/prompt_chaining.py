import os
load_dotenv()
from pathlib import Path
from time import sleep
from xmlrpc import client
from dotenv import load_dotenv
from groq import Groq
from time import sleep

model = os.getenv("MODEL")
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

JD="""
We are hiring a Backend Python Developer.

Requirements:
- Strong Python
- FastAPI or Django
- PostgreSQL
- Docker
- AWS
- REST APIs
- 2+ years of experience
"""

RESUME="""
Name: Ramesh Katakam

Experience:
10 years of experience in a Software role.

Skills:
Python, FastAPI, MySQL, Docker,
REST APIs, Git

Projects:
Built a food delivery backend using
FastAPI and MySQL.

Deployed applications using Docker.
"""

def ask_llm(system_prompt, user_prompt):
    print("Asking LLM...")
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

def step1_resume_extract():
    print("Extracting skills from candidate's resume...")
    system_prompt = """
    You are a professional HR assistant, extract the skills from candidate's resume. 
    Do not include any other information, only return the skills in a comma separated format.
    """
    user_prompt = f"""
    Resume: {RESUME}
    """
    return ask_llm(system_prompt, user_prompt)

def step2_jd_extract():
    print("Extracting skills from job description...")
    system_prompt = """
    You are a professional HR assistant, extract the required skills from the job description. 
    Do not include any other information, only return the skills in a comma separated format.
    """
    user_prompt = f"""
    Job Description: {JD}
    """
    return ask_llm(system_prompt, user_prompt)

def step3_compare_skills(resume_skills, jd_skills):
    print("Comparing candidate's skills with job description...")
    system_prompt = """
    You are a professional HR assistant, compare the skills from candidate's resume and job description. 
    Return the result from 1 to 100, also produce a short verdict if he is a good fit.
    """
    user_prompt = f"""
    Resume Skills: {resume_skills}
    Job Description Skills: {jd_skills}
    """
    return ask_llm(system_prompt, user_prompt)

candidate_skills = step1_resume_extract() 
sleep(1)
job_skills = step2_jd_extract()
sleep(1)
score = step3_compare_skills(candidate_skills, job_skills)
print("Candidate Score:", score)