#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，
8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，
及809*??后的结果。
程序分析：无。
'''
a = 809
i = 10
while(1):
	y = a * i
	if y > 1000 and 8*i>10 and 9*i>100:
		break
	else:
		i += 1
print('{} = 800 * {} + 9 * {}'.format(a*i,i,i))