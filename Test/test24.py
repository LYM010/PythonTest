#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

程序分析：请抓住分子与分母的变化规律。 
'''
a = 2
b = 1
lst = []
for i in range(20):
    lst.append(str(a) + '/' + str(b))
    a,b = a+b, a
print('{0} = {1}'.format(eval('+'.join(lst)), '+'.join(lst)))