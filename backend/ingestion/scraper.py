import json
import os
import re
import time
import requests

INPUT_FILE = "data/raw_html/urls.json"
OUTPUT_DIR = "data/raw_html/pages"


def safe_filename(title: str, index: int) -> str:
    title = title.strip() or f"page_{index}"
    title = re.sub(r"[^a-zA-Z0-9_-]+", "_", title)
    return f"{index:03d}_{title[:60]}.html"


def scrape_page(url: str) -> str:
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    return response.text


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        links = json.load(f)

    print(f"Scraping {len(links)} pages...")

    for i, item in enumerate(links, start=1):
        title = item.get("title", "")
        url = item.get("url", "")

        try:
            html = scrape_page(url)
            filename = safe_filename(title, i)
            path = os.path.join(OUTPUT_DIR, filename)

            with open(path, "w", encoding="utf-8") as f:
                f.write(html)

            print(f"[{i}] Saved: {filename}")

            time.sleep(1)

        except Exception as e:
            print(f"[{i}] Failed: {url}")
            print(e)


if __name__ == "__main__":
    main()