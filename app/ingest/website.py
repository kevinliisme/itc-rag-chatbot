from pathlib import Path
from app.ingest.chunking import chunk_text
from app.rag.embeddings import embed_texts
from app.db.vector_store import collection


def ingest_website_folder(folder_path: Path):
    print("Ingest folder received:", folder_path)
    print("Exists?", folder_path.exists())

    files = list(folder_path.glob("*.md"))
    print("Markdown files found:", files)

    for file_path in files:
        print("Reading file:", file_path)

        text = file_path.read_text()
        print("Text length:", len(text))

        chunks = chunk_text(text)
        print("Chunks created:", len(chunks))

        if not chunks:
            print("⚠️ No chunks created, skipping file")
            continue

        embeddings = embed_texts(chunks)
        print("Embeddings created:", len(embeddings))

        for i, chunk in enumerate(chunks):
            collection.add(
                ids=[f"{file_path.stem}_{i}"],
                documents=[chunk],
                embeddings=[embeddings[i]],
                metadatas=[{
                    "source": "website",
                    "page": file_path.stem,
                }],
            )

        print(f"Finished ingesting {file_path.name}")
