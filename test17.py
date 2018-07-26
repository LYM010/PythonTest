#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。
'''
InPut = input('输入任意字符:')
letters = []
spaces = []
digits = []
others = []
for i in iter(InPut):
    if i.isalpha() == True:
        letters.append(i)
    elif i.isspace() == True:
        spaces.append(i)
    elif i.isdigit() == True:
        digits.append(i)
    else:
        others.append(i)
print('''
字母: {}, 个数: {};
空字符: {}, 个数: {};
数字: {}, 个数: {};
其他: {}, 个数: {}'''.format(letters, len(letters), spaces, len(spaces), digits, len(digits), others, len(others)))
