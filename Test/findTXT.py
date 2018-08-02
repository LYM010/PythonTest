#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
编写一个程序，打开文件夹中所有的.txt文件，查找匹配用户提供的正则表达式
的所有行。结果应该打印到屏幕上。
'''
import re,os,sys
cwd = os.getcwd()
txtDirList = []

regex1 = re.compile(r'\.txt$')
for sdir in os.listdir(cwd):
	if regex1.search(sdir):
		txtDirList.append(sdir)
print(txtDirList)

print('{} {}'.format(sys.argv[0],sys.argv[1]))
regex2 = re.compile(sys.argv[1])
txtLineList = []

for sdir in txtDirList:
	with open(sdir,'r',encoding='UTF-8') as txtFile:
		txtLineList = txtFile.readlines()
		for l in txtLineList:
			if regex2.search(l):
				print(l)