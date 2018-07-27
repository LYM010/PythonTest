#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

程序分析：无。
'''
import random

def arr_max(array=[]):
	max = array[0]
	flag = 0
	for i in range(1,len(array)):
		if max < array[i]:
			max = array[i]
			flag = i
	array[0],array[flag] = array[flag],array[0]
	return array

def arr_min(array=[]):
	min = array[0]
	flag = 0
	for i in range(1,len(array)):
		if min > array[i]:
			min = array[i]
			flag = i
	array[-1],array[flag] = array[flag],array[-1]
	return array

if __name__ == '__main__':
	l = [random.randint(0,100) for i in range(10)]
	print(l)
	print(arr_min(arr_max(l)))