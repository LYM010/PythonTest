#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：输出指定格式的日期。
程序分析：使用 datetime 模块。
'''
import time

print(time.time())
print(time.localtime())
print(time.asctime())
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())) 

import datetime

print(datetime.date.today()) 
print(datetime.date.today().strftime('%d/%m/%Y'))
print(datetime.date(1941, 1, 5))