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
            print('[crawling...] ' + url)
            s = BeautifulSoup(requests.get(url, cookies={'over18': '1'}).text, 'html.parser')
            if s.select('span.article-meta-value'):
                author = s.select('span.article-meta-value')[0].text
                board = s.select('span.article-meta-value')[1].text
                head = s.select('span.article-meta-value')[2].text
                date = s.select('span.article-meta-value')[3].text
                text = s.select('#main-content')[0].text
                crawler_list.append(WebCrawler(author, board, head, date, text, url))

        return crawler_list

def main():
    board = input('Input the board name: ')
    crawler = WebCrawler.ptt_crawler(board)
    count = 0
    for item in crawler:
        print('[' + str(count) + '] ' + item.head)
        count += 1

    while 1:
        choice = input('input a list number to get detail information or input q to quit: ')
        if choice == 'q':
            break
        else:
            index = int(choice)
            print(crawler[index].url)
            print(crawler[index].board)
            print(crawler[index].author)
            print(crawler[index].head)
            print(crawler[index].date)
            print(crawler[index].text)


if __name__ == '__main__':
    main()
