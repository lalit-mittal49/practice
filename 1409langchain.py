import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=api_key
)



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
""" prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert educator. Adapt your explanations to the target audience level."),
    ("human",""Explain the topic '{topic}' for a '{level}' level learner.
    Format your output strictly with the following sections:
1. Simple Explanation
2. Concrete Real-World Example
3. 3 Key Points (as bullet points)
4. 2 Practice Questions (to test understanding)"")
])
parser = StrOutputParser()
chain= prompt | model | parser
inputs=[
    {"topic": "Machine Learning", "level": "beginner"},
    {"topic": "Docker and Containers", "level": "intermediate"},
    {"topic": "Recursion in Programming", "level": "beginner"},
    {"topic": "Quantum Computing", "level": "advanced"}
]
result=chain.batch(inputs)
print(result) """

#3
""" prompt = ChatPromptTemplate.from_messages([
    ("system" , "You are an experienced Python developer."),
    ("human" , "Explain {topic}")
])
def clean_text(text):
    text = text.strip()
    text = " ".join(text.split())
    return text
cleaner = RunnableLambda(clean_text)
parser = StrOutputParser()
chain = cleaner|prompt|model|parser
input = "Explain Python functions. "
result = chain.invoke(input)
print(result) """


#4
"""prompt = ChatPromptTemplate.from_messages(
    ("system" , "You are an experienced techincal interviewer and teacher."
    "Explain these topics in a very simple way."
    "For each topic generate :"
    "1. Definition"
    "2. One example"
    "3. One interview question"
    "Topic : {topic}")
)
parser = StrOutputParser()
chain = prompt|model|parser
inputs = [
    {"topic" : "REST API"},
    {"topic" : "Docker"},
    {"topic" : "Git Rebase"},
    {"topic" : "SQL Index"},
    {"topic" : "Async Programming"}
]
result = chain.batch(inputs)
print(result)
"""

#5
"""prompt = ChatPromptTemplate.from_messages([
    ("system" , "You are an experienced technical teacher."),
    ("human" , "Explain {topic} for {difficulty} student.")
])
parser = StrOutputParser()
chain = prompt|model|parser
for chunk in chain.stream({"topic":"Neural networks" , "difficulty":"beginner"}):
    print(chunk , end="")"""

#6
"""first_prompt = ChatPromptTemplate.from_messages([
    ("system" ,"You are an experienced topic describer."),
    ("human" , "explain this topic : {topic} in a very detailed way.") 
])
parser = StrOutputParser()
second_prompt = ChatPromptTemplate.from_messages([
    ("system" , "You are an experienced summary creator."),
    ("human" , "Generate a short summary on the basis of this explanation : {explanation}")
])
third_prompt = ChatPromptTemplate.from_messages([
    ("system" , "You are an experienced techincal interview questions generator."),
    ("human" , "generate the technical interview questions based on this summary : {summary}")
])
first_chain = first_prompt|model|parser
second_chain = second_prompt|model|parser
third_chain = third_prompt|model|parser

def prepare_explanation(explanation):
    return{
        "explanation" : explanation
    }
def prepare_summary(summary):
    return{
        "summary":summary
    }
chain = first_chain|RunnableLambda(prepare_explanation)|second_chain|RunnableLambda(prepare_summary)|third_chain

result = chain.invoke({
    "topic":"Vector Databases"
})
print(result)"""

