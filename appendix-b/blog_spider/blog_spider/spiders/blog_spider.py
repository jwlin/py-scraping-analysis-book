from scrapy.spiders import Spider
from bs4 import BeautifulSoup

class BlogSpider(Spider):
    name = 'blog_spider'
    start_urls = ['http://blog.castman.net/web-crawler-tutorial/ch1/connect.html']
    
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1').text
        content = soup.find('p').text
        print(title)
        print(content)
        yield {
            'title': title,
            'content': content
        }