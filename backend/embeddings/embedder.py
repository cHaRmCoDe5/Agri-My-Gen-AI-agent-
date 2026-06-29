from openai import OpenAI
from backend.utils.logger import get_logger
from backend.config import OPENAI_API_KEY

logger = get_logger("Embedder")


class Embedder:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = "text-embedding-3-small"

    def embed_text(self, text: str):
        response = self.client.embeddings.create(
            model=self.model,
            input=text
        )
        return response.data[0].embedding

    def embed_documents(self, documents):
        vectors = []

        for doc in documents:
            try:
                vector = self.embed_text(doc.page_content)

                vectors.append({
                    "vector": vector,
                    "metadata": doc.metadata,
                    "text": doc.page_content
                })

                logger.info("Embedding created successfully")

            except Exception as e:
                logger.error(f"Embedding failed: {e}")

        return vectors