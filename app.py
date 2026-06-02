import streamlit as st
from ibm_watsonx_ai.foundation_models import Model
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
PROJECT_ID = os.getenv("PROJECT_ID")
URL = os.getenv("URL")

credentials = {
    "url": URL,
    "apikey": API_KEY
}
print("API KEY:", API_KEY[:10] if API_KEY else "NOT FOUND")
print("PROJECT:", PROJECT_ID)
print("URL:", URL)

model = Model(
    model_id="openai/gpt-oss-120b",
    credentials=credentials,
    project_id=PROJECT_ID
)

st.title("🎓 IntelliCheck AI")

st.subheader("AI-Driven Plagiarism Intelligence")

student = st.text_input("Student Name")
course = st.text_input("Course Name")

assignment = st.text_area(
    "Paste Assignment Text",
    height=250
)

if st.button("Analyze Assignment"):

    prompt = f"""
You are IntelliCheck AI, an academic integrity assistant.

Analyze the assignment and generate ONLY the report.

Student: {student}
Course: {course}

Assignment:
{assignment}

Rules:
- Do not repeat the assignment text.
- Do not explain your task.
- Generate only the report.
- Use professional academic language.
- External similarity cannot be verified without a plagiarism database.
- Similarity analysis should only consider repeated content within the submitted text.

Output Format:

Academic Integrity Report

Student:
Course:

Writing Quality:

AI Content Assessment:

Similarity Analysis:

Risk Level:

Suspicious Indicators:
- item
- item

Faculty Recommendation:

Final Verdict:
"""

    with st.spinner("Analyzing..."):

        response = model.generate_text(
            prompt=prompt
        )

    st.subheader("📋 Academic Integrity Report")
    st.write(response)