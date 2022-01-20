# 获取NBA球队名称
import urllib.request

from lxml import etree


class Team:
    def __init__(self, team_id, logo_url, team_name):
        self._team_id = team_id
        self._logo_url = logo_url
        self._team_name = team_name

    def to_string(self):
        print("Id : ", self._team_id, "Name : ", self._team_name, "logo : ", self._logo_url)


def create_request():
    base_url = 'https://china.nba.cn/standings/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    request = urllib.request.Request(url=base_url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)
    tree = etree.HTML(content)
    id_list = tree.xpath('//div[@class="wrap-list"]//a/@data-id')
    logo_list = tree.xpath('//div[@class="wrap-list"]//a/span/img/@src')
    name_list = tree.xpath('//div[@class="wrap-list"]//a/i/text()')

    print(id_list)
    print(logo_list)
    print(name_list)

    team_list = []

    for i in range(len(name_list)):
        team = Team(id_list[i], 'https:' + logo_list[i], name_list[i])
        team_list.append(team)
        urllib.request.urlretrieve(url='https:' + logo_list[i], filename='./logo/' + name_list[i] + '.jpg')
    print(team_list)


if __name__ == '__main__':
    request = create_request()
    get_content(request)
