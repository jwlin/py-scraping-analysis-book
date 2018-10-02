# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html



import sqlite3

class BooksSpiderPipeline(object):
    def open_spider(self, spider):
        self.conn = sqlite3.connect ("books.sqlite") 
        self.cur = self.conn.cursor() 
        self.cur.execute("CREATE TABLE if not exists books(title TEXT, author TEXT, price INTEGER)")
        
    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()
        
    def process_item(self, item, spider):
        title = item['title']
        author = ', '.join(item['author'])
        price = item['price']
        self.cur.execute('''INSERT INTO books(title, author, price) VALUES(?,?,?)''', (title, author, price))
        return item