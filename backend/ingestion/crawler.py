import json
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

START_URL = "https://www.doa.gov.my/index.php/pages/view/1053?mid=12"
BASE_URL = "https://www.doa.gov.my"
OUTPUT_FILE = "data/raw_html/urls.json"


def fetch_html(url: str) -> str:
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    return response.text


def extract_doa_links(html: str):
    soup = BeautifulSoup(html, "html.parser")

    links = []

    for a in soup.find_all("a", href=True):
        href = a["href"]
        title = a.get_text(" ", strip=True)

        if "/index.php/pages/view/" in href:
            full_url = urljoin(BASE_URL, href)

            links.append({
                "title": title,
                "url": full_url
            })

    # remove duplicates
    unique = {}
    for item in links:
        if item["url"] not in unique:
            unique[item["url"]] = item

    return list(unique.values())


def save_links(links):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(links, f, ensure_ascii=False, indent=2)


def main():
    html = fetch_html(START_URL)
    links = extract_doa_links(html)
    save_links(links)

    print(f"Found {len(links)} DOA page links")
    print(f"Saved to {OUTPUT_FILE}")

    for item in links[:20]:
        print("-", item["title"], "=>", item["url"])


if __name__ == "__main__":
    main()