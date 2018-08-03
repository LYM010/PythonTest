#!/usr/bin/env python3
# coding:UTF-8

import os,openpyxl,logging
logging.basicConfig(level = logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

logging.debug('Opening file...')
os.chdir(os.path.join('..','tmp'))
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']
logging.debug(f'sheet is {sheet}')

for columnNum in range(1,sheet.max_column+1):
	with open(f'xlsx{columnNum}.txt','w') as file:
		for rowNum in range(1,sheet.max_row+1):
			file.write(str(sheet.cell(row=rowNum,column=columnNum).value)+'\r\n')
