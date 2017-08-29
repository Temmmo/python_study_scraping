import csv
from zipfile import ZipFile
from StringIO import StringIO
from downloader import Downloader
urls = []
zf = ZipFile('top-1m.csv.zip')
zf.extractall()
zf.close()
csv_file = open('top-1m.csv')
csv_reader = csv.reader(csv_file)
for _, website in csv_reader:
    urls.append('http://'+website)










