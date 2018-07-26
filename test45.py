#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：统计 1 到 100 之和。

程序分析：无
'''
from functools import reduce
print(reduce(lambda x,y:x+y,range(1,101)))
