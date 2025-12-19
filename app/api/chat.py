from fastapi import APIRouter
from pydantic import BaseModel
from openai import OpenAI

from app.rag.retriever import retrieve_context
from app.rag.prompt import build_prompt

router = APIRouter()
client = OpenAI()


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str


@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    context_chunks = retrieve_context(req.question)
    prompt = build_prompt(context_chunks, req.question)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    answer = response.choices[0].message.content
    return {"answer": answer}
