#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：求一个3*3矩阵主对角线元素之和。

程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
'''
import random
matrix = []
sum = 0
for i in range(3):
    matrix.append([])
    for j in range(3):
        matrix[i].append(random.randint(0,100))

print(matrix)
for i in range(3):
    sum += matrix[i][i]
print(sum)
