import requests
from requests.exceptions import ConnectionError
from lxml import etree
import os


# TODO: Download Page
def get_page(offset):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    url = 'https://www.fabiaoqing.com/biaoqing/lists/page/' + str(offset)
    html = requests.get(url, headers=headers)
    try:
        if html.status_code == 200:
            return html.content
    except ConnectionError:
        pass


# TODO: Use Xpath to parse and download photo urls
def parse_page(html, offset):
    selector = etree.HTML(html)
    image_list = selector.xpath('//a/img/@data-original')
    os.mkdir(str(i))
    for image in image_list:
        print('Downloading one image...')
        if str(image).endswith('jpg'):
            file_path = '{0}/{1}.{2}'.format(str(offset), str(image)[50:55], '.jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    target = requests.get(image)
                    content = target.content
                    f.write(content)
                    print('one jpg file downloaded!')
        elif str(image).endswith('gif'):
            file_path = '{0}/{1}.{2}'.format(str(offset), str(image)[50:55], '.gif')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    target = requests.get(image)
                    content = target.content
                    f.write(content)
                    print('one gif file downloaded!')
        else:
            print('Oops, one image failed to download. :/')


# TODO: Make a loop for 10 pages


if __name__ == '__main__':
    for i in range(1,11):
        page = get_page(i)
        parse_page(page, i)
    print('Finished!')

