#!/usr/bin/env python3
# coding:UTF-8

import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s -%(message)s')

# logging.disable(logging.CRICAL)

browser = webdriver.Firefox(executable_path = 'E:\Program Files (x86)\Mozilla Firefox\geckodriver')
browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element_by_tag_name('html')

for i in range(100):
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.LEFT)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)

print('done!')
