import sqlite3


db_name = 'data.sqlite3'


def get_data(fname, stock_id, period):
    conn = sqlite3.connect(fname)
    c = conn.cursor()
    cmd = 'SELECT 日期, 收盤價 FROM daily_price WHERE 證券代號 = "{:s}" ORDER BY 日期 DESC LIMIT {:d};'.format(stock_id, period)
    c.execute(cmd)
    rows = c.fetchall()
    rows.reverse()
    conn.close()
    return rows


def calc_rsv(prices):
    # 採用常見的 "9, 3, 3" 方式計算 KD 值
    # (http://yhhuang1966.blogspot.com/2015/02/kd.html)
    # (http://www.cmoney.tw/notes/note-detail.aspx?nid=6460)
    window = prices[:8]  # 前 8 天股價
    # 因不足 9 天，前 8 天的最高點、最低點、及 RSV 值皆為0; 第八天的 K 值 = D 值 = 50
    highest = [0]*8
    lowest = [0]*8
    rsv_values = [0]*8
    k_values = [0]*7 + [50]
    d_values = [0]*7 + [50]
    for i, p in enumerate(prices[8:]):  # 從第 9 天開始計算 RSV 及 KD 值
        window.append(p)
        window = window[len(window)-9:]  # 計算範圍為最近 9 天
        high = max(window)
        low = min(window)
        rsv = 100 * ((p - low) / (high - low))
        k = ((1/3)*rsv) + ((2/3)*k_values[i-1])
        d = ((1/3)*k) + ((2/3)*d_values[i-1])
        highest.append(high)
        lowest.append(low)
        rsv_values.append(rsv)
        k_values.append(k)
        d_values.append(d)
    return k_values, d_values


def get_buy_signal(k_values, d_values):
    buy = [0]*8  # 前 8 天沒有資料故無買進訊號
    for i in range(8, len(k_values)):
        # 策略: KD 黃金交叉 (前一天 k < d 且今天 k > d) 且在低檔 (30)
        # (http://www.cmoney.tw/app/ItemContent.aspx?id=2739)
        if k_values[i-1] < d_values[i-1] and k_values[i] > d_values[i] and k_values[i] < 30:
            buy.append(1)
        else:
            buy.append(0)
    return buy


if __name__ == '__main__':
    price_data = get_data(db_name, '0050', 260)
    dates = [d[0] for d in price_data]
    prices = [d[1] for d in price_data]
    print('起始日期: {} (收盤價: {}), 結束日期: {} (收盤價: {}) ({} 天)'.format(
        dates[0], prices[0], dates[-1], prices[-1], len(dates)))
    k, d = calc_rsv(prices)
    buy = get_buy_signal(k, d)
    print('本金 10 萬元. 期間有 {} 次買進訊號, 一次投入 1 萬元'.format(sum(buy)))
    profit = [10]
    ratios = [1] + [prices[i] / prices[i - 1] for i in range(1, len(prices))]
    # 因為買進訊號是根據當天盤後價格計算, 隔天才能真正加碼, 故將買進訊號往右平移一天當作當天加碼 1 萬元
    buy = [0] + buy[:-1]
    for b, r in zip(buy[1:], ratios[1:]):
        profit.append(profit[-1] * r + b)
    print('回測結果: {}'.format(profit[-1]))
    interest_rate = 0.011 * (260/365)
    total = 10 + sum(buy)
    print('{} 萬元定存結果 (利率 1.1%): {}'.format(total, total*(1+interest_rate)))
