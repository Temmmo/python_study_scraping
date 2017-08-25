import re
from common import download
from bs4 import BeautifulSoup
url ='http://example.webscraping.com/places/default/view/Armenia-12'
html =download(url)
print re.findall('<tr id="places_area__row"><td class=["\']w2p_fl["\']><label class="readonly" for="places_area" id="places_area__label">Area: </label></td><td class="w2p_fw">(.*?)</td>', html)
broken_html ='<ul class=country><li>Area<li>Population</ul>'
soup =BeautifulSoup(broken_html, 'html.parser')
fixed_html =soup.prettify()
#print fixed_html
ul = soup.find('ul', attrs={'class': 'country'})
print ul.find('li')
print ul.find_all('li')

