import requests

url = "https://www.doa.gov.my/index.php/pages/view/1053?mid=12"

headers = {"User-Agent": "Mozilla/5.0"}

html = requests.get(url, headers=headers, timeout=30).text

keywords = [
    "Program",
    "Skim",
    "Pertanian",
    "Pembangunan",
    "Insentif",
    "Bantuan",
    "Projek",
]

for keyword in keywords:
    print("=" * 80)
    print("KEYWORD:", keyword)
    index = html.lower().find(keyword.lower())

    if index == -1:
        print("Not found")
    else:
        print(html[index:index + 1500])