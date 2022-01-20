from selenium import webdriver
import time

path = './chromedriver'

browser = webdriver.Chrome(path)

url = 'https://slamdunk.sports.sina.com.cn/match#status=1&date=2022-01-20'
#
browser.get(url)

# content = browser.page_source
# print(content)

# 日期
# date_list = browser.find_elements_by_xpath('//div[@class="match-con"]/div[@class="match-con-list"]/h2')

# 前缀
pre_path = '//div[@class="match-con"]/div[@class="match-con-list"]/ul[@class="match-con-ul"]/li'

# 开始时间
start_time_list = browser.find_elements_by_xpath(
    pre_path + '/span[@class="match-con-time living-time2"]')

# 比分
score_result_list = browser.find_elements_by_xpath(
    pre_path + '/p/span/span[@class="match-con-num"]/a')

# 主队
home_team_list = browser.find_elements_by_xpath(pre_path + '/p/span/a')

# 客队

away_team_list = browser.find_elements_by_xpath(pre_path + '/p/span/span[@class="match-con-text_left"]/a')

time.sleep(1.0)

for i in range(len(score_result_list)):
    start_time = start_time_list[i].text
    score_result = score_result_list[i].text
    home_team = home_team_list[i].text
    away_team = away_team_list[i].text
    print(start_time, score_result, away_team, 'vs', home_team)

# for score in score_result_list:
#     print(score.text)
#
# for time in start_time_list:
#     print(time.text)

# for div in date_list:
#     print(div.text)

# url = 'https://www.baidu.com'
# browser.get(url)
#
# # 元素定位
#
# # 根据id来找到对象
# # button = browser.find_element_by_id('su')
# # print(button)
#
# # 根据标签属性的属性值来获取对象的
# # button = browser.find_element_by_name('wd')
# # print(button)
#
# # 根据xpath语句来获取对象
# button = browser.find_elements_by_xpath('//input[@id="su"]')[0]
# print(button.get_attribute('value'))

# 根据标签的名字来获取对象
# button = browser.find_elements_by_tag_name('input')
# print(button)

# 使用的bs4的语法来获取对象
# button = browser.find_elements_by_css_selector('#su')
# print(button)

# button = browser.find_element_by_link_text('直播')
# print(button)
