from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from app.controllers.upload_controller import upload_file

file_router = APIRouter(prefix="/file", tags=["File"])

UPLOAD_DIR = "files"

@file_router.post("/upload")
async def api_upload_file(file: UploadFile = File(...)):
    doc_id = await upload_file(file, UPLOAD_DIR)
    return JSONResponse(status_code=200,  content={"message": "Upload Successful", "doc_id": str(doc_id)})

