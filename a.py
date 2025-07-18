import requests
from bs4 import BeautifulSoup

# Step 1: 最新話数を取得
api_url = "https://api.syosetu.com/novelapi/api/?ncode=n2267be&out=json"
api_res = requests.get(api_url).json()
latest_no = api_res[1].get("general_all_no")

# Step 2: 最新話ページURLを生成
latest_url = f"https://ncode.syosetu.com/n2267be/{latest_no}/"

# Step 3: 最新話HTMLからタイトル取得
headers = {"User-Agent": "Mozilla/5.0"}
html_res = requests.get(latest_url, headers=headers)
soup = BeautifulSoup(html_res.text, "html.parser")

title_tag = soup.find("title")
if title_tag and " - " in title_tag.text:
    latest_title = title_tag.text.split(" - ")[-1].strip()
    print("✅ 最新話タイトル:", latest_title)
else:
    print("❌ タイトル取得失敗")
