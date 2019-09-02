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
    # 利用 regex 找出所有 'NormalPostLayout__Left' 開頭的 div
    for div in soup.find_all('div', re.compile('NormalPostLayout__Left.+')):
        lower_divs = div.find_all('div')
        actions = lower_divs[2].text.strip()
        nums = re.findall(r"\d+", actions)
        articles.append({
            'title': lower_divs[0].text.strip(),
            'excerpt': lower_divs[1].text.strip(),
            'bookmark': nums[1],
            'response': nums[0],
            'href': div.parent.parent.parent['href']
        })

    print('共 %d 篇' % (len(articles)))
    for a in articles[:3]:
        print(a)


if __name__ == '__main__':
    main()