from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from app.controllers.file_controller import upload_file, get_file
from app.controllers.search_controller import search_file, file_query
from app.models.request_model import SearchRequest, FileQueryRequest, GetFileRequest
from app.middlewares.app_error import AppError


file_router = APIRouter(prefix="/file", tags=["File"])

UPLOAD_DIR = "files"

@file_router.post("/upload")
async def api_upload_file(file: UploadFile = File(...)):
    doc_id = await upload_file(file, UPLOAD_DIR)
    return JSONResponse(status_code=201,  content={"message": "Upload Successful", "doc_id": str(doc_id)})

@file_router.post("/search")
async def api_search_file(req: SearchRequest):
    result = await search_file(req.prompt, req.amount)
    return JSONResponse(status_code=200, content=result)

@file_router.post("/file_query")
async def api_file_query(req: FileQueryRequest):
    result = await file_query(req.prompt, req.doc_info, UPLOAD_DIR)
    return JSONResponse(status_code=200, content=result)

@file_router.post("/get_file")
async def api_get_file(req : GetFileRequest,):
    result = await get_file(req.doc_id)
    return JSONResponse(status_code=200, content=result)