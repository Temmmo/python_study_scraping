import lxml.html
import re
from common import download
broken_html ='<ul class=country><li>Area<li>Population</ul>'
tree = lxml.html.fromstring(broken_html)
fixed_html = lxml.html.tostring(tree, pretty_print=True)
url ='http://example.webscraping.com/places/default/view/Armenia-12'
html = download(url)
html_tree = lxml.html.fromstring(html)
td = html_tree.cssselect('tr#places_area__row>td.w2p_fw')[0]
area = td.text_content()
print area


