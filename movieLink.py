#!/usr/bin/env python3
# coding:UTF-8

import requests,os,bs4,logging,codecs
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s -%(message)s')
# logging.disable(logging.CRITICAL)

url = 'http://www.dytt8.net/'
savePath = os.path.join('..','movieLink.txt')
movieLink = codecs.open(savePath,'a','utf-8')

res = requests.get(url)
res.raise_for_status()
aElement = bs4.BeautifulSoup(res.text,features="html.parser").select('a[href]')
movieLink.write(f'-----------------------------------------\r\nThere are {len(aElement)} links in {url}\r\n')

for i in range(len(aElement)):
    link = aElement[i].get('href')
    if link.startswith('/'):
        link = link[1:]
    if not link.startswith('http:') or not link.startswith('https:'):
        link = url +link
    try:
        link_res = requests.get(link,timeout=3)
        if link_res.status_code == 404:
            movieLink.write(f'\r\nNot Found: {link}')
    except requests.exceptions.Timeout:
        movieLink.write(f'\r\nTimeout: {link}')

movieLink.write('\r\n-----------------------------------------')
movieLink.close()
