#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：列表排序及连接。
程序分析：排序可使用 sort() 方法，连接可以使用 + 号或 extend() 方法。
'''
import random

if __name__ == '__main__':
	l1 = [random.randint(0, 100) for i in range(10)]
	l2 = [random.randint(0, 100) for i in range(10)]
	print(l1,l2)
	l1.sort()
	l2.sort()

	l3 = l1+l2
	print(l3)
	l3.sort()
	print(l3)