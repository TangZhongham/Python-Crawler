import requests
import json


def get_url():
    package_num = input('请输入快递单号：')
    com_name = requests.get('https://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text=' + package_num)
    company = json.loads(com_name.text)['auto'][0]['comCode']
    print('Please wait...\n')
    print('Fetching the company\'s name...\n')
    print(company)
    url2 = 'https://www.kuaidi100.com/query?type=' + company + '&postid=' + package_num
    return url2


def get_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
    }
    page = requests.get(url, headers=headers)
    content = page.text
    content_json = json.loads(content)
    print('单号：' + content_json['nu'])
    print('时间----------------------------地点及跟踪进度\n')
    for info in content_json['data']:
        print(info['time'], info['context'])


if __name__ == '__main__':
    start = get_url()
    get_info(start)
    again_search = input('按任意键再次查询\'q\'键退出......\n')
    while again_search != 'q' and again_search != 'quit':
        start = get_url()
        get_info(start)
        again_search = input('按任意键再次查询\'q\'键退出......\n')


