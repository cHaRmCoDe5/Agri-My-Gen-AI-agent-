from backend.retrieval.semantic import SemanticRetriever
from backend.retrieval.bm25 import BM25Retriever
from backend.retrieval.rrf import reciprocal_rank_fusion
from backend.utils.logger import get_logger

logger = get_logger("HybridRetriever")


class HybridRetriever:
    def __init__(self, k=3):
        self.k = k
        self.semantic = SemanticRetriever(k=k)
        self.bm25 = BM25Retriever(k=k)

    def search(self, query: str):
        semantic_results = self.semantic.search(query)
        bm25_results = self.bm25.search(query)

        fused_results = reciprocal_rank_fusion(
            [semantic_results, bm25_results]
        )

        final_results = fused_results[: self.k]

        logger.info(f"Hybrid search returned {len(final_results)} results")
        return final_results


if __name__ == "__main__":
    retriever = HybridRetriever(k=3)

    query = input("Ask AgriAssist: ")

    results = retriever.search(query)

    print("\nTop Hybrid Results:\n")

    for i, result in enumerate(results, start=1):
        print("=" * 60)
        print(f"Result {i}")
        print("Text:")
        print(result.get("text", "")[:700])
        print("\nMetadata:")
        print(result.get("metadata", {}))