from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('D:\\firefox\\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)
driver.get('http://example.webscraping.com/places/default/search')
driver.find_element_by_id('search_term').send_keys('.')
driver.execute_script("document.getElementById('page_size').options[1].text = '1000'");
driver.find_element_by_id('search').click()
driver.implicitly_wait(30)
links = driver.find_elements_by_css_selector('#results a')
countries = [link.text for link in links]
driver.close()
print countries




