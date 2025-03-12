from app.configs.pinecone import index
import asyncio
from functools import partial

async def save_vector_data(doc_id, embedding, summary):
    loop = asyncio.get_event_loop()
    upsert_partial = partial(index.upsert, vectors=[(doc_id, embedding, {"summary": summary})])
    await loop.run_in_executor(None, upsert_partial)
    print(f"Summary stored with id: {doc_id}")

async def search_vector_data(embedding, amount):
    loop = asyncio.get_event_loop()
    query_partial = partial(index.query, vector=embedding, top_k=amount, include_metadata=True)
    result = await loop.run_in_executor(None, query_partial)
    return result.get("matches", [])
