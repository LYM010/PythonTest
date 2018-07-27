#!/usr/bin/env python3
# -*-coding:UTF-8-*-
def collatz(num):
    print(num)
    if num == 1:
        return "succeed!"
    elif num%2 == 0:
        collatz(n = num//2)
    else:
        collatz(num*3+1)

if __name__=='__main__':
    n = int(input('Enter number:')
    print(collatz(n))
