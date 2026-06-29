from backend.embeddings.embedder import Embedder
from backend.vectorstore.faiss_store import FAISSStore
from backend.rag.prompt_builder import build_prompt
from backend.rag.answer_generator import generate_answer

class RAGPipeline:
    def __init__(self):
        self.embedder = Embedder()
        self.vectorstore = FAISSStore()

    def ask(self, question: str):
        print("\n🔍 Processing question:", question)

        # 1. Convert question → vector
        query_vector = self.embedder.embed_text(question)

        # 2. Retrieve similar documents
        results = self.vectorstore.search(query_vector, k=3)

        # 3. Build prompt
        prompt = build_prompt(question, results)

        # 4. Generate answer
        answer = generate_answer(prompt)

        return answer