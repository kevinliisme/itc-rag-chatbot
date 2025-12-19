from app.core import config  # noqa: F401 (load env)
from fastapi import FastAPI
from app.api.chat import router

app = FastAPI()
app.include_router(router)


@app.get("/health")
def health():
    return {"status": "ok"}
