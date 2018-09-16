import requests
from requests.exceptions import ConnectionError, ConnectTimeout
from lxml import etree
import os


# TODO: Download the page
def get_page(offset):
    headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    url = 'http://jandan.net/ooxx/page-' + str(offset)
    html = requests.get(url, headers=headers)
    try:
        if html.status_code == 200:
            return html.content
    except ConnectTimeout and ConnectionError:
        print('Oops, error occurs!')


# TODO: Parse the page
def parse_page(html, offset):
    selector = etree.HTML(html)
    image_list = selector.xpath('//p/img/@src')
    print(image_list)
    os.mkdir(str(i))
    for image in image_list:
        if str(image).endswith('jpg'):
            file_path = '{0}/{1}.{2}'.format(str(offset), str(image)[40:45], '.jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    target = requests.get(image)
                    content = target.content
                    f.write(content)
                    print('one jpg file downloaded!')
        elif str(image).endswith('gif'):
            file_path = '{0}/{1}.{2}'.format(str(offset), str(image)[40:45], '.gif')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    target = requests.get(image)
                    content = target.content
                    f.write(content)
                    print('one gif file downloaded!')
        else:
            print('Oops, one image failed to download. :/')


if __name__ == '__main__':
    for i in range(1,5):
        page = get_page(i)
        parse_page(page, i)
    print('Finished!')

