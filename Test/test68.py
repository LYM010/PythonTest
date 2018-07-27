#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
程序分析：无。
'''

import random

if __name__ == '__main__':
	n=10
	l = [random.randint(0, 100) for i in range(n)]
	print(l)
	m = int(input("Enter a number:"))
	l[m:n],l[0:m] = l[0:n-m],l[n-m:n]
	print(l)