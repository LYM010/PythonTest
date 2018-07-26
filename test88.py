#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
程序分析：无。
'''
if __name__ == '__main__':
    n = 1
    while n <= 7:
        a = int(input('input a number:\n'))
        while a < 1 or a > 50:
            a = int(nput('input a number:\n'))
        print(a * '*')
        n += 1