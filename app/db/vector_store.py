import chromadb
from chromadb.config import Settings

# Explicit persistent client (THIS is the fix)
client = chromadb.PersistentClient(
    path="chroma",
    settings=Settings(
        anonymized_telemetry=False,
    ),
)

collection = client.get_or_create_collection(
    name="itc_knowledge"
)
