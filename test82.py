#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：八进制转换为十进制
程序分析：无。
'''

def f8to10(n):
	sum = 0
	j = len(n)-1
	for flag in n:
		sum += pow(8,j)*int(flag)
		j -= 1
	return sum

n = input('Enter a octal number: ')
print(f8to10(n))