from fastapi import FastAPI
from app.core import config

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
