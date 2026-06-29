from backend.rag.pipeline import RAGPipeline

rag = RAGPipeline()

while True:
    q = input("\nAsk AgriAssist (type 'exit'): ")

    if q.lower() == "exit":
        break

    answer = rag.ask(q)

    print("\n🤖 Answer:\n", answer)