#!/usr/bin/env python3
# coding:UTF-8
import requests,os,bs4,logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s -%(message)s')

# logging.disable(logging.CRICAL)

url = 'http://xkcd.com'
savePath = os.path.join('..','xkcd')
os.makedirs(savePath,exist_ok=True)

while not url.endswith('#'):
    print('Downloading page %s' % url)
    res = requests.get(url)
    assert res.status_code == requests.codes.ok

    soup = bs4.BeautifulSoup(res.text)
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'http:'+comicElem[0].get('src')
        print('Downloading image %s...'%comicUrl)
        res = requests.get(comicUrl)
        assert res.status_code == requests.codes.ok

        imageFile = open(os.path.join(savePath,os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com'+prevLink.get('href')
print('Done')
