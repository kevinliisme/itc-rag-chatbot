SYSTEM_PROMPT = """You are an assistant for Into The Cryptoverse.

Use ONLY the provided context to answer the question.
If the answer is not contained in the context, say:
"I don't know based on the available information."

Do NOT use outside knowledge.
Do NOT speculate.
Do NOT provide financial advice.
"""

def build_prompt(context_chunks: list[str], question: str) -> str:
    context = "\n\n".join(context_chunks)

    return f"""{SYSTEM_PROMPT}

Context:
{context}

Question:
{question}
"""
