#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

程序分析：无。 
'''
def output(s,l):
    if l==0:
       return
    print(s[l-1])
    output(s,l-1)
 
s = input('Input a string:')
output(s,len(s))
