from pydantic import BaseModel

class SearchRequest(BaseModel):
    prompt: str
    amount: int

class FileQueryRequest(BaseModel):
    prompt: str
    doc_info: object

class GetFileRequest(BaseModel):
    doc_id: str