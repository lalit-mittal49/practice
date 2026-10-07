import os
from typing import TypedDict, Annotated, List
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

# 1. Define the State that agents pass to each other
class PatientState(TypedDict):
    messages: List[BaseMessage]
    lab_report_text: str
    extracted_symptoms: str
    rag_context: str
    is_info_complete: bool
    final_analysis: str

# Initialize the LLM for the agents
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

# 2. Define the Agents (Nodes)
def symptom_collector_agent(state: PatientState):
    """Analyzes conversation to extract symptoms or ask follow-ups."""
    chat_history = "\n".join([f"{type(m).__name__}: {m.content}" for m in state["messages"]])
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a medical triage AI. Review the chat history. 
        If you DO NOT have enough information about symptoms, duration, and severity, ask ONE relevant follow-up question. Start your response with 'QUESTION:'.
        If you HAVE sufficient information, summarize the symptoms in a short list. Start your response with 'SYMPTOMS:'."""),
        ("user", "{history}")
    ])
    
    response = llm.invoke(prompt.format_messages(history=chat_history)).content
    
    if response.startswith("QUESTION:"):
        # Add the question to messages and mark incomplete
        new_msg = AIMessage(content=response.replace("QUESTION:", "").strip())
        return {"messages": state["messages"] + [new_msg], "is_info_complete": False}
    else:
        # Save symptoms and mark complete
        symptoms = response.replace("SYMPTOMS:", "").strip()
        return {"extracted_symptoms": symptoms, "is_info_complete": True}

def report_analysis_agent(state: PatientState):
    """Processes uploaded lab reports."""
    if not state.get("lab_report_text"):
        return {"lab_report_text": "No lab reports provided."}
    
    prompt = f"Extract key abnormal values and important findings from this medical report text:\n{state['lab_report_text']}"
    analysis = llm.invoke([HumanMessage(content=prompt)]).content
    return {"lab_report_text": analysis}

def medical_knowledge_agent(state: PatientState):
    """Simulates RAG retrieval from a Vector DB."""
    # In a full production app, you would query ChromaDB here.
    # For this executable demo, we simulate the retrieval based on symptoms.
    symptoms = state.get("extracted_symptoms", "")
    prompt = f"Retrieve relevant medical textbook guidelines and differential diagnosis for these symptoms: {symptoms}"
    rag_data = llm.invoke([HumanMessage(content=prompt)]).content
    return {"rag_context": rag_data}

def orchestrator_agent(state: PatientState):
    """Synthesizes all data into a final report with medical disclaimers."""
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a clinical orchestrator. Synthesize the following into a final report:
        Symptoms: {symptoms}
        Lab Findings: {labs}
        Medical Context: {context}
        
        RULES:
        1. DO NOT provide a definitive diagnosis.
        2. List at least 3 possible conditions.
        3. Begin exactly with: '⚠️ **DISCLAIMER:** This is an AI-generated analysis for informational purposes and does not replace professional medical advice.'"""),
    ])
    
    response = llm.invoke(prompt.format_messages(
        symptoms=state.get("extracted_symptoms"),
        labs=state.get("lab_report_text"),
        context=state.get("rag_context")
    )).content
    
    new_msg = AIMessage(content=response)
    return {"messages": state["messages"] + [new_msg], "final_analysis": response}

# 3. Build the Graph Workflow
workflow = StateGraph(PatientState)

# Add Nodes
workflow.add_node("symptom_collector", symptom_collector_agent)
workflow.add_node("report_analyzer", report_analysis_agent)
workflow.add_node("knowledge_rag", medical_knowledge_agent)
workflow.add_node("orchestrator", orchestrator_agent)

# Add Routing Logic
def route_triage(state: PatientState):
    if state["is_info_complete"]:
        return "report_analyzer"
    return END # Stop and wait for user reply

workflow.set_entry_point("symptom_collector")
workflow.add_conditional_edges("symptom_collector", route_triage)
workflow.add_edge("report_analyzer", "knowledge_rag")
workflow.add_edge("knowledge_rag", "orchestrator")
workflow.add_edge("orchestrator", END)

# Compile the engine
medical_app = workflow.compile()