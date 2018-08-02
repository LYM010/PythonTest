#!/usr/bin/env python3
# coding:UTF-8

import requests,sys,webbrowser,bs4,logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

# logging.disable(logging.CRITICAL)

print('Searching...')
res = requests.get('http://www.baidu.com/s?wd=' + ' '.join(sys.argv[1:]))
assert res.status_code == requests.codes.ok

bd_soup = bs4.BeautifulSoup(res.text,'html.parser')
linkElems = bd_soup.select('.t a')

print(len(linkElems))

for i in range(min(5,len(linkElems))):
    webbrowser.open(linkElems[i].get('href'))
