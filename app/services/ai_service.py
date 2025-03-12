from app.configs.genai import embedding_model, chat_model
from langchain.schema import HumanMessage, SystemMessage

async def create_embedding(text):
    return await embedding_model.aembed_query(text)

async def summarize_document(text):
    messages = [
        SystemMessage(content="Identify the document type (e.g., CV, Legal Document, Invoice, Research Paper, etc..) and generate a structured summary highlighting key details relevant to its category, such as credentials in a CV, legal terms in a contract, or financial data in an invoice, etc.., and make it good for searching in pinecone"),
        HumanMessage(content=text[:40000])
    ]
    
    response = await chat_model.ainvoke(messages)
    return response.content

async def answer_query(query, summary):
    if not query or not summary:
        print("Invalid Search")
        return None
    
    messages = [
        SystemMessage(content=f"Generate a response based on this summary: {summary}"),
        HumanMessage(content=query[:40000])
    ]
    
    response = await chat_model.ainvoke(messages)
    return response.content