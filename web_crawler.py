import requests
from bs4 import BeautifulSoup


class WebCrawler(object):
    """docstring for Crawler"""
    def __init__(self, author, board, head, date, text, url):
        self.date = date
        self.author = author
        self.head = head
        self.text = text
        self.url = url
        self.board = board

    def ptt_crawler(board):
        main_url = 'https://www.ptt.cc/bbs/' + board + '/index.html'
        s = BeautifulSoup(requests.get(main_url, cookies={'over18': '1'}).text, 'html.parser')
        title_list = s.select('div.title > a')
        url_list = []
        crawler_list = []
        for title in title_list:
            url_list.append('https://www.ptt.cc' + title.get('href'))
        for url in url_list:
            s = BeautifulSoup(requests.get(url, cookies={'over18': '1'}).text, 'html.parser')
            value = s.select('article-meta-value')
            author = value[0].text
            board = value[1].text
            head = value[2].text
            date = value[3].text


def main():
    board = input('Input the board name: ')
    print(board)
    WebCrawler.ptt_crawler(board)


if __name__ == '__main__':
    main()
