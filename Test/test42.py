#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：学习使用auto定义变量的用法。

程序分析：没有auto关键字，使用变量作用域来举例吧。
'''
num = 2
def autofunc():
    num = 1
    print('internal block num = {}'.format(num))
    num = num + 1


for i in range(3):
    print('The num = {}'.format(num))
    num += 1
    autofunc()
