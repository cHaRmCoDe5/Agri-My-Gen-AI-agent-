from bs4 import BeautifulSoup

with open(
    "data/raw_html/pages/004_Latar_Belakang_dan_Sejarah.html",
    "r",
    encoding="utf-8"
) as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

print("=" * 80)
print("TITLE")
print("=" * 80)
print(soup.title)

print("\n" + "=" * 80)
print("MAIN")
print("=" * 80)
print(soup.find("main"))

print("\n" + "=" * 80)
print("ARTICLE")
print("=" * 80)
print(soup.find("article"))

print("\n" + "=" * 80)
print("DIV id='content'")
print("=" * 80)
print(soup.find("div", id="content"))

print("\n" + "=" * 80)
print("DIV class='content'")
print("=" * 80)
print(soup.find("div", class_="content"))

print("\n" + "=" * 80)
print("DIV class='item-page'")
print("=" * 80)
print(soup.find("div", class_="item-page"))

print("\n" + "=" * 80)
print("DIV class='block-body'")
print("=" * 80)
print(soup.find("div", class_="block-body"))