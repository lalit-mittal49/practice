import os
import json
from dotenv import load_dotenv
from pydantic import BaseModel, ValidationError
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

#1
""" class Resume(BaseModel):
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    location: str | None = None
    experience_years: int | None = None
    skills: list[str] | None = None
    education: list[str] | None = None
    current_role: str | None = None


prompt_template = ""
You are an AI resume information extraction system.
Extract information ONLY from the supplied resume.
Rules:
1. Do not invent any information.
2. Do not infer missing skills.
3. Do not infer missing experience.
4. If information is not available, return null.
5. Return only structured JSON matching the schema.

Resume:
{resume}
""

def extract_resume(resume_text: str) -> Resume | None:
    try:
        prompt = prompt_template.format(resume=resume_text)
        
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": Resume,
            },
        )

        return response.parsed
    except Exception as e:
        print("\nError while processing resume:")
        print(e)
        return None


def save_resume(result: Resume, filename: str = "resume_data.json") -> None:
        data = result.model_dump()
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"\nResume saved successfully to '{filename}'!")



resume_text = input("\nEnter resume text:\n")

if not resume_text.strip():
    print("\nNo resume text provided.")
else:
    result = extract_resume(resume_text)
    if result is not None:
            try:
                # Ensure validation integrity
                validated_resume = Resume.model_validate(result)

                print("\n--- Extracted Resume Data ---")
                print("Name:           ", validated_resume.name)
                print("Email:          ", validated_resume.email)
                print("Phone:          ", validated_resume.phone)
                print("Location:       ", validated_resume.location)
                print("Experience:     ", validated_resume.experience_years)
                print("Skills:         ", validated_resume.skills)
                print("Education:      ", validated_resume.education)
                print("Current Role:   ", validated_resume.current_role)

                save_resume(validated_resume)

            except ValidationError as e:
                print("\nPydantic Validation Error:")
                print(e)
    else:
            print("\nCould not extract resume information.") """

#2
""" class customerSupport(BaseModel):
    category: str | None = None
    priority: str | None = None
    sentiment: str | None = None
    summary: str | None = None
    requires_human_support: bool | None = None

prompt_template = ""
You are an AI customer complaint triage system.
Analyze the provided customer complaint and extract structured information strictly according to these rules:

Rules:
1. Category must strictly be one of: billing, technical_support, account, delivery, general.
2. If the category cannot be clearly determined or does not fit, return null.
3. Priority must strictly be one of: low, medium, high.
4. Sentiment must strictly be one of: positive, neutral, negative.
5. Set requires_human_support to true if urgent action, refund, or technician assistance is needed; otherwise false.
6. Provide a concise summary of the issue.
7. Return only structured JSON matching the schema.
Complaint:
{complaint} ""

def extract_complaint(complaint_text: str) -> customerSupport | None:
    prompt = prompt_template.format(complaint=complaint_text)
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": customerSupport,
        },
    )
    return response.text
complaint_text = input("\nEnter customer complaint text:\n")
if not complaint_text.strip():
    print("\nNo complaint text provided.")
else:
    result = extract_complaint(complaint_text)
    print("\n--- Extracted Complaint Data ---")
    print(result) """

#3