import re,csv
import urlparse, urllib2, datetime, time
import lxml.html
def download(url,proxy, user_agent='shu',num_retries = 2):
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
                return download(url, user_agent=user_agent,proxy=proxy, num_retries=num_retries-1)
        html = None
    return html

def link_crawler(seed_url, proxy, delay=5,max_depth = 2,scrape_callback=None):
    crawl_queue = [seed_url]
    seen = {seed_url: 0}
    throttle = Throttle(delay)
    while crawl_queue:
        url = crawl_queue.pop()
        throttle.wait(url)
        html = download(url, proxy= proxy)
        links = []
        if scrape_callback:
            print url, html
            links.extend(scrape_callback(url, html) or [])
        depth = seen[url]
        if depth != max_depth:
            for link in get_links(html):
                link = urlparse.urljoin(seed_url, link)
                # check if have already seen this link
                if link not in seen:
                    seen[link] = depth + 1
                    crawl_queue.append(link)

def get_links(html):
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    return webpage_regex.findall(html)

class Throttle:
    def __init__(self,delay):
        self.delay = delay
        self.domains ={}
    def wait(self, url):
        domain =urlparse.urlparse(url).netloc
        last_accessed = self.domains.get(domain)
        if self.delay>0 and last_accessed is not None:
            sleep_secs =self.delay- (datetime.datetime.now()-last_accessed).seconds
            if sleep_secs>0:
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.datetime.now()
class ScrapeCallback:
    def __init__(self):
        self.writer = csv.writer(open('countries.csv', 'w'))
        self.fields = ('area', 'population', 'iso', 'country', 'capital', 'continent', 'tld', 'currency_code', 'currency_name', 'phone', 'postal_code_format', 'postal_code_regex', 'languages', 'neighbours')
        self.writer.writerow(self.fields)
    def __call__(self, url, html):
        if re.search('/view/', url):
            tree = lxml.html.fromstring(html)
            row = []
            for field in self.fields:
                row.append(tree.cssselect('table > tr#places_{}__row > td.w2p_fw'.format(field))[0].text_content())
            self.writer.writerow(row)


if __name__ == '__main__':
    link_crawler('http://example.webscraping.com',proxy=None,delay=3, max_depth=1,scrape_callback=ScrapeCallback())
