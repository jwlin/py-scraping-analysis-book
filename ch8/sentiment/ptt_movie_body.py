import csv
import requests
import re
import json
import time
from bs4 import BeautifulSoup


PTT_URL = 'https://www.ptt.cc'


def sanitize(txt):
    # 保留英數字, 中文 (\u4e00-\u9fa5) 及中文標點, 部分特殊符號
    # http://ubuntu-rubyonrails.blogspot.com/2009/06/unicode.html
    expr = re.compile('[^\u4e00-\u9fa5。；，：“”（）、？「」『』【】\s\w:/\-.()]')  # ^ 表示"非括號內指定的字元"
    txt = re.sub(expr, '', txt)
    txt = re.sub('[。；，：“”（）、？「」『』【】:/\-_.()]', ' ', txt)  # 用空白取代中英文標點
    txt = re.sub('(\s)+', ' ', txt)  # 用單一空白取代多個換行或 tab 符號
    txt = txt.replace('--', '')
    txt = txt.lower()  # 英文字轉為小寫
    return txt


def get_post(url):
    resp = requests.get(
        url=url,
        cookies={'over18': '1'}  # 告知 Server 已回答過滿 18 歲的問題
    )
    soup = BeautifulSoup(resp.text, 'html5lib')
    main_content = soup.find('div', id='main-content')

    # 把非本文的部份 (標題區及推文區) 移除
    # 移除標題區塊
    for meta in main_content.find_all('div', 'article-metaline'):
        meta.extract()
    for meta in main_content.find_all('div', 'article-metaline-right'):
        meta.extract()
    # 移除推文區塊
    for push in main_content.find_all('div', 'push'):
        push.extract()

    parsed = []
    for txt in main_content.stripped_strings:
        # 移除 '※ 發信站:', '--' 開頭, 及本文區最後一行文章網址部份
        if txt[0] == '※' or txt[:2] == '--' or url in txt:
            continue
        txt = sanitize(txt)
        if txt:
            parsed.append(txt)
    return ' '.join(parsed)


def get_article_body(csv_file):
    id_to_body = {}
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print('處理', row['title'], row['href'])
            title = ' '.join(row['title'].split(']')[1:])
            title = sanitize(title)
            body = get_post(PTT_URL + row['href'])
            id_to_body[row['href']] = title + ' ' + body  # 以文章超連結為 key, 標題 + 本文為 value
            time.sleep(1)  # 放慢爬蟲速度
    return id_to_body


if __name__ == '__main__':
    d1 = get_article_body('mov_pos.csv')
    d2 = get_article_body('mov_neg.csv')
    id_to_body = {**d1, **d2}  # 將兩個 dict 合併為一個
    with open('id_to_body.json', 'w', encoding='utf-8') as f:
        json.dump(id_to_body, f, indent=2, ensure_ascii=False)