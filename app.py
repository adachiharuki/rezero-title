from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/rezero")
def rezero():
    url = "https://ncode.syosetu.com/n2267be/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    title_tag = soup.find("title")
    if not title_tag:
        return "❌ タイトル取得失敗", 500

    full_title = title_tag.text.strip()
    if " - " in full_title:
        latest = full_title.split(" - ")[-1]
        return latest
    else:
        return "❌ タイトル形式不明", 500
    

    
