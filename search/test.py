# -*- coding: utf-8 -*-
import lxml.html, json, string
from downloader import Downloader
D = Downloader()
template_url = 'http://example.webscraping.com/places/ajax/search.json?&search_term={}&page_size=10&page={}'
countries = set()
for letter in string.lowercase: #生成所有的小写字母
    page = 0
    while True:
        html = D(template_url.format(letter, page)) #格式化字符串的函数str.format
        try:
            ajax = json.loads(html)
        except ValueError as e:
            print e
            ajax = None
        else:
            for record in ajax['records']:
                countries.add(record['country'])
        page += 1
        if ajax is None or page >= ajax['num_pages']:
            break
open('countries.txt', 'w').write('\n'.join(sorted(countries)))#sort()与sorted()的不同在于，sort是在原位重新排列列表，而sorted()是产生一个新的列表









