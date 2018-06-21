import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    URL = 'https://taqm.epa.gov.tw/taqm/tw/HourlyData.aspx'

    # 先連線一次取得隱藏欄位
    resp = requests.get(URL)
    soup = BeautifulSoup(resp.text, 'html5lib')
    view_state = soup.find(id='__VIEWSTATE')['value']
    event_validation = soup.find(id='__EVENTVALIDATION')['value']
    viewstate_generator = soup.find(id='__VIEWSTATEGENERATOR')['value']

    # 創建查詢欄位並透過 POST 取得資料
    form_data = {
        '__VIEWSTATE': view_state,
        '__VIEWSTATEGENERATOR': viewstate_generator,
        '__EVENTVALIDATION': event_validation,
        'ctl04$lbSite': '41',
        'ctl04$lbParam': '4',
        'ctl04$txtDateS': '2018/06/01',
        'ctl04$txtDateE': '2018/06/10',
        'ctl04$btnQuery': '查詢即時值'
    }
    resp = requests.post(URL, data=form_data)
    soup = BeautifulSoup(resp.text, 'html5lib')
    for tr in soup.find('table', 'TABLE_G').find_all('tr'):
        print([s for s in tr.stripped_strings])
