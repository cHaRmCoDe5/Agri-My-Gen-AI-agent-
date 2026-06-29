import faiss
import numpy as np
import pickle
import os

from backend.utils.logger import get_logger

logger = get_logger("FAISS")


class FAISSStore:
    def __init__(self, dim=1536, index_path="data/vectorstore/faiss.index"):
        self.dim = dim
        self.index_path = index_path

        self.index = faiss.IndexFlatL2(dim)
        self.metadata = []

        # Load existing index if available
        if os.path.exists(index_path):
            self.load()

    def add_vectors(self, vectors):
        embeddings = []

        for item in vectors:
            embeddings.append(item["vector"])
            self.metadata.append({
                "text": item["text"],
                "metadata": item["metadata"]
            })

        embeddings = np.array(embeddings).astype("float32")

        self.index.add(embeddings)

        logger.info(f"Added {len(vectors)} vectors to FAISS")

    def search(self, query_vector, k=3):
        query_vector = np.array([query_vector]).astype("float32")

        distances, indices = self.index.search(query_vector, k)

        results = []

        for idx in indices[0]:
            if idx < len(self.metadata):
                results.append(self.metadata[idx])

        return results

    def save(self):
        faiss.write_index(self.index, self.index_path)

        with open(self.index_path + ".meta", "wb") as f:
            pickle.dump(self.metadata, f)

        logger.info("FAISS index saved successfully")

    def load(self):
        self.index = faiss.read_index(self.index_path)

        with open(self.index_path + ".meta", "rb") as f:
            self.metadata = pickle.load(f)

        logger.info("FAISS index loaded successfully")