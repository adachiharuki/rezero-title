from flask import Flask
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

@app.route("/")

def rezero():
    try:
        # 最新話数を取得
        api_url = "https://api.syosetu.com/novelapi/api/?ncode=n2267be&out=json"
        api_res = requests.get(api_url, timeout=10).json()
        latest_no = api_res[1].get("general_all_no")

        # 最新話ページ
        latest_url = f"https://ncode.syosetu.com/n2267be/{latest_no}/"
        headers = {"User-Agent": "Mozilla/5.0"}
        html_res = requests.get(latest_url, headers=headers, timeout=10)

        soup = BeautifulSoup(html_res.text, "html.parser")
        title_tag = soup.find("title")

        if title_tag and " - " in title_tag.text:
            latest_title = title_tag.text.split(" - ")[-1].strip()
            return latest_title
        else:
            return "❌ タイトル形式不明", 500

    except Exception as e:
        return f"❌ エラー: {str(e)}", 500



if __name__ == "__main__":
    app.run(debug=True)
