from app.models.mongo_model import FileMongo
from app.configs.mongodb import documents_collection

async def save_mongo_data(data: FileMongo):
    return await documents_collection.insert_one(data)
