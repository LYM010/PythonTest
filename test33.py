#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：按逗号分隔列表。

程序分析：无。
'''
a = [1,2,3,4,5]
for i in a:
    if i!=a[-1]:
        print(i,end=',')
    else:
        print(i)
