# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 22:06:09 2020

@author: Administrator
"""

import numpy as np

# 股票费
# a = np.array([1, 3, 2, 8, 4, 9])
a = np.array([1, 3, 7, 5, 10, 3])
fee = 3


def benefit(a, fee):
    mean = a.mean()
    print(mean)
    b = np.zeros(len(a))
    c = []  # 相同数字数组
    inter = 0
    for i in range(len(a)):
        if a[i] > mean:
            b[i] = 0
        else:
            if a[i] == mean:
                b[i] = 2
            else:
                b[i] = 1
    print("b", b)
    i = 0
    while i < 6:
        print("i", i)
        while i < 6 and b[i] >= 1:
            c.append(a[i])
            i = i + 1
        print("buy", c)
        if c != []:
            min_n = min(c)
            print(min_n, "fff")
            c.clear()
        while i < 6 and (b[i] == 0 or b[i] == 2):
            c.append(a[i])
            i = i + 1
        print("sell", c)
        if c != []:
            max_n = max(c)
            print(max_n, "ddd")
            c.clear()
        inter = inter + (max_n - min_n) - fee
        print("interi", inter)
    return inter


print("benefit=", benefit(a, fee))
