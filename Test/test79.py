#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：字符串排序。
程序分析：无。
'''
if __name__=='__main__':
    ls=[]
    str1=input("string1:\n")
    str2=input("string2:\n")
    str3=input("string3:\n")
    ls.extend([str1,str2,str3])
    ls.sort()
    print(ls)