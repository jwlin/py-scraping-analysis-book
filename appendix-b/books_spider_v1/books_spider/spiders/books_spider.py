from scrapy.spiders import Spider
from bs4 import BeautifulSoup
from books_spider.items import BookItem

class BooksSpider(Spider):
    name = 'books_spider'
    start_urls = ['http://search.books.com.tw/search/query/cat/all/key/python/sort/1/page/1/v/0/']
    
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all('li', {'class': 'item'})
        
        for book in books:
            book_item = BookItem()
            title = book.a['title']
            authors = []
            for author in book.find_all('a', {'rel': 'go_author'  }):
                authors.append(author.text)
            price = book.find('span', {'class': 'price'})('strong')[-1].b.text
            
            book_item['title'] = title
            book_item['author'] = authors
            book_item['price'] = price
            yield book_item