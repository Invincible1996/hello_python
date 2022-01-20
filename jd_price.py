import urllib.request

from lxml import etree


def get_content():
    base_url = 'https://search.jd.com/Search?keyword=%E9%94%AE%E7%9B%98&enc=utf-8&wq=%E9%94%AE%E7%9B%98&pvid=a5c97c53cbd84bbc836595d72797fd5a'

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }

    request = urllib.request.Request(url=base_url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    # print(content)
    return content


def parse_data(data):
    tree = etree.HTML(data)
    price_list = tree.xpath('//div[@id="J_goodsList"]/ul/li/div/div[@class="p-price"]/strong/i/text()')
    name_list = tree.xpath('//div[@id="J_goodsList"]/ul/li/div/div[@class="p-name p-name-type-2"]/a/em/text()')
    print(price_list)
    print(name_list)


if __name__ == '__main__':
    content = get_content()
    parse_data(content=content)
