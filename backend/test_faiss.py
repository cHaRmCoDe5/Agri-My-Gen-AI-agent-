from backend.ingestion.pipeline import run
from backend.embeddings.embedder import Embedder
from backend.vectorstore.faiss_store import FAISSStore

print("Running ingestion...")
docs = run()

print("\nCreating embeddings...")
embedder = Embedder()
vectors = embedder.embed_documents(docs)

print("\nBuilding FAISS index...")
store = FAISSStore()
store.add_vectors(vectors)
store.save()

print("\nFAISS built successfully!")

print("\nTesting search...")
query_vector = vectors[0]["vector"]
results = store.search(query_vector)

for r in results:
    print("\n--- RESULT ---")
    print(r["text"][:300])