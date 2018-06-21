import requests
from bs4 import BeautifulSoup


# 網址後方加上 MARKET:STOCK_ID 即為個股資訊. e.g, TPE:2330
G_FINANCE_URL = 'https://www.google.com/search?q='


def get_web_page(url, stock_id):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/66.0.3359.181 Safari/537.36'}
    resp = requests.get(url + stock_id, headers=headers)
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text


def get_stock_info(dom):
    soup = BeautifulSoup(dom, 'html5lib')
    stock = dict()

    sections = soup.find_all('g-card-section')

    # 第 2 個 g-card-section, 取出公司名及即時股價資訊
    stock['name'] = sections[1].div.text
    spans = sections[1].find_all('div', recursive=False)[1].find_all('span', recursive=False)
    stock['current_price'] = spans[0].text
    stock['current_change'] = spans[1].text

    # 第 4 個 g-card-section, 有左右兩個 table 分別存放股票資訊
    for table in sections[3].find_all('table'):
        for tr in table.find_all('tr')[:3]:
            key = tr.find_all('td')[0].text.lower().strip()
            value = tr.find_all('td')[1].text.strip()
            stock[key] = value

    return stock


if __name__ == '__main__':
    page = get_web_page(G_FINANCE_URL, 'TPE:2330')
    if page:
        stock = get_stock_info(page)
        for k, v in stock.items():
            print(k, v)