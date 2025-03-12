from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from app.controllers.file_controller import upload_file
from app.controllers.search_controller import search_file
from app.models.request_model import SearchRequest

file_router = APIRouter(prefix="/file", tags=["File"])

UPLOAD_DIR = "files"

@file_router.post("/upload")
async def api_upload_file(file: UploadFile = File(...)):
    doc_id = await upload_file(file, UPLOAD_DIR)
    return JSONResponse(status_code=201,  content={"message": "Upload Successful", "doc_id": str(doc_id)})

@file_router.post("/search")
async def api_search_file(request: SearchRequest):
    result = await search_file(request.prompt, request.amount)
    return JSONResponse(status_code=200, content=result)
