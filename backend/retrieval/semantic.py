from backend.embeddings.embedder import Embedder
from backend.vectorstore.faiss_store import FAISSStore
from backend.utils.logger import get_logger

logger = get_logger("SemanticRetriever")


class SemanticRetriever:
    def __init__(self, k=3):
        self.k = k
        self.embedder = Embedder()
        self.store = FAISSStore()

    def search(self, query: str):
        if not query or not query.strip():
            return []

        try:
            query_vector = self.embedder.embed_text(query)
            results = self.store.search(query_vector, k=self.k)

            logger.info(f"Semantic search returned {len(results)} results")
            return results

        except Exception as e:
            logger.error(f"Semantic search failed: {e}")
            return []


if __name__ == "__main__":
    retriever = SemanticRetriever(k=3)

    query = input("Ask AgriAssist: ")

    results = retriever.search(query)

    print("\nTop Semantic Results:\n")

    for i, result in enumerate(results, start=1):
        print("=" * 60)
        print(f"Result {i}")
        print("Text:")
        print(result.get("text", "")[:500])
        print("\nMetadata:")
        print(result.get("metadata", {}))

