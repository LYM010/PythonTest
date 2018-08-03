#!/usr/bin/env python3
# coding:UTF-8

import os,openpy,logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

# 打开xlx文件
logging.debug('Opening file...')
os.chdir(os.path.join('..','tmp'))
wb = openpyxl.load_workbook('test.xlsx')
sheet = wb[0]

logging.debug('Reading data...')
# 数据保存按行保存至列表
dataList = []
for rowNum in range(1,wb.max_row+1):
	for coloumnNum in range(1,wb.max_coloumn+1):
		cList.append(sheet.cell(row=rowNum,coloumn=coloumnNum).value)
		sheet.cell(row=rowNum,coloumn=coloumnNum).value = ''
	dataList.append(cList)

# 交换行列
logging.debug('Switching data...')
wbNew = openpyxl.Workbook()
sheetNew = wbNew[0]
for i in range(len(dataList)):
	for j in range(len(dataList[0])):
		sheetNew.cell(row=j,coloumnNum=i).value=dataList[i][j]

# 保存数据至新表
wbNew.save('test_copy.xlsx')