from pydantic import BaseModel

class FileMongo(BaseModel):
    name: str
    path: str
