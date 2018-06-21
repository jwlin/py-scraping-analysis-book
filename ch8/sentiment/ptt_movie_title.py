import requests
import re
import csv
from bs4 import BeautifulSoup


PTT_URL = 'https://www.ptt.cc'


def get_articles(url):
    resp = requests.get(
        url=url,
        cookies={'over18': '1'}  # 告知 Server 已回答過滿 18 歲的問題
    )
    soup = BeautifulSoup(resp.text, 'html5lib')
    prev_link = soup.find('div', 'btn-group-paging').find_all('a')[1]
    # 若 <a> 有 href 屬性, 代表有上一頁的超連結
    prev_link = prev_link['href'] if 'href' in prev_link.attrs else None

    # 巡覽每一篇文章所在區塊
    positive = []
    negative = []
    for div in soup.find_all('div', 'r-ent'):
        href = div.find('div', 'title').a['href']
        title = div.find('div', 'title').text.strip()
        # 若標題為 [] 開頭, e.g., [好雷] 星際大戰八-各種元素集於一身
        if re.match('\[.*\]', title):
            tag = re.match('\[.*\]', title).group(0)
            # 標籤內含'好'為好評; 含'負'或'爛'為負評
            if '好' in tag:
                positive.append([title, href])
            if '爛' in tag or '負' in tag:
                negative.append([title, href])
    return prev_link, positive, negative


if __name__ == '__main__':
    start_url = PTT_URL + '/bbs/movie/search?q=黑豹'
    positive_posts, negative_posts = [], []
    prev_link, pos, neg = get_articles(start_url)
    positive_posts += pos
    negative_posts += neg
    while prev_link:
        url = PTT_URL + prev_link
        prev_link, pos, neg = get_articles(url)
        positive_posts += pos
        negative_posts += neg
    print(len(positive_posts), positive_posts[:3])
    print(len(negative_posts), negative_posts[:3])

    with open('mov_pos.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['title', 'href'])
        writer.writerows(positive_posts)

    with open('mov_neg.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['title', 'href'])
        writer.writerows(negative_posts)
