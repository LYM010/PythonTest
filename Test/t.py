#!/usr/bin/env python3
# -*-coding:UTF8-*-
import os
path = 'D:\\Documents\\LeonWorkSpace\\tmp'
for root,dirs,files in os.walk(path):
    for fileName in files:
        print(os.path.join(root,fileName))
