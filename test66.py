#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：输入3个数a,b,c，按大小顺序输出。　　　

程序分析：无。
'''
n1 = int(input('input a number'))
n2 = int(input('input a number'))
n3 = int(input('input a number'))

def swap(m,n):
    return n,m

if n1>n2:
    n1,n2 = swap(n1,n2)
if n1>n3:
    n1,n3 = swap(n1,n3)
if n2>n3:
    n2,n3 = swap(n2,n3)
print(n1,n2,n3)
