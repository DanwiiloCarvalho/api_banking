from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title="API Banking")


@app.get("/")
async def root():
    return {"message": f"Hello World {settings.DATABASE_URL}"}
