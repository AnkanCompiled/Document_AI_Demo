from pinecone import Pinecone, ServerlessSpec
import os
from dotenv import load_dotenv
from app.middlewares.app_error import AppError

load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
if not PINECONE_API_KEY:
    raise AppError(status_code=404, detail="PINECONE_API_KEY not found")

PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
if not PINECONE_INDEX_NAME:
    raise AppError(status_code=404, detail="PINECONE_INDEX_NAME not found")

pc = Pinecone(api_key=PINECONE_API_KEY)


if not pc.has_index(PINECONE_INDEX_NAME):
    print(f"Creating Pinecone index: {PINECONE_INDEX_NAME}")
    pc.create_index(
        name=PINECONE_INDEX_NAME,
        dimension=768,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
            )
    )

index = pc.Index(PINECONE_INDEX_NAME)
