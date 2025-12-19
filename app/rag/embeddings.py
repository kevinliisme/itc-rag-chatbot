# from app.core import config
# from openai import OpenAI

# client = OpenAI()

# def embed_texts(texts: list[str]) -> list[list[float]]:
#     """
#     Convert a list of texts into embedding vectors.
#     """
#     response = client.embeddings.create(
#         model="text-embedding-3-small",
#         input=texts,
#     )

#     return [item.embedding for item in response.data]

from sentence_transformers import SentenceTransformer

# Small, fast, very good for semantic search
_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts: list[str]) -> list[list[float]]:
    """
    Generate embeddings locally (no API calls).
    """
    embeddings = _model.encode(
        texts,
        show_progress_bar=False,
        normalize_embeddings=True,
    )
    return embeddings.tolist()
