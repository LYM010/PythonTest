#!/usr/bin/env python3
# coding:UTF-8

import os,openpyxl,logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

os.chdir(os.path.join('..','tmp'))
logging.debug(f'Set default path: {os.getcwd()}')

fileList = []
type = 'txt'

logging.debug('Loading files...')
for root,dirs,files in os.walk('.'):
	for fileName in files:
		if fileName.endswith(type):
			fileList.append(os.path.join(root,fileName))
logging.debug(f'Files is {fileList}')

logging.debug('Create a new workbook.')
wb = openpyxl.Workbook()
sheet = wb.active

logging.debug('Loading data...')
for i in range(len(fileList)):
	file = open(fileList[i])
	text = file.readlines()
	for j in range(len(text)):
		sheet.cell(row=j+1,column=i+1).value = text[j]

logging.debug('Saving file...')
wb.save('c.xlsx')
logging.debug('Done')
