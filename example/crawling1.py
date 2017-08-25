import urllib2, re, itertools, urlparse


def download(url, user_agent='wswp',proxy,num_retries = 2):
    print 'Downloading:', url
    headers ={'User-agent':user_agent}
    request = urllib2.Request(url,headers=headers)
    opener = urllib2.build_opener()
    if proxy:
        proxy_params ={urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        html = opener.open(request).read()
    except urllib2.URLError as e:
        print 'Downloading error:',e.reason
        if num_retries>0:
            if hasattr(e, 'code') and 500 <=e.code <600:
                return download(url, num_retries-1)
        html = None
    return html
def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall('href=(.*?)', sitemap)
    # cant work
    for link in links:
        html = download(link)


max_errors = 5
num_errors = 0
for page in itertools.count(1):
    url = 'http://example.webscraping.com/places/default/view/-%d' % page
    html = download(url)
    if html is None:
        num_errors +=1
        if num_errors == max_errors:
            break
    else:
        num_errors = 0


