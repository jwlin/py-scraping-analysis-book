* 20190708: `ch7/thrsc.py`: 因高鐵網頁查詢機制改變, 原程式碼已不適用; 該網頁新的機制會送出 POST 請求到另一個網址, 並回傳 JSON 檔案, 包含當日所有車次資料. 請參考新的 `get_times()` 函式
* 20190523: `ch8/finanance/kd.py`: 修正程式碼關於取得前一天 k, d 值的錯誤
* 20190309: `ch3/news.py`: 擷取自由今日焦點時加上判斷式 `if ele.find('a', 'tit')` 以略過廣告區塊
* 20190125: `ch3/dcard.py`: `requests.get()` 內加上 User-Agent 的 header
* 20190120: `ch6/non_utf.py`: 博客來 66 折網址已換，且改為 utf-8 編碼，`gold_66_test()` 已失效，請參考 `gold_66_new()`
