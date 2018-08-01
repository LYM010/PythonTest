#!/usr/bin/env python3
# -*-UTF-8-*-
'''
编写一个程序，在一个文件夹中，找到所有带指定前缀的文件，
诸如spam001.txt、spam002.txt等，并定位缺失的编号，让该程序对所有后面的文件改名，
消除缺失的编号。
作为附加的挑战，编写另一个程序，在一些连续编号的文件中，空出一些编号，
以便加入新的文件。
'''
import os,re
# 文件重排
def resortfiles(path):
    os.chdir(path)
    spamList = []
    fullList = []
    #  获取当前文件列表并排序
    for file in os.listdir('.'):
        if file.startswith('spam') and file.endswith('txt'):
            spamList.append(file)
    spamList.sort()
    # 获取最大文件编号并以这个数值创建完整列表
    fileRegex = re.compile(r'\d+')
    finalNum =int( fileRegex.search(spamList[-1]).group())
    for i in range(1,finalNum+1):
        fileNum = str(i).zfill(3)
        fullList.append('spam'+fileNum+'.txt')

    # 重命名文件
    for i in range(len(spamList)):
        if spamList[i] != fullList[i]:
            os.rename(spamList[i],fullList[i])

# 空出文件
def backwardfiles(i,j,path):
    os.chdir(path)
    spamList = []
    fullList = []
    for file in os.listdir('.'):
        if file.startswith('spam') and file.endswith('txt'):
            spamList.append(file)
    spamList.sort()
    for k in range(1,len(spamList)+j):
        fullList.append('spam'+str(k).zfill(3)+'.txt')
    print(len(fullList),fullList)
    for k in range(-1,i-len(fullList),-1):
        if spamList[k] != fullList[k]:
            os.rename(spamList[k],fullList[k])
        
if __name__ == '__main__':
    path = os.path.join('..','tmp')
    print(path)
    resortfiles(path)
