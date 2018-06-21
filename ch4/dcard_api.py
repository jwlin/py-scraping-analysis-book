import requests


DCARD_URL = 'https://www.dcard.tw'
DCARD_API = DCARD_URL + '/_api/posts?popular=true'


def show(post):
    for key in ['id', 'title', 'excerpt', 'likeCount', 'commentCount']:
        print('%s: %s' %(key, post[key]))
    print('href: %s/f/%s/p/%s' %(DCARD_URL, post['forumAlias'], post['id']))


if __name__ == '__main__':
    num_page = 5
    posts = list(requests.get(DCARD_API).json())
    for i in range(1, num_page):
        id_last_post = posts[-1]['id']
        posts += list(requests.get(DCARD_API + '&before=' + str(id_last_post)).json())
    print('共 %d 頁, %d 篇文章' %(num_page, len(posts)))
    print('第 1 篇:')
    show(posts[0])
    print('第 %d 篇:' %(len(posts)))
    show(posts[-1])