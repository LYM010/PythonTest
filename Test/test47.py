#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：两个变量值互换。

程序分析：无
'''
def exchange(a,b):
    a,b = b,a
    return (a,b)
 
if __name__ == '__main__':
    x = int(input('Enter a number:'))
    y = int(input('Enter a number:'))
    print('x = %d,y = %d' % (x,y))
    x,y = exchange(x,y)
    print('x = %d,y = %d' % (x,y))
