# from argparse import ArgumentParser
from get_data import PcstoreCrawler

if __name__ == '__main__':
    # parser = ArgumentParser()
    # parser.add_argument("search")
    # args = parser.parse_args()
    # crawler.raw_text = args.search
    crawler = PcstoreCrawler()
    crawler.raw_text = "搜尋關鍵字"
    print("正在搜尋", crawler.raw_text, "......")
    titles = crawler.get_title()
    for title in titles:
        print(title)
