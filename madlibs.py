#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
首先创建文本文件，文本内容如下：
The ADJECTIVE panda walked to the NOUN and then VERB. 
A nearby NOUN was unaffected by these events.
'''

import re

if __name__ == '__main__':
	# 读取文本
	txtFile = open('test1')
	s1 = txtFile.read()
	txtFile.close()

	# 查找关键字
	pattern = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
	lst = pattern.findall(s1)

	# 替换关键字
	for word in lst:
		tmp = input('Enter a {}:\n>'.format(word))
		regex = re.compile(word)
		s1 = regex.sub(tmp, s1,1)
	
	# 输出至屏幕
	print(s1)

	# 输出至新文件
	new_txtFile = open('test2','w')
	new_txtFile.write(s1)
	new_txtFile.close()
