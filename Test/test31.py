#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：请输入星期几的第一个字母来判断一下是星期几，
如果第一个字母一样，则继续判断第二个字母。

程序分析：用情况语句比较好，如果第一个字母一样，
则判断用情况语句或if语句判断第二个字母。
'''
week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def find(week,s=''):
    result = []
    c = input('please input a letter\n')
    s+=c
    s=s.lower()
    for i in week:
        if i.startswith(s):
            result.append(i)
    if len(result)==1:
        return result
    else:
        return find(result,s)

print(find(week)[0].capitalize())
        
