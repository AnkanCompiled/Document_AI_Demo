import aiofiles
import os
from app.services.convert_service import convert_to_text
from app.services.ai_service import summarize_document, create_embedding
from app.services.mongo_service import save_mongo_data, search_mongo_data
from app.services.vector_service import save_vector_data
from app.middlewares.app_error import AppError

async def upload_file(file, dir):
    os.makedirs(dir, exist_ok=True)
    file_path = os.path.join(dir, file.filename)

    async with aiofiles.open(file_path, "wb") as f:
        await f.write(await file.read())

    text = convert_to_text(file_path)
    if not (text):
        raise AppError(status_code=404, detail="Document empty")

    doc = await save_mongo_data({"name": file.filename, "path": file_path})
    summary = await summarize_document(text)
    embedding = await create_embedding(f"file: {file.filename} {summary}")
    await save_vector_data(str(doc.inserted_id), embedding, summary)
    return doc.inserted_id



async def get_file(doc_id):
    return await search_mongo_data(doc_id)