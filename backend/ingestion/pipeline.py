import os
from langchain_core.documents import Document

from backend.ingestion.parser import parse_html
from backend.ingestion.cleaner import clean_raw_text

RAW_HTML_DIR = "data/raw_html/pages"


def run_ingestion():
    print("Starting multi-page ingestion...")

    documents = []

    for filename in os.listdir(RAW_HTML_DIR):

        if not filename.endswith(".html"):
            continue

        path = os.path.join(RAW_HTML_DIR, filename)

        with open(path, "r", encoding="utf-8") as f:
            html = f.read()

        raw_text = parse_html(html)
        clean_text = clean_raw_text(raw_text)

        if len(clean_text) < 10:
            continue

        doc = Document(
            page_content=clean_text,
            metadata={
                "source_file": filename,
                "source": "https://www.doa.gov.my",
                "length": len(clean_text),
            },
        )

        documents.append(doc)

    print(f"Created {len(documents)} documents")
    return documents


# --------------------------------------------------
# Compatibility for test_faiss.py and test_rag.py
# --------------------------------------------------
def run():
    return run_ingestion()


if __name__ == "__main__":
    docs = run()

    for doc in docs[:5]:
        print("\n--- DOCUMENT ---")
        print(doc.page_content[:500])
        print(doc.metadata)