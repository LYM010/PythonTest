#!/usr/bin/env python3
# -*-UTF8-*-
# 编写一个程序，遍历一个目录树，查找特定扩展名的文件（诸如.pdf 或.jpg），
# 不论这些文件的位置在哪里， 将它们拷贝到一个新的文件夹中。

import os,shutil,re
path =os.path.abspath( os.path.join('..','tmp'))
folder = os.path.abspath(os.path.join('..','test'))

if os.path.exists(folder):
    print('Folder exists.')
else:
    os.mkdir(folder)
    print('Folder created successfuly!')

type = 'txt'

for root,dirs,files in os.walk(path):
    for fileName in files:
        mo = re.compile(f'.*\.{type}$').search(fileName)
        if mo == None:
            continue
        else:
            fillName = os.path.join(root,mo.group())
            print(fillName)
            shutil.copy(fillName,folder)
