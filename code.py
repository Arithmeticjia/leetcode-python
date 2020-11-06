# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 19:31:26 2020

@author: Administrator
"""

import numpy as np

# a=np.array([[1,0,0,1,1],[1,1,0,0,0],[1,0,1,0,1],[0,0,1,1,1],[1,1,0,0,0]])
a = np.array([[1, 0, 1, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0]])
print(a)


def islands(a, inum, jnum):
    if inum < 0 or inum >= len(a) or jnum < 0 or jnum >= len(a[0]) or a[inum][jnum] == 0:
        return
    else:
        a[inum][jnum] = 0
    islands(a, inum - 1, jnum)
    islands(a, inum + 1, jnum)  # 1,2,1
    islands(a, inum, jnum - 1)
    islands(a, inum, jnum + 1)


c = 0
# print(a,b[0][0],"ok")
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] == 1:
            c = c + 1
            islands(a, i, j)
print(c)
