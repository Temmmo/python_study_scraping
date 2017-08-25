# -*- coding: utf-8 -*-

try:
    from PySide.QtGui import QApplication
    from PySide.QtCore import QUrl, QEventLoop, QTimer
    from PySide.QtWebKit import QWebView
except ImportError:
    from PyQt4.QtGui import QApplication
    from PyQt4.QtCore import QUrl, QEventLoop, QTimer
    from PyQt4.QtWebKit import QWebView


def main():
    app = QApplication([])
    webview = QWebView()
    loop = QEventLoop()
    webview.loadFinished.connect(loop.quit)
    webview.load(QUrl('http://example.webscraping.com/places/default/search'))
    loop.exec_()
    webview.show()
    frame = webview.page().mainFrame()
    frame.findFirstElement('#search_term').setAttribute('value', '.')
    frame.findFirstElement('#page_size option').setPlainText('1000') #设置纯文本
    frame.findFirstElement('#search').evaluateJavaScript('this.click()')
    app.exec_()
    elements = None
    while not elements:
        app.processEvents()
        elements = frame.findAllElements('#results a')
        countries = [e.toPlainText().strip() for e in elements]
        print countries
if __name__ == '__main__':
    main()
