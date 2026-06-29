from rank_bm25 import BM25Okapi
from backend.vectorstore.faiss_store import FAISSStore
from backend.utils.logger import get_logger

logger = get_logger("BM25Retriever")


class BM25Retriever:
    def __init__(self, k=3):
        self.k = k
        self.store = FAISSStore()
        self.documents = self.store.metadata

        self.texts = [doc["text"] for doc in self.documents]
        self.tokenized_texts = [text.lower().split() for text in self.texts]

        self.bm25 = BM25Okapi(self.tokenized_texts)

    def search(self, query: str):
        if not query or not query.strip():
            return []

        tokenized_query = query.lower().split()
        scores = self.bm25.get_scores(tokenized_query)

        ranked_indices = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )[:self.k]

        results = []

        for idx in ranked_indices:
            result = self.documents[idx].copy()
            result["bm25_score"] = float(scores[idx])
            results.append(result)

        logger.info(f"BM25 search returned {len(results)} results")
        return results


if __name__ == "__main__":
    retriever = BM25Retriever(k=3)

    query = input("Ask AgriAssist: ")

    results = retriever.search(query)

    print("\nTop BM25 Results:\n")

    for i, result in enumerate(results, start=1):
        print("=" * 60)
        print(f"Result {i}")
        print("BM25 Score:", result.get("bm25_score"))
        print("Text:")
        print(result.get("text", "")[:500])
        print("\nMetadata:")
        print(result.get("metadata", {}))