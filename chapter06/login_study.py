import urllib, urllib2, lxml.html, pprint
import cookielib
def parse_form(html):
    tree =lxml.html.fromstring(html)
    data = {}
    for e in tree.cssselect('form input'):
        if e.get('name'):
            data[e.get('name')] = e.get('value')
    return data
LOGIN_URL = 'http://example.webscraping.com/places/default/user/login'
LOGIN_EMAIL = 'example@webscraping.com'
LOGIN_PASSWORD = 'example'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
html = opener.open(LOGIN_URL).read()
data = parse_form(html)
data['email'] = LOGIN_EMAIL
data['password'] = LOGIN_PASSWORD
encoded_data = urllib.urlencode(data)
request = urllib2.Request(LOGIN_URL, encoded_data)
response = opener.open(request)
print response.geturl()

