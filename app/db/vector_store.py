import chromadb
from chromadb.config import Settings

# Persistent local vector DB
client = chromadb.Client(
    Settings(
        persist_directory="chroma",
        anonymized_telemetry=False,
    )
)

# Single unified collection for now
collection = client.get_or_create_collection(
    name="itc_knowledge"
)
