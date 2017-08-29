import urllib, urllib2, lxml.html, pprint, json
import cookielib
import os,glob
def load_ff_sessions(session_filename):
    cj =cookielib.CookieJar()
    if os.path.exists(session_filename):
        json_data = json.loads(open(session_filename, 'rb').read())
        for window in json_data.get('windows', []):
            for cookie in window.get('cookies', []):
                import pprint;
                pprint.pprint(cookie)
                c = cookielib.Cookie(0, cookie.get('name', ''), cookie.get('value', ''),
                                     None, False,
                                     cookie.get('host', ''), cookie.get('host', '').startswith('.'),
                                     cookie.get('host', '').startswith('.'),
                                     cookie.get('path', ''), False,
                                     False, str(int(time.time()) + 3600 * 24 * 7), False,
                                     None, None, {})
                cj.set_cookie(c)
    else:
        print 'Session filename does not exist:', session_filename
    return cj
def find_ff_sessions():
    paths = [
        '~/.mozilla/firefox/*.default',
        '~/Library/Application Support/Firefox/Profiles/*.default',
        '%APPDATA%/Roaming/Mozilla/Firefox/Profiles/*.default'
    ]
    for path in paths:
        filename = os.path.join(path, 'sessionstore.js')
        matches = glob.glob(os.path.expanduser(filename))
        if matches:
            return matches[0]
session_filename = find_ff_sessions()
print  session_filename
cj = load_ff_sessions(session_filename)
processor = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(processor)
url = 'http://example.webscraping.com'
html = opener.open(url).read()
tree = lxml.html.fromstring(html)
print tree.cssselect('ul#navbar li a')[0].text_content()

