import requests
import re
from bs4 import BeautifulSoup


def main():
    URL = 'https://www.dcard.tw/f'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    resp = requests.get(URL, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')

    articles = []
    # 利用 regex 找出所有 'PostList_wrapper_' 開頭的 div
    for div in soup.find_all('div', re.compile('PostEntry_content_\w{5}')):
        articles.append(
            {'title': div.h3.text.strip(),
             'excerpt': div.find_all('div')[0].text.strip(),
             'bookmark': re.findall(r'\d+', div.find_all('div')[1].text.strip())[0],
             'response': re.findall(r'\d+', div.find_all('div')[1].text.strip())[1],
             'href': div.parent.parent['href']
            }
        )

    print('共 %d 篇' % (len(articles)))
    for a in articles[:3]:
        print(a)


if __name__ == '__main__':
    main()