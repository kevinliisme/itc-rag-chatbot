from pathlib import Path
from app.ingest.website import ingest_website_folder

if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parents[1]
    data_path = repo_root / "data" / "website"

    print("Repo root:", repo_root)
    print("Data path:", data_path)
    print("Exists?", data_path.exists())
    print("Files:", list(data_path.glob("*")))

    ingest_website_folder(data_path)
    print("Website ingestion complete.")
