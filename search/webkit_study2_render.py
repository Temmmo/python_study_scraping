# -*- coding: utf-8 -*-

import re
import csv
import time
import socket
try:
    from PySide.QtGui import QApplication
    from PySide.QtCore import QUrl, QEventLoop, QTimer
    from PySide.QtWebKit import QWebView
except ImportError:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
    from PyQt4.QtWebKit import *

import lxml.html
class BrowserRender(QWebView):
    def __init__(self, display=True):
        self.app = QApplication([])
        QWebView.__init__(self)
        if display:
            self.show()   # show the browser
    def downlaod(self,url,timeout=60):
        loop = QEventLoop()
        timer = QTimer()
        timer.setSingleShot(True)
        timer.timeout.connect(loop.quit)
        self.loadFinished.connect(loop.quit)
        self.load(QUrl(url))
        timer.start(timeout * 1000)
        loop.exec_()
        if timer.isActive():
            timer.stop()
            return self.html()
        else:
            print 'Request timed out: '+ url
    def html(self):
        return self.page().mainFrame().toHtml()
    def find(self, pattern):
        return self.page().mainFrame().findAllElements(pattern)
    def attr(self, pattern, name, value):
        for e in self.find(pattern):
            e.setAttribute(name, value)
    def text(self, pattern, value):
        for e in self.find(pattern):
            e.setPlainText(value)
    def click(self, pattern):
        for e in self.find(pattern):
            e.evaluateJavaScript("this.click()")
    def wait_load(self, pattern, timeout=60):
        deadline = time.time()+timeout
        while time.time() < deadline:
            self.app.processEvents()
            matches = self.find(pattern)
            if matches:
                return matches
        print 'Wait load timed out'

br = BrowserRender()
br.downlaod('http://example.webscraping.com/places/default/search')
br.attr('#search_term', 'value', '.')
br.text('#page_size option','1000')
br.click('#search')
elements = br.wait_load('#results a')
countries= [e.toPlainText().strip() for e in elements]
print countries






