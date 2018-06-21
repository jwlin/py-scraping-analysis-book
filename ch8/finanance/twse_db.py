import requests
import datetime
import sqlite3
import time

db_name = 'data.sqlite3'


def str_to_num(s, c_type):
    # 將字串 s 移除逗點與句點後轉為 float/int
    # 若非 float 或 int 則不處理, 直接回傳
    if c_type not in ['float', 'int']:
        return s
    s = s.replace(',', '')
    try:
        if c_type == 'int':
            return int(s)
        else:  # c_type == 'float':
            return float(s)
    except:  # 轉換失敗則回傳 -1
        return -1


def crawl_price(date):
    # 將 datetime 物件字串化為 YYYYMMDD 格式
    datestr = date.strftime('%Y%m%d')

    # 從證交所網站上獲取指定日期的所有個股資訊
    resp = requests.get('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date='
                         + datestr + '&type=ALLBUT0999')
    data = resp.json()
    if 'data5' not in data:  # 當天沒有資料, 可能為假日
        return None

    # 欄位定義：
    # ['證券代號', '日期(新增)', '成交股數', '成交筆數', '成交金額', '開盤價', '最高價', '最低價', '收盤價', '漲跌價差',
    #  '最後揭示買價', '最後揭示買量', '最後揭示賣價', '最後揭示賣量', '本益比']
    types = ['text', 'datetime', 'int', 'int', 'int', 'float', 'float', 'float', 'float', 'float',
             'float', 'int', 'float', 'int', 'float']

    prices = []
    for item in data['data5']:
        if item[2] == '0':  # 忽略成交股數為 0 的資料列
            continue
        # 第 2 欄 (證券名稱) 及第 10 欄 ('漲跌(+/-)', 為 HTML 碼) 不需要, 故移除之
        filtered = item[:1] + item[2:9] + item[10:]
        # 插入日期欄位到第 2 欄
        filtered = filtered[:1] + [date.strftime('%Y-%m-%d')] + filtered[1:]
        prices.append([str_to_num(s, types[i]) for i, s in enumerate(filtered)])

    return prices


def bulk_insert(fname, bulk_data):
    conn = sqlite3.connect(fname)
    c = conn.cursor()
    c.execute('BEGIN TRANSACTION')
    for d in bulk_data:
        values = ["'" + str(e) + "'" for e in d]
        cmd = 'INSERT OR REPLACE INTO daily_price VALUES({})'.format(','.join(values))
        #print(cmd)
        c.execute(cmd)
    c.execute('COMMIT')
    conn.close()


def get_date_range_from_db(fname):
    conn = sqlite3.connect(fname)
    c = conn.cursor()
    c.execute('select * from daily_price order by 日期 ASC LIMIT 1;')
    date_from = datetime.datetime.strptime(list(c)[0][1], '%Y-%m-%d')
    c.execute('select * from daily_price order by 日期 DESC LIMIT 1;')
    date_to = datetime.datetime.strptime(list(c)[0][1], '%Y-%m-%d')
    conn.close()
    return date_from, date_to


def update_db(date_from, date_to):
    print('更新資料: {} 到 {}'.format(date_from.strftime('%Y-%m-%d'), date_to.strftime('%Y-%m-%d')))
    current = date_from
    while current <= date_to:
        prices = crawl_price(current)
        if prices:
            bulk_insert(db_name, prices)
            print(current.strftime('%Y-%m-%d'), '... 成功')
        else:
            print(current.strftime('%Y-%m-%d'), '... 失敗 (可能為假日)')
        current += datetime.timedelta(days=1)
        time.sleep(3)  # 放慢爬蟲速度


if __name__ == '__main__':
    db_from, db_to = get_date_range_from_db(db_name)
    print('資料庫日期: {} 到 {}'.format(db_from.strftime('%Y-%m-%d'), db_to.strftime('%Y-%m-%d')))
    #date_from = db_to + datetime.timedelta(days=1)
    #date_to = datetime.datetime.today()
    #update_db(date_from, date_to)
