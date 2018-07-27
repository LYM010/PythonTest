#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），
凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
程序分析：无。
'''
import random

l = [x+1 for x in range(random.randint(0, 100))]
print('参加人数：{}'.format(len(l)))

flag = 1

while(len(l)) >1:
	if flag%3 ==0:
		l.pop(0)
	else:
		l.insert(len(l),l.pop(0))
	flag += 1

print('幸存者号码：{}'.format(l))