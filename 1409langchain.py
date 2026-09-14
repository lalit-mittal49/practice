""" import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=api_key
)
 """


#1
""" prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an experienced {role}."),
    ("human", "Explain {topic}")
])
parser = StrOutputParser()
chain = prompt | model | parser

result = chain.invoke({
    "role": "Python Trainer",
    "topic": "decorators"
})

print(result) """

#2