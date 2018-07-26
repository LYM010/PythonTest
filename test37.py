#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：对10个数进行排序。

程序分析：可以利用选择法，即从后9个比较过程中，
选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，
并进行交换。
'''

import random

l = []

for n in range(10):
    l.append(random.randint(0,100))

print(l)

for i in range(len(l)):
    for j in range(i):
        if l[i] < l[j]:
            l[i],l[j] = l[j],l[i]

print(l)
