#!/usr/bin/env python3
# -*-UTF8-*-

import os
for root,dirs,files in os.walk('..'):
    for path in dirs:
        pathName = os.path.join(root,path)
        if os.path.getsize(pathName)>1024:
            print(pathName)
    for file in files:
        fileName = os.path.join(root,file)
        if os.path.getsize(fileName) > 1024:
            print(fileName)
    
