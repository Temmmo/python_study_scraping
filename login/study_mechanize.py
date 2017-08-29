# -*- coding: utf-8 -*-

import urllib
import urllib2
import mechanize
import login
import pprint
LOGIN_EMAIL = 'example@webscraping.com'
LOGIN_PASSWORD = 'example'
COUNTRY_URL = 'http://example.webscraping.com/places/default/edit/Afghanistan-1'
LOGIN_URL = 'http://example.webscraping.com/places/default/user/login?_next=/places/default/index'
br = mechanize.Browser()
br.open(LOGIN_URL)
br.select_form(nr=0)
br['email'] = LOGIN_EMAIL
br['password'] = LOGIN_PASSWORD
response = br.submit()
br.open(COUNTRY_URL)
br.select_form(nr=0)
br['population'] = str(250)
br.submit()



