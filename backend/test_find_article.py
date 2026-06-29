from bs4 import BeautifulSoup

with open(
    "data/raw_html/pages/004_Latar_Belakang_dan_Sejarah.html",
    "r",
    encoding="utf-8"
) as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

keyword = "Latar Belakang"

print("=" * 80)

found = False

for tag in soup.find_all(True):

    text = tag.get_text(" ", strip=True)

    if keyword in text:

        found = True

        print("TAG :", tag.name)
        print("ID  :", tag.get("id"))
        print("CLASS :", tag.get("class"))
        print("-" * 80)
        print(text[:1200])
        print("=" * 80)

if not found:
    print("Keyword not found.")