def build_prompt(question, results):
    context = ""

    for r in results:
        context += r["text"] + "\n\n"

    prompt = f"""
You are an agricultural assistant for Malaysia (DOA system).

Use the context below to answer the question.

Context:
{context}

Question:
{question}

Answer clearly and concisely:
"""
    return prompt