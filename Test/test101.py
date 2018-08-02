#!/usr/bin/env python3
# -*-coding:UTF-8-*-
'''
题目：编写一个函数，它以一个列表值作为参数，返回一个字符串。该字符串包含所有
表项，表项之间以逗号和空格分开，并在最后一个表项之前插入and。
'''

def p(sp):
    for i in sp:
        if i != sp[-1]:
            print(i,end=', ')
        else:
            print('and {}'.format(i))
    return
if __name__ == '__main__':
    spam = ['apple','bananas','tofu','cats']
    p(spam)
