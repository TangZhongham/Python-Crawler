from selenium import webdriver
import os
import requests
import time
import random


def get_page(url, offset):
    if not os.path.exists(str(offset)):
        print(url + str(offset))
        os.mkdir('page' + str(offset))
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(url + str(offset))
        print(url + str(offset))
        print('Start downloading page ' + str(offset))
        image_list = browser.find_elements_by_class_name('view_img_link')
        for img in image_list:
            image_url = img.get_attribute('href')
            print('This file\'s url is ' + image_url)
            print('Downloading...\n')
            image = requests.get(image_url)
            content = image.content
            if str(image_url).endswith('jpg'):
                with open('{0}/{1}.{2}'.format('page' + str(offset), str(random.randint(1,1000)), 'jpg'), 'wb') as f:
                    f.write(content)
                    print('One JPG downloaded!\n')
            elif str(image_url).endswith('gif'):
                with open('{0}/{1}.{2}'.format('page' + str(offset), str(random.randint(1,1000)), 'gif'), 'wb') as f:
                    f.write(content)
                    print('One GIF downloaded!\n')
            else:
                print('Oops! Don\'t know what it is :/ \n')
        print('\n-----------One page finished! ; )')
        time.sleep(3)
        browser.close()
        time.sleep(1)


if __name__ == '__main__':
    url = 'http://jandan.net/ooxx/page-'
    i = 1
    while i <= 40:
        print(url + str(i))
        get_page(url, i)
        i = i + 1
    print('\n-------------------------All Downloaded!')


'''
    url = 'http://jandan.net/ooxx/page-'
    for i in [1, 2, 3, 4]:
        get_page(url, i)
    print('\n-------------------------All Downloaded!')
'''