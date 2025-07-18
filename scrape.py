import requests
from bs4 import BeautifulSoup
import re

ATOM_URL = "https://api.syosetu.com/writernovel/235132.Atom"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(ATOM_URL, headers=headers)
print("ステータスコード:", response.status_code)

soup = BeautifulSoup(response.text, "xml")
entries = soup.find_all("entry")

latest_entry = sorted(entries, key=lambda e: e.updated.text, reverse=True)[0]
raw_title = latest_entry.title.text.strip()

match = re.search(r"\[(.*?)\]\(エピソード\d+\)", raw_title)
if not match:
    print("❌ タイトル形式不明")
    with open("latest.txt", "w", encoding="utf-8") as f:
        f.write("❌ タイトル形式不明")
    exit()

full_inner_title = match.group(1)
prefix_removed = re.sub(r"^Ｒｅ：ゼロから始める異世界生活[-ー─]{0,1}", "", full_inner_title).strip()

print("✅ 最新話タイトル:", prefix_removed)
with open("latest.txt", "w", encoding="utf-8") as f:
    f.write(prefix_removed)
