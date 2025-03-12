from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.middlewares.error_handler import register_exception_handlers
from app.routes.file_route import file_router

app = FastAPI()

app.include_router(file_router)

register_exception_handlers(app)

@app.get("/")
async def api_router_check():
    return JSONResponse(status_code=200, content={"message": "Upload Successful"})


