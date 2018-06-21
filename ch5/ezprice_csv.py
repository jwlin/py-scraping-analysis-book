import requests
import csv
import re
from bs4 import BeautifulSoup


if __name__ == '__main__':
    query = 'ps4主機'
    page = requests.get('https://ezprice.com.tw/s/' + query).text
    soup = BeautifulSoup(page, 'html5lib')
    items = list()
    for div in soup.find_all('div', 'search-rst clearfix'):
        item = list()
        item.append(div.h3.a.text.strip())  # 商品名稱
        # 先取得價格字串，再移除其中的非數字部份(以空白字串取代非0-9的字元)
        price = div.find('span', 'num').text
        price = re.sub(r'[^0-9]', '', price)
        item.append(price)
        # 若商家區塊存在則取出商家名稱
        if div.find('span', 'platform-name'):
            item.append(div.find('span', 'platform-name').text.strip())
        else:
            item.append('無')
        items.append(item)
    print('共 %d 項商品' % (len(items)))
    for item in items:
        print(item)

    # with open('ezprice.csv', 'wb') as f:
    #     f.write(b'\xEF\xBB\xBF')  # 在檔頭加上 UTF-8 編碼的 BOM
    # 或用 encoding='utf_8_sig'

    with open('ezprice.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(('品項', '價格', '商家'))
        for item in items:
            writer.writerow((column for column in item))
    '''
    print('讀取 csv 檔')
    with open('ezprice.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row['品項'], row['價格'], row['商家'])
    '''
