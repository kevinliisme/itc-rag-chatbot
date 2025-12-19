from app.db.vector_store import collection
from app.rag.embeddings import embed_texts


def retrieve_context(query: str, top_k: int = 5) -> list[str]:
    """
    Retrieve top-k relevant text chunks for a query.
    """
    q_emb = embed_texts([query])[0]

    results = collection.query(
        query_embeddings=[q_emb],
        n_results=top_k,
        include=["documents"],
    )

    return results["documents"][0]
