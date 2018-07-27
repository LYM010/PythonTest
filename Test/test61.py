#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：打印出杨辉三角形（要求打印出10行如下图）。　　

程序分析：无。
'''
l = []
# 建立杨辉三角结构
for i in range(10):
    l.append([])
    for j in range(10):
        l[i].append(0)
# 填充每行第一和最后一个元素为1
for i in range(10):
    l[i][0] = 1
    l[i][i] = 1
# 计算其他位置的元素，每个数字等于上一行的左右两个数字之和，即 C(n+1,i)=C(n,i)+C(n,i-1)。
for i in range(2,10):
    for j in range(1,i):
        l[i][j] = l[i-1][j-1] + l[i-1][j]
from sys import stdout
for i in range(10):
    for j in range(i + 1):
        stdout.write(str(l[i][j]))
        stdout.write(' ')
    print()
