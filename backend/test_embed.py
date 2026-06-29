from backend.embeddings.embedder import Embedder
from backend.ingestion.pipeline import run

print("Running ingestion...")
docs = run()

print("\nCreating embeddings...")
embedder = Embedder()

vectors = embedder.embed_documents(docs)

print("\nTotal vectors created:", len(vectors))
print(vectors[0])