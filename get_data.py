import sys
import bs4
import requests
from encode_text import pcstore_input_text_convert


class PcstoreCrawler:

    def __init__(self):
        self.base_url_head = "https://www.pcstore.com.tw/adm/psearch.htm?store_k_word="
        self.base_url_tail = "&slt_k_option=1"
        self.raw_text = ""

    def search(self):
        headers = {'User-Agent': 'Mozilla/5.0'}
        search_text = pcstore_input_text_convert(self.raw_text)
        url = self.base_url_head + search_text + self.base_url_tail
        req = requests.post(url, headers)
        req = str(req.content.decode("big5", "ignore"))
        html_res = bs4.BeautifulSoup(req, "html.parser")
        print("從", url, "獲取資料")
        return html_res

    def get_title(self):
        html_res = self.search()
        raw_title = html_res.find_all("div", id="keyad-pro-right3")
        titles = []
        for item in raw_title:
            if item.strong:
                titles.append(item.strong.get_text())
            else:
                titles.append(item.find("div", {"class": "pic2t pic2t_bg"}).get_text())
        if not titles:
            if len(self.raw_text) < 2:
                titles.append("輸入關鍵字太少，請重新輸入。")
            else:
                titles.append("無相關商品，請更換關鍵字。")
        return titles
