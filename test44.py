#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
'''
import random

data1 = [[random.randint(1,100) for i in range(3)] for j in range(3)]
data2 = [[random.randint(1,100) for i in range(3)] for j in range(3)]

print("data1:",data1)
print("data2:",data2)

data3 = data1[:]

for i in range(len(data1)):
    for j in range(len(data1[i])):
        data3[i][j] = data1[i][j] + data2[i][j]
print("data3:",data3)
