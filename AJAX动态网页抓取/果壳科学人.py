import requests
import json
import time


def get_target(url):
    res = requests.get(url)
    a = json.loads(res.text)
    title_list = a['result']
    print(type(title_list))
    for name in title_list:
        yield {
            '标题': name['title'],
            'URL': name['url']
        }


def write_file(target):
    with open('科学人.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(target, ensure_ascii=False) + '\n')


def main(offset):
    url = 'https://www.guokr.com/apis/minisite/article.json?retrieve_type=by_subject&limit=20&offset=' + offset + \
          '8&_=1537500260983'
    target = get_target(url)
    for item in target:
        print(item)
        write_file(item)


if __name__ == '__main__':
    for i in range(1, 10):
        main(str(i))
        time.sleep(2)
    print('Done!')
