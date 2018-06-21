import requests
from bs4 import BeautifulSoup

# 未附加 User-Agent header, 回傳錯誤訊息
#resp = requests.get('https://www.kingstone.com.tw/book/book_page.asp?kmcode=2011771147021')
#print(resp.text)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/66.0.3359.181 Safari/537.36'}
resp = requests.get('https://www.kingstone.com.tw/book/book_page.asp?kmcode=2011771147021', headers=headers)
soup = BeautifulSoup(resp.text, 'html.parser')
for li in soup.find('ul', 'item_list').find_all('li'):
    print(li.text.strip())