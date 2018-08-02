#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：时间函数举例3。
程序分析：无。
'''

def f(num):
	print(num)
	if num == 1:
		return
	elif num%2 == 0:
		f(num//2)
	elif num%2 == 1:
		f(num*3+1)

if __name__ == '__main__':
    n = int(input('Enter a number:'))
    f(n)