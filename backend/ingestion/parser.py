from bs4 import BeautifulSoup


def parse_html(html: str):
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style", "noscript", "form", "input", "button"]):
        tag.decompose()

    content = (
        soup.find("div", id="page_content")
        or soup.find("div", id="container_content")
        or soup.find("table", class_="cms_content")
    )

    if not content:
        return ""

    text = content.get_text(separator=" ", strip=True)
    return text