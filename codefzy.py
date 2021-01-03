# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 19:31:26 2020

@author: Administrator
"""

import pandas as pd
import numpy as np

# a=np.array([[1,0,0,1,1],[1,1,0,0,0],[1,0,1,0,1],[0,0,1,1,1],[1,1,0,0,0]])
a = np.array([[1, 0, 1, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0]])
print(a)


def islands(a, b, inum, jnum, count):
    if b[inum][jnum] != 2 and a[inum][jnum] == 1:
        b[inum][jnum] = 2
        if inum != 0 and a[inum - 1][jnum] == 1 and b[inum - 1][jnum] != 2:  # 遍历过就是2
            b[inum - 1][jnum] = 2
            islands(a, b, inum - 1, jnum, count)
        if inum != 4 and a[inum + 1][jnum] == 1 and b[inum + 1][jnum] != 2:  # 遍历过就是2
            b[inum + 1][jnum] = 2
            islands(a, b, inum + 1, jnum, count)  # 1,2,1
        if jnum != 0 and a[inum][jnum - 1] == 1 and b[inum][jnum - 1] != 2:  # 遍历过就是2
            b[inum][jnum - 1] = 2
            islands(a, b, inum, jnum - 1, count)
        if jnum != 4 and a[inum][jnum + 1] == 1 and b[inum][jnum + 1] != 2:  # 遍历过就是2
            b[inum][jnum + 1] = 2
            islands(a, b, inum, jnum + 1, count)
        if a[inum - 1][jnum] + a[inum + 1][jnum] + a[inum][jnum - 1] + a[inum][jnum + 1] == 0 or a[inum][jnum - 1] == 1:
            count = count + 1

    return count


c = 0
b = np.zeros((5, 5))
# print(a,b[0][0],"ok")
for i in range(5):
    for j in range(5):
        c = islands(a, b, i, j, c)
        # print("@new",i,j)
print(c)
