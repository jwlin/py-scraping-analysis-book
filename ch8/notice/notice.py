import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText


def check_price(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    words = list(soup.find('div', 'product-price-detail').stripped_strings)
    print(words)
    # e.g., ['$1,529', '$26 / 1粒', '(含運)']
    #       ['商品原價', '$1,529', '商品折扣', '-', '$240', '小計', '$1,289', '$22 / 1粒', '(含運)']
    prices = [w for w in words if '$' in w]
    return '折扣' in ' '.join(words), prices[-2]


def send_mail(price):
    EMAIL = '你的 Email 信箱'
    PWD = '你的 Email 密碼'

    sender = to = EMAIL
    subject = '益節價格 {}'.format(str(price))
    body = 'https://www.costco.com.tw/Health-Beauty/Vitamins-Herbals-Dietary-Supplements/Glucosamine-Joint-Supplements/Move-Free-Ultra-60-Tablets/p/363985'
    msg = MIMEText(body.encode('utf-8'), _charset='utf-8')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(EMAIL, PWD)
        server.sendmail(sender, to, msg.as_string())
        server.close()
        print('Email 已寄出')
    except Exception as e:  
        print('Email 寄送失敗')
        print(e)
    

if __name__ == '__main__':
    urls = [
        'https://jwlin.github.io/py-scraping-analysis-book/ch8/move-free-normal.html',  # 普通網頁
        'https://jwlin.github.io/py-scraping-analysis-book/ch8/move-free-discount.html'  # 折扣網頁
    ]
    print(check_price(urls[0]))
    print(check_price(urls[1]))
    #is_discount, price = check_price(urls[1])
    #if is_discount:
    #    send_mail(price)
