import urlparse
compnents = urlparse.urlsplit('http://example.webscring.com/index/')
print compnents
print compnents.path
path =compnents.path
if not path:
    path = '/index.html'
elif path.endswith('/'):
    path += 'index.html'
filename = compnents.netloc +path +compnents.query
print filename