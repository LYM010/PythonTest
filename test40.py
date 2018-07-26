#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：将一个数组逆序输出。

程序分析：用第一个与最后一个交换。
'''
import random
l = []

for i in range(10):
    l.append(random.randint(0,100))
print(l)
print(l[::-1])
