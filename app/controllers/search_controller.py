from app.services.ai_service import create_embedding, answer_query
from app.services.vector_service import search_vector_data
from app.middlewares.app_error import AppError

async def search_file(prompt, amount):
    embedding = await create_embedding(prompt)
    if not len(embedding) == 768:
        raise AppError(status_code=400 ,detail="Error in embedding.")
    result = await search_vector_data(embedding, amount)

    if not result:
        raise AppError(status_code=404, detail="No result found")

    match_summary = result[0].get("metadata", {}).get('summary', None)
    
    if not match_summary:
        raise AppError(status_code=404, detail="No result found")

    ai_answer = await answer_query(prompt, match_summary)
    
    return {
        "answer": ai_answer,
        "documents": [item.get('id', 'Unknown') for item in result]
    }

    