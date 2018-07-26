#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
程序分析：999999 / 13 = 76923。
'''

n = int(input('Enter a number:'))
c = '9'
count = 1
while(1):
	if int(c*count)%n == 0:
		break
	else:
		count += 1

print('{}个9可以被{}整除：{}'.format(count,n,c*count))
print('{} / {} = {}'.format(c*count,n,int(c*count)//n))