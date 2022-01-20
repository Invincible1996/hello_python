import urllib.request

from lxml import etree

headers = {
    'cookie': 'sid=53cb7f655825bd66f8fdd9b27e82757b; __cf_bm=NNIT1Ne.YxgJ7OLhwtnaQLYFVbiGjz9j2yRDktkDxTk-1642491599-0-AeV/Ih2a7mkL0HaBcwKoPPOGh0dvvCpUYS+D8VZmlfMQGo+aQ/hAY6hcE1E8ZhWas9HZRxEUe7xJ0U5Ox0Kah0R/FM1FMLqcef2izIpe29LxPLNcwNbZ47MU6nooAI5Seg==; _gid=GA1.2.1345476268.1642491600; screen-width=1920; screen-height=1080; ratio=1; _ga=GA1.2.1173695629.1638601659; _ga_TXM0B6HHQC=GS1.1.1642491599.3.1.1642492128.0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}


def get_content():
    # base_url = 'https://4kwallpapers.com/nature/'
    base_url = 'https://4kwallpapers.com/technology/'
    request = urllib.request.Request(url=base_url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    tree = etree.HTML(content)
    img_list = tree.xpath('//div[@id="pics-list"]/p/a/span/img/@src')
    href_list = tree.xpath('//div[@id="pics-list"]/p/a/@href')

    print(href_list)
    print(img_list)

    for item in img_list:
        img_name = item.split('/')[6].split('.')[0]
        # download_img(opener=opener, url=item, filename=img_name)


def download_img(url, filename):
    opener = urllib.request.URLopener()
    opener.addheader('user-agent',
                     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36')
    opener.retrieve(url, filename='./img/' + filename + '.jpeg')


def get_big_image_url():
    url = 'https://4kwallpapers.com/technology/google-logo-typography-night-crescent-moon-half-moon-5k-8k-4562.html'
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    tree = etree.HTML(content)
    href_list = tree.xpath('//div[@id="content"]/div/div/div[@class="pic-right"]/div/span/a/@href')
    print(href_list)
    download_img(url='https://4kwallpapers.com' + href_list[0], filename='test')


def get_tree():
    print('tree')


if __name__ == '__main__':
    # get_content()
    get_big_image_url()
