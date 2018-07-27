#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

程序分析：关键是计算出每一项的值。
'''
n=str(input('请输入计算数:'))
m=int(input('请输入层数:'))
s=0
for i in range(1,m+1):
    a=n*i
    s+=eval(a)
print('{}'.format(s))
