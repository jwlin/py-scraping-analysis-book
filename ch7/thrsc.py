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


if __name__ == '__main__':
    station_to_id = get_station_id()
    all_times = []

    times, prev_time, next_time = time_table(station_to_id['台北站'], station_to_id['嘉義站'], '2018/07/15', '10:30')
    all_times += times

    # 較早班次
    times, _, _ = time_table(station_to_id['台北站'], station_to_id['嘉義站'], '2018/07/15', '10:30', prev_time, '1')
    all_times = times + all_times

    # 較晚班次
    times, _, _ = time_table(station_to_id['台北站'], station_to_id['嘉義站'], '2018/07/15', '10:30', next_time, '2')
    all_times += times

    for t in all_times:
        print(t)
