from langchain_core.documents import Document

def build_document(text, metadata):
    return Document(
        page_content=text,
        metadata=metadata
    )