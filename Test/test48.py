#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：数字比较。

程序分析：无
'''
def compare(num1, num2):
    if num1 > num2:
        print("%s大于%s" % (num1, num2))
    elif num2 > num1:
        print("%s大于%s" % (num2, num1))
    else:
        print("%s等于%s" % (num1, num2))

if __name__ == "__main__":
    numOne = input("请输入第一个数字:")
    numTwo = input("请输入第二个数字:")
    compare(numOne, numTwo)
