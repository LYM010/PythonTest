#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，
插入后此元素之后的数，依次后移一个位置。 
'''
import random
l = []

for i in range(10):
    l.append(random.randint(0,100))
l.sort()
print(l)
number = int(input("\n插入一个数字:\n"))
length=len(l)
if number > l[-1]:
        l.append(number)
else:
    l.append(0)
    for i in range(length):
        if l[i] > number:
            temp1 = l[i]
            l[i] = number
            for j in range(i + 1,length+1):
                temp2 = l[j]
                l[j] = temp1
                temp1 = temp2
            break
print('排序后列表:',l)

