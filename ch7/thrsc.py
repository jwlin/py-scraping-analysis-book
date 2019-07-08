import requests
from bs4 import BeautifulSoup


URL = 'https://www.thsrc.com.tw/tw/TimeTable/SearchResult'


def get_station_id():
    station_to_id = {}
    resp = requests.get(URL)
    soup = BeautifulSoup(resp.text, 'html5lib')
    for opt in soup.find('select', id='StartStation').find_all('option'):
        if opt['value']:
            station_to_id[opt.text.strip()] = opt['value']
    return station_to_id


def time_table(start_station, end_station, search_date, search_time, rest_time=None, early_or_later=None):
    form_data = {
        'StartStation': start_station,
        'EndStation': end_station,
        'SearchDate': search_date,
        'SearchTime': search_time,
        'SearchWay': 'DepartureInMandarin',
    }
    if rest_time:
        form_data['RestTime'] = rest_time
    if early_or_later:
        form_data['EarlyOrLater'] = early_or_later

    times = []
    resp = requests.post(URL, data=form_data)
    soup = BeautifulSoup(resp.text, 'html5lib')
    for tr in soup.find_all('table', 'touch_table'):
        times.append([s for s in tr.stripped_strings])

    # 取得較早及較晚班次時間
    prev_time = soup.find('a', 'res_prev_btn')['onclick'].split("'")[1]
    next_time = soup.find('a', 'res_next_btn')['onclick'].split("'")[1]

    return times, prev_time, next_time


def get_times(start_station, end_station, search_date, search_time):
    URL = 'https://www.thsrc.com.tw/tw/TimeTable/Search'
    form_data = {
        'StartStationName': start_station,#'台北站',
        'EndStationName': end_station,#'嘉義站',
        'SearchType': 'S',
        'StartStation': station_to_id[start_station],# '977abb69-413a-4ccf-a109-0272c24fd490',
        'EndStation': station_to_id[end_station],# '60831846-f0e4-47f6-9b5b-46323ebdcef7',
        'DepartueSearchDate': search_date,#'2019/07/07',
        'DepartueSearchTime': search_time#'15:30'
    }
    resp = requests.post(URL, data=form_data)
    data = resp.json()
    # 回傳資料也包含其他車次詳細資訊, 此處僅取出其中四項作為範例
    columns = ['TrainNumber', 'DepartureTime', 'DestinationTime', 'Duration']
    times = []
    for d in data['data']['DepartureTable']['TrainItem']:
        times.append([d[c] for c in columns])
    return times


if __name__ == '__main__':
    station_to_id = get_station_id()
    times = get_times('台北站', '嘉義站', '2019/07/12', '10:30')
    print('車次, 出發時間, 抵達時間, 行車時間')
    for t in times:
        print(t)

    # 20190708: 因高鐵網頁查詢機制改變, 以下程式碼已不適用
    # all_times = []
    #
    # times, prev_time, next_time = time_table(station_to_id['台北站'], station_to_id['嘉義站'], '2018/07/15', '10:30')
    # all_times += times
    #
    # # 較早班次
    # times, _, _ = time_table(station_to_id['台北站'], station_to_id['嘉義站'], '2018/07/15', '10:30', prev_time, '1')
    # all_times = times + all_times
    #
    # # 較晚班次
    # times, _, _ = time_table(station_to_id['台北站'], station_to_id['嘉義站'], '2018/07/15', '10:30', next_time, '2')
    # all_times += times
    #
    # for t in all_times:
    #     print(t)
