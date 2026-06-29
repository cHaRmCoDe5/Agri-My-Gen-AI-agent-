def extract_metadata(url, text):
    return {
        "source": url,
        "length": len(text)
    }