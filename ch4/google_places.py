import googlemaps
from pprint import pprint  # 印出排版整齊的 dict 或 JSON 資料

API_KEY = 'YOUR_API_KEY'


if __name__ == '__main__':
    gmaps = googlemaps.Client(key=API_KEY)
    geocode_result = gmaps.geocode("臺北市")
    pprint(geocode_result)

    loc = geocode_result[0]['geometry']['location']
    places = gmaps.places_radar(keyword="拉麵", location=loc, radius=2500)['results']
    print("臺北市中心半徑2500公尺的拉麵店數量: " + str(len(places)))
    print("第一筆資料")
    pprint(places[0])

    print("第一筆資料細節")
    p = gmaps.place(place_id=places[0]['place_id'], language='zh-TW')#['result']
    pprint(p)