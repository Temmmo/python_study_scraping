import os
import re
import urlparse
import pickle
class DiskCache:
    def __init__(self,cache_dir ='cache'):
        self.cache_dir =cache_dir
        self.max_length = max_length
    def url_to_path(self, url):
        components = urlparse.urlsplit(url)
        path =components.path
        path = components.path
        if not path:
            path = '/index.html'
        elif path.endswith('/'):
            path += 'index.html'
        filename = components.netloc + path + components.query
        filename = re.sub('[^/0-9a-zA-Z\-.,;_]', '_', filename)
        filename ='/'.join(segment[:255] for segment in filename.split('/'))
        return os.path.join(self.cache_dir, filename)
    def __getitem__(self, url):
        path = self.url_to_path(url)
        if os.path.exists(path):
            with open(path, 'rb') as fp:#紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，这个方法的返回值将被赋值给as后面的变量。当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法。
                return pickle.load(fp)
        else:
            raise KeyError(url +'does not exist')#在Python中，要想引发异常，最简单的形式就是输入关键字raise，后跟要引发的异常的名称。
    def __setitem__(self, url, result):
        path = self.url_to_path(url)
        folder =os.path.dirname(path)
        if not os.path.exists(path):
            os.makedev(folder)
        with open(path, 'wb') as fp:
            fp.write(pickle.dumps(result))
