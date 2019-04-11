from get_data import PcstoreCrawler
import sys

if __name__ == '__main__':
    crawler = PcstoreCrawler()
    while True:
        crawler.raw_text = input("請輸入關鍵字 ( 輸入exit結束 )：")
        if crawler.raw_text == "exit":
            break
        print("正在搜尋", crawler.raw_text, "......")
        titles = crawler.get_title()
        for title in titles:
            print(title.encode(sys.stdin.encoding, "ignore").decode(sys.stdin.encoding), "\n")

