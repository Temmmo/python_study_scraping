# -*- coding: utf-8 -*-
import lxml.html, json, string, csv
from downloader import Downloader
FILEDS =('country','id')
writer =csv.writer(open('countries.csv', 'w'))
D = Downloader()
page =0
template_url = 'http://example.webscraping.com/places/ajax/search.json?&search_term={}&page_size=500&page={}'
ajax =json.loads(D(template_url.format('.', page)))
for record in ajax['records']:
    row = [record[filed] for filed in FILEDS]
    writer.writerow(row)




