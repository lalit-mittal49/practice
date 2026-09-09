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
""" import json
import os
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class ProductInfo(BaseModel):
    product: str
    quantity: int
    unit_price: float


class Invoice(BaseModel):
    invoice_number: str
    customer: str
    invoice_date: str
    items: list[ProductInfo]
    tax_percentage: float
    total_amount: float

prompt_template = """
You are an AI invoice extraction system.
Extract structured information strictly from the invoice text.

Rules:
1. Extract all line items with quantity and unit price.
2. quantity must be >= 0.
3. unit_price cannot be negative.
4. Extract stated tax percentage and stated total amount.
5. Return only structured JSON matching the schema.

Invoice:
{invoice}
"""


def extract_invoice(invoice_text: str) -> Invoice | None:
    prompt = prompt_template.format(invoice=invoice_text)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": Invoice,
        },
    )
    if response.parsed:
        return response.parsed
    return Invoice.model_validate_json(response.text)

invoice_text = ""
Invoice No: INV-9087
Customer: ABC Technologies
Date: 01-09-2026
Product: Laptop
Quantity: 3
Unit Price: 65000
Tax: 18%
Total Amount: 230100
""

result = extract_invoice(invoice_text)

if result:
    print("\n--- Extracted Invoice ---")
    print("Invoice No:", result.invoice_number)
    print("Customer:  ", result.customer)
    print("Date:      ", result.invoice_date)
    print("Items:     ", result.items)
    print("Tax %:     ", result.tax_percentage)
    print("LLM Total: ", result.total_amount)

    subtotal = sum(item.quantity * item.unit_price for item in result.items)
    calculated_total = subtotal + (subtotal * result.tax_percentage / 100)

    print("\nPython Calculated Total:", calculated_total)

    if calculated_total != result.total_amount:
        print("Warning: LLM total does not match calculated total!")
    else:
        print("Total verified successfully!")

    with open("invoices.json", "w") as f:
        json.dump(result.model_dump(), f, indent=4)
    print("Saved to invoices.json!")
 """

#4
import json
import os
from typing import Literal
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


class CandidateEvaluation(BaseModel):
    candidate_name: str
    matched_skills: list[str]
    missing_skills: list[str]
    experience_years: int | None = None
    required_experience_years: int | None = None
    skill_match_score: int
    experience_match: bool
    recommendation: Literal["shortlist", "review", "reject"]
    reason: str


prompt_template = """
You are an AI Candidate Evaluation Engine.
Compare the Resume against the Job Description.

Rules:
1. Do not invent any skills not in the resume.
2. matched_skills must be present in both resume and JD.
3. missing_skills are required by JD but absent in resume.
4. skill_match_score must be between 0 and 100.
5. recommendation must strictly be: shortlist, review, or reject.
6. Return only structured JSON.

Job Description:
{jd}

Resume:
{resume}
"""


def evaluate_candidate(jd: str, resume: str) -> CandidateEvaluation | None:
    prompt = prompt_template.format(jd=jd, resume=resume)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": CandidateEvaluation,
        },
    )
    if response.parsed:
        return response.parsed
    return CandidateEvaluation.model_validate_json(response.text)


jd_text = """
Role: DevOps Engineer
Required Experience: 3+ years
Required Skills: AWS, Docker, Kubernetes, Terraform, Python
"""

resumes = [
    "Candidate: Aman. 3 years exp. Skills: AWS, Docker, Kubernetes, Terraform, Python.",
    "Candidate: Rohit. 1 year exp. Skills: Python, Git, Linux.",
    "Candidate: Simran. 4 years exp. Skills: AWS, Docker, Kubernetes, Jenkins.",
    "Candidate: Pooja. 5 years exp. Skills: Java, Spring Boot, MySQL.",
    "Candidate: Karan. 3 years exp. Skills: Docker, Kubernetes, AWS, Terraform.",
]

evaluations = []

for r in resumes:
    ev = evaluate_candidate(jd_text, r)
    if ev:
        evaluations.append(ev)

evaluations.sort(key=lambda x: x.skill_match_score, reverse=True)

print("\n--- Leaderboard ---")
for ev in evaluations:
    print(
        f"{ev.candidate_name}: Score {ev.skill_match_score}/100 -> {ev.recommendation}"
    )

print("\nTop Candidate:", evaluations[0].candidate_name)

with open("candidate_evaluation.json", "w") as f:
    json.dump([e.model_dump() for e in evaluations], f, indent=4)
print("Saved to candidate_evaluation.json!")

#5
import json
import os
from typing import Literal
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class DocumentType(BaseModel):
    document_type: Literal[
        "Resume",
        "Invoice",
        "Complaint",
        "Meeting Notes",
        "Product Description",
        "Unsupported",
    ]
    confidence: float


class ResumeData(BaseModel):
    name: str | None = None
    skills: list[str] = []
    experience: int | None = None


class InvoiceData(BaseModel):
    invoice_number: str
    amount: float


class ComplaintData(BaseModel):
    category: str
    priority: str
    sentiment: str


class MeetingNotesData(BaseModel):
    participants: list[str] = []
    decisions: list[str] = []
    action_items: list[str] = []

SCHEMA_MAP = {
    "Resume": ResumeData,
    "Invoice": InvoiceData,
    "Complaint": ComplaintData,
    "Meeting Notes": MeetingNotesData,
}


def classify_doc(text: str) -> DocumentType:
    prompt = f"Identify document type (Resume, Invoice, Complaint, Meeting Notes, Product Description, or Unsupported):\n{text}"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": DocumentType,
        },
    )
    return DocumentType.model_validate_json(response.text)


def extract_data(text: str, schema_class):
    prompt = f"Extract information matching the schema:\n{text}"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": schema_class,
        },
    )
    return schema_class.model_validate_json(response.text)


doc_text = """
Sprint Review Notes
Participants: Karan, Rohit, Aman
Decisions: Move deployment to Friday.
Action items: Aman to test APIs, Karan to configure Docker.
"""

doc_info = classify_doc(doc_text)
print(
    f"Classified as: {doc_info.document_type} (Confidence: {doc_info.confidence})"
)

if doc_info.document_type in SCHEMA_MAP:
    chosen_schema = SCHEMA_MAP[doc_info.document_type]
    extracted = extract_data(doc_text, chosen_schema)

    print("\n--- Extracted Data ---")
    print(extracted.model_dump())

    with open("doc_result.json", "w") as f:
        json.dump(extracted.model_dump(), f, indent=4)
    print("Saved to doc_result.json!")
else:
    print(f"Skipping: Type '{doc_info.document_type}' is not supported.")