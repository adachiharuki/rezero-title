from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/rezero")
def rezero():
    try:
        # APIから最新話数を取得
        api_url = "https://api.syosetu.com/novelapi/api/?ncode=n2267be&out=json"
        api_res = requests.get(api_url, timeout=10).json()
        latest_no = api_res[1]["general_all_no"]

        # 最新話URL
        latest_url = f"https://ncode.syosetu.com/n2267be/{latest_no}/"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(latest_url, headers=headers, timeout=10)
        html = res.text

        # BeautifulSoupで<title>タグを抽出
        soup = BeautifulSoup(html, "html.parser")
        title_tag = soup.find("title")
        if not title_tag:
            return "❌ タイトル取得失敗", 500

        full_title = title_tag.text.strip()

        # 「 - 」で区切られていれば話タイトルのみを返す
        if " - " in full_title:
            return full_title.split(" - ")[-1].strip()
        else:
            return "❌ タイトル形式不明", 500

    except Exception as e:
        return f"❌ エラー: {str(e)}", 500
