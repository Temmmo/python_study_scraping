import login, pprint, urllib, urllib2,cookielib
LOGIN_EMAIL = 'example@webscraping.com'
LOGIN_PASSWORD = 'example'
url = 'http://example.webscraping.com/places/default/edit/Afghanistan-1'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
html = opener.open(url).read()
data = login.parse_form(html)
##data['password'] = LOGIN_PASSWORD
encoded_data = urllib.urlencode(data)
request = urllib2.Request(url, encoded_data)
response = opener.open(request)
#opener = login.login_cookies()
country_html = opener.open(url).read()
data = login.parse_form(country_html)


#data['population'] = int(data['population']) + 1
pprint.pprint(data)
encoded_data = urllib.urlencode(data)
request = urllib2.Request(url, encoded_data)
response = opener.open(request)
country_html = opener.open(url).read()
data = login.parse_form(country_html)
print data['population']