#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，
60-89分之间的用B表示，60分以下的用C表示。
程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。
'''

def grade(s):
	if s > 100 or s < 0:
		print("Error!Please Enter The Correct Score")
		return;
	elif s >= 90:
		return 'A'
	elif s >= 60:
		return 'B'
	else:
		return 'C'

s=int(input("输入分数："))
print("Grade:",grade(s))