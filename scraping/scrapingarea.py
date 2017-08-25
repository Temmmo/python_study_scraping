from bs4 import BeautifulSoup
import re
from common import download
url ='http://example.webscraping.com/places/default/view/Armenia-12'
html = download(url)
soup =BeautifulSoup(html,'html.parser')
tr =soup.find(attrs={'id': 'places_area__row'})
#tr =BeautifulSoup(tr,'html.parser')
td =tr.find(attrs={'class': 'w2p_fw'})
area =td.text
print  area

