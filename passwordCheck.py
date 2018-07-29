#!/usr/bin/env python3
# -*-UTF-8-*-
# passwordCheck.py

import re

def passwordCheck(pwd):
	flag = True
	if len(pwd) < 8:
		flag = False
	cpw1 = re.compile(r'[a-z]').search(pwd)
	cpw2 = re.compile(r'[A-Z]').search(pwd)
	cpw3 = re.compile(r'[0-9]').search(pwd)
	if (cpw1 == None) or cpw2 == None or cpw3 == None:
		flag = False
	return flag

pwd = str(input('Enter a Password:'))
if passwordCheck(pwd):
	print('Password Correct!')
else:
	print('Please reset your password!')