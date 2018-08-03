#!/usr/bin/env python3
# coding:UTF-8

import os,openpyxl,logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

# 打开xlx文件
logging.debug('Opening file...')
os.chdir(os.path.join('..','tmp'))
wb = openpyxl.load_workbook('test.xlsx')
sheet = wb['Sheet1']

logging.debug('Reading data...')
# 数据保存按行保存至列表
dataList = []
for rowNum in range(1,sheet.max_row+1):
	cList=[]
	for columnNum in range(1,sheet.max_column+1):
		cList.append(sheet.cell(row=rowNum,column=columnNum).value)
		sheet.cell(row=rowNum,column=columnNum).value = ''
	dataList.append(cList)

# 交换行列
logging.debug('Switching data...')
wbNew = openpyxl.Workbook()
sheetNew=wbNew.active
for i in range(len(dataList)):
	for j in range(len(dataList[0])):
		sheetNew.cell(row=j+1,column=i+1).value=dataList[i][j]

# 保存数据至新表
logging.debug('Saving data...')
wbNew.save('test_copy.xlsx')