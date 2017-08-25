import re
import time
import lxml.html
from common import download
from bs4 import BeautifulSoup
FIELDS = ('area','population','iso','country', 'capital','continent', 'tld','currency_code',
          'currency_name', 'phone','postal_code_format')
def re_scraper(html):
    results ={}
    for field in FIELDS:
        results[field] = re.search('<tr id="places_%s__row">.*?<td class="w2p_fw">(.*?)</td>' % field, html).groups()[0]
    return results
def bs_scraper(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = {}
    for field in FIELDS:
        #ta =soup.find('table')
        tr = soup.find(attrs={'id':'places_%s__row'% field})
        td = tr.find(attrs={'class':'w2p_fw'})
        results[field]=td.text
    return results
def lxml_scraper(html):
    tree = lxml.html.fromstring(html)
    results ={}
    for field in FIELDS:
        results[field] =tree.cssselect('table > tr#places_%s__row > td.w2p_fw' % field)[0].text_content()
    return results

NUM_ITERATIONS = 100
url ='http://example.webscraping.com/places/default/view/Armenia-12'
html = download(url)
for name, scraper in[('Regular expressions',re_scraper),
                      ('Lxml',lxml_scraper),
                     ('BeautifulSoup',bs_scraper)]:
    start =time.time()
    for i in range(NUM_ITERATIONS):
        if scraper == re_scraper:
            re.purge()
        result = scraper(html)
    end =time.time()
    print '%s: %.2f seconds'%(name, end-start)





