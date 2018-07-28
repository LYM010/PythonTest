#!/usr/bin/env python3
# -*-UTF-8-*-


if __name__ == '__main__':
    tableData = [['apples','oranges','cherries','banana'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]
    colWidths = [0]*len(tableData)
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            if colWidths[i] < len(tableData[i][j]):
                colWidths[i] = len(tableData[i][j])

    for i in range(len(tableData)):
        for j in range(len(tableData[0])):
            print(tableData[i][j],end='|')
        print()
