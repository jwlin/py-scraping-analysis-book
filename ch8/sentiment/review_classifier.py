import json
import csv
import jieba
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score

jieba.set_dictionary('dict.txt.big')  # 對繁體中文斷詞較準確的字典檔


def load_data(a_csv, b_json, label):
    a_ids = []
    with open(a_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            a_ids.append(row['href'])
    with open(b_json, 'r', encoding='utf-8') as f:
        id_to_body = json.load(f)
    data = []
    for a_id in a_ids:
        tokenized_post = []
        txt = id_to_body[a_id]
        for sent in txt.split():  # 將文章以空白隔開
            # 斷詞後的結果, 若非空白且長度為 2 以上, 則列入詞庫
            filtered = [t for t in jieba.cut(sent) if t.split() and len(t) > 1]
            tokenized_post += filtered
        data.append((tokenized_post, label))
    return data


if __name__ == '__main__':
    pos_data = load_data('mov_pos.csv', 'id_to_body.json', '正評')
    neg_data = load_data('mov_neg.csv', 'id_to_body.json', '負評')

    '''
    # 印出正評與負評文章的前幾個字, 確認資料無誤
    for post, label in pos_data[:3]:
        print(post[:5], label)
    for post, label in neg_data[:3]:
        print(post[:5], label)
    '''

    # 打亂資料順序
    random.seed(42)
    random.shuffle(pos_data)
    random.shuffle(neg_data)

    x_train, y_train, x_test, y_test = [], [], [], []
    # 前 22 筆資料 (及答案) 放入 training set
    # 建立資料時要用空白將斷好的詞重新連成一個字串, 以便之後使用 scikit-learn 建立字典並轉換文字資料為向量
    for i in range(22):
        x_train.append(' '.join(pos_data[i][0]))
        x_train.append(' '.join(neg_data[i][0]))
        y_train.append(pos_data[i][1])
        y_train.append(neg_data[i][1])
    # 最後 5 筆資料 (及答案) 放入 testing set
    for i in range(22, len(pos_data)):
        x_test.append(' '.join(pos_data[i][0]))
        x_test.append(' '.join(neg_data[i][0]))
        y_test.append(pos_data[i][1])
        y_test.append(neg_data[i][1])

    vectorizer = CountVectorizer()
    x_train = vectorizer.fit_transform(x_train)
    transformer = TfidfTransformer()
    x_train = transformer.fit_transform(x_train)
    clf = SGDClassifier(random_state=42)
    clf.fit(x_train, y_train)
    x_test = vectorizer.transform(x_test)
    x_test = transformer.transform(x_test)
    y_pred = clf.predict(x_test)
    print('預測結果:', list(y_pred))
    print('正確答案:', y_test)
    print('正確率:', accuracy_score(y_test, y_pred))

    # 測試自己輸入的句子
    sentences = [
        '我 覺得 這部 電影 還 不錯',
        '這部 片 應該 可以 更好 才對'
    ]
    analyze = vectorizer.build_analyzer()
    print(analyze(sentences[0]))
    print(analyze(sentences[1]))

    custom_data = transformer.transform(vectorizer.transform(sentences))
    print(clf.predict(custom_data))
