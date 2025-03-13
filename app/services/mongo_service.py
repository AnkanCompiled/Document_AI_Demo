from app.models.mongo_model import FileMongo
from app.middlewares.app_error import AppError
from app.configs.mongodb import documents_collection
from bson import ObjectId

async def save_mongo_data(data: FileMongo):
    return await documents_collection.insert_one(data)

from bson import ObjectId
from fastapi import HTTPException

async def search_mongo_data(doc_id: str):
    if ObjectId.is_valid(doc_id):
        doc_obj_id = ObjectId(doc_id)
        document =  await documents_collection.find_one({"_id": doc_obj_id})
        if document:
            document["_id"] = str(document["_id"])
            return document
        else:
            raise AppError(status_code=404, detail="Document not found")

    else:
        raise AppError(status_code=400, detail="Invalid ObjectId format")
