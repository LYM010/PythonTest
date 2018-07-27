#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：反向输出一个链表。
程序分析：无。
'''
import random

lst = [random.randint(0,100) for i in range(random.randint(0,100))]
print(lst)
lst.reverse()
print(lst)