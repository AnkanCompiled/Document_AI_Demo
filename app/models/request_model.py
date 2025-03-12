from pydantic import BaseModel

class SearchRequest(BaseModel):
    prompt: str
    amount: int