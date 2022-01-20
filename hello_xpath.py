#
#
from lxml import etree

tree = etree.parse('test.html')

print(tree)

li_list = tree.xpath('//body/ul/li/text()')

print(li_list)

print(len(li_list))
