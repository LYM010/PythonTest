#!/usr/bin/env python3
# coding:UTF-8
import requests,os,bs4,logging,threading

savePath = os.path.join('..','xkcd')
os.makedirs(savePath,exist_ok=True)
os.chdir(savePath)
logging.basicConfig(filename='download_log.log',level=logging.DEBUG,format='%(asctime)s - %(levelname)s -%(message)s')

# logging.disable(logging.CRICAL)
logging.debug(f'Setting work path:{savePath}')

def download(startNum,endNum,url):
	for urlNum in range(startNum,endNum):
		print(f'Downloading page: {url+str(urlNum)}')
		logging.debug(f'Downloading page: {url+str(urlNum)}')

		res = requests.get(url+str(urlNum))
		res.raise_for_status()

		soup = bs4.BeautifulSoup(res.text)
		comicElem = soup.select('#comic img')

		if comicElem == []:
			print('Could not found comic image.')
			logging.debug(f'Could not found comic image in{url+str(urlNum)}')
		else:
			comicUrl = 'https:'+ comicElem[0].get('src')
			logging.debug(f'Downloading comic image:{comicUrl}')
			res = requests.get(comicUrl)
			res.raise_for_status()

			imageFile = open(os.path.basename(comicUrl),'wb')
			for chunk in res.iter_content(100000):
				imageFile.write(chunk)
			imageFile.close()
			logging.debug(f'{comicUrl} has been load.')

URL = 'http://xkcd.com/'
downloadThreads = []
for i in range(1,1500,100):
	logging.debug(f'Start thread {i}')
	downloadThread = threading.Thread(target=download,args=(i,i+99,URL))
	downloadThreads.append(downloadThread)
	downloadThread.start()

for downloadThread in downloadThreads:
	downloadThread.join()

logging.debug(f'Done.')