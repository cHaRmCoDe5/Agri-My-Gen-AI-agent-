from backend.utils.logger import get_logger

logger = get_logger("RRF")


def reciprocal_rank_fusion(result_lists, k=60):
    """
    Combine multiple ranked result lists using Reciprocal Rank Fusion.
    """

    scores = {}
    items = {}

    for results in result_lists:
        for rank, item in enumerate(results, start=1):
            text = item.get("text", "")

            if not text:
                continue

            if text not in scores:
                scores[text] = 0
                items[text] = item

            scores[text] += 1 / (k + rank)

    fused_results = sorted(
        items.values(),
        key=lambda item: scores[item.get("text", "")],
        reverse=True
    )

    logger.info(f"RRF fused {len(fused_results)} results")

    return fused_results


if __name__ == "__main__":
    list1 = [
        {"text": "Agro scheme for farmers", "metadata": {"source": "semantic"}},
        {"text": "Farming support programme", "metadata": {"source": "semantic"}},
    ]

    list2 = [
        {"text": "Farming support programme", "metadata": {"source": "bm25"}},
        {"text": "Agriculture grant information", "metadata": {"source": "bm25"}},
    ]

    results = reciprocal_rank_fusion([list1, list2])

    for i, result in enumerate(results, start=1):
        print(f"{i}. {result['text']}")