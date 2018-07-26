#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：求1+2!+3!+...+20!的和。

程序分析：此程序只是把累加变成了累乘。 
'''
s=0
def fact(n):
   if n==1:
      return 1
   return n*fact(n-1)

for n in  range(1,21):
   a=fact(n)
   s+=a
print(s)
