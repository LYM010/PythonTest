#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
题目：文本颜色设置。

程序分析：无。
'''
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = "\033[93m"
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''
    
print(bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC)
