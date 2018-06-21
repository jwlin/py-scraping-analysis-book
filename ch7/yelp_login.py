import requests
from bs4 import BeautifulSoup

# 創建 session 物件
s = requests.session()

# 先瀏覽網頁, 取得 csrf token
resp = s.get('https://www.yelp.com/login')
soup = BeautifulSoup(resp.text, 'html5lib')
csrf = soup.find('form', id='ajax-login').find('input', 'csrftok')['value']

# 傳送表單資料並登入
form_data = {
    'email': '[你的 Yelp 帳號]',
    'password': '[你的 Yelp 密碼]',
    'csrftok': csrf
}
resp = s.post('https://www.yelp.com/login', data=form_data)

# 登入成功後，相關資訊皆保留在 session 物件中，可以直接索取相關網頁資訊
resp = s.get('https://www.yelp.com/user_details')

# 確認我的列表餐廳有出現，表示成功取得需要登入才能瀏覽的頁面
# 此處請代換 'The Front Porch' 為你自己的 Yelp 頁面餐廳
print('The Front Porch' in resp.text)

