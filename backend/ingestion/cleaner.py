import re

REMOVE_KEYWORDS = [
    "Portal Rasmi",
    "JABATAN PERTANIAN",
    "KEMENTERIAN PERTANIAN",
    "Carian Terperinci",
    "SOALAN LAZIM",
    "MAKLUM BALAS",
    "HUBUNGI KAMI",
    "PETA LAMAN",
    "Laman Utama",
    "Info Jabatan",
]


def clean_raw_text(text: str) -> str:
    if not text:
        return ""

    text = re.sub(r"\s+", " ", text)

    for keyword in REMOVE_KEYWORDS:
        text = text.replace(keyword, "")

    text = re.sub(r"\bT\b", "", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()