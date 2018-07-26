#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：某个公司采用公用电话传递数据，数据是四位的整数，
在传递过程中是加密的，加密规则如下：
每位数字都加上5,然后用和除以10的余数代替该数字，
再将第一位和第四位交换，第二位和第三位交换。
程序分析：无。
'''
def example89():
    val=[5,4,9,7]
    newval=[(i+5)%10 for i in val]
    l=len(newval)
    for i in range(0,l//2):
        newval[i],newval[l-i-1]=newval[l-i-1],newval[i]
    print(newval)
example89()